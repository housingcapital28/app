import requests
import sys
import json
from datetime import datetime

class HousingCapitalAPITester:
    def __init__(self, base_url="https://gurugram-luxury.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def log_test(self, name, success, details=""):
        """Log test result"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
        
        result = {
            "test": name,
            "status": "PASS" if success else "FAIL",
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)
        
        status_icon = "✅" if success else "❌"
        print(f"{status_icon} {name}: {details}")

    def run_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.api_url}/{endpoint}"
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=10)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=10)

            success = response.status_code == expected_status
            
            if success:
                try:
                    response_data = response.json()
                    details = f"Status: {response.status_code}, Response: {type(response_data).__name__}"
                    if isinstance(response_data, list):
                        details += f" with {len(response_data)} items"
                    elif isinstance(response_data, dict) and 'message' in response_data:
                        details += f" - {response_data['message']}"
                except:
                    details = f"Status: {response.status_code}"
            else:
                details = f"Expected {expected_status}, got {response.status_code}"
                try:
                    error_data = response.json()
                    if 'detail' in error_data:
                        details += f" - {error_data['detail']}"
                except:
                    details += f" - {response.text[:100]}"

            self.log_test(name, success, details)
            return success, response.json() if success else {}

        except requests.exceptions.RequestException as e:
            self.log_test(name, False, f"Request failed: {str(e)}")
            return False, {}
        except Exception as e:
            self.log_test(name, False, f"Error: {str(e)}")
            return False, {}

    def test_health_check(self):
        """Test API health check"""
        success, response = self.run_test(
            "API Health Check",
            "GET",
            "",
            200
        )
        return success

    def test_get_properties(self):
        """Test getting all properties"""
        success, response = self.run_test(
            "Get All Properties",
            "GET",
            "properties",
            200
        )
        if success and isinstance(response, list):
            self.log_test("Properties Data Validation", len(response) > 0, f"Found {len(response)} properties")
            return response
        return []

    def test_get_single_property(self, property_id):
        """Test getting a single property"""
        success, response = self.run_test(
            f"Get Property {property_id}",
            "GET",
            f"properties/{property_id}",
            200
        )
        return success, response

    def test_search_properties(self):
        """Test property search functionality"""
        # Test 1: Search by location
        search_data = {"location": "Sector 54"}
        success1, response1 = self.run_test(
            "Search Properties by Location",
            "POST",
            "properties/search",
            200,
            data=search_data
        )

        # Test 2: Search by property type
        search_data = {"property_type": "Apartment"}
        success2, response2 = self.run_test(
            "Search Properties by Type",
            "POST",
            "properties/search",
            200,
            data=search_data
        )

        # Test 3: Empty search (should return all)
        search_data = {}
        success3, response3 = self.run_test(
            "Search Properties (Empty)",
            "POST",
            "properties/search",
            200,
            data=search_data
        )

        return success1 and success2 and success3

    def test_get_projects(self):
        """Test getting all projects"""
        success, response = self.run_test(
            "Get All Projects",
            "GET",
            "projects",
            200
        )
        if success and isinstance(response, list):
            self.log_test("Projects Data Validation", len(response) > 0, f"Found {len(response)} projects")
            return response
        return []

    def test_get_testimonials(self):
        """Test getting all testimonials"""
        success, response = self.run_test(
            "Get All Testimonials",
            "GET",
            "testimonials",
            200
        )
        if success and isinstance(response, list):
            self.log_test("Testimonials Data Validation", len(response) > 0, f"Found {len(response)} testimonials")
            return response
        return []

    def test_submit_lead(self):
        """Test lead submission"""
        lead_data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "+91-9876543210",
            "message": "Interested in properties in Sector 54",
            "source": "website"
        }
        
        success, response = self.run_test(
            "Submit Lead",
            "POST",
            "leads",
            200,
            data=lead_data
        )
        return success, response

    def test_get_leads(self):
        """Test getting all leads (admin endpoint)"""
        success, response = self.run_test(
            "Get All Leads",
            "GET",
            "leads",
            200
        )
        return success, response

    def run_all_tests(self):
        """Run all API tests"""
        print("🏠 Starting Housing Capital API Tests")
        print("=" * 50)

        # Test 1: Health Check
        if not self.test_health_check():
            print("❌ API is not responding. Stopping tests.")
            return False

        # Test 2: Properties
        properties = self.test_get_properties()
        if properties:
            # Test getting a single property
            first_property = properties[0]
            if 'id' in first_property:
                self.test_get_single_property(first_property['id'])

        # Test 3: Property Search
        self.test_search_properties()

        # Test 4: Projects
        self.test_get_projects()

        # Test 5: Testimonials
        self.test_get_testimonials()

        # Test 6: Lead Submission
        lead_success, lead_response = self.test_submit_lead()
        
        # Test 7: Get Leads (if lead submission worked)
        if lead_success:
            self.test_get_leads()

        # Print Summary
        print("\n" + "=" * 50)
        print(f"📊 Test Summary: {self.tests_passed}/{self.tests_run} tests passed")
        
        if self.tests_passed == self.tests_run:
            print("🎉 All tests passed!")
            return True
        else:
            print(f"⚠️  {self.tests_run - self.tests_passed} tests failed")
            return False

    def get_test_report(self):
        """Get detailed test report"""
        return {
            "total_tests": self.tests_run,
            "passed_tests": self.tests_passed,
            "failed_tests": self.tests_run - self.tests_passed,
            "success_rate": (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0,
            "test_results": self.test_results
        }

def main():
    tester = HousingCapitalAPITester()
    success = tester.run_all_tests()
    
    # Save test report
    report = tester.get_test_report()
    with open('/app/backend_test_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Test report saved to: /app/backend_test_report.json")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())