import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage } from "@/pages/HomePage";
import { PropertyDetailsPage } from "@/pages/PropertyDetailsPage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/property/:id" element={<PropertyDetailsPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
