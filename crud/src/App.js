import logo from "./logo.svg";
import "./App.css";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import EmpListing from "./EmpListing";
import EmpCreate from "./EmpCreate";
import EmpDetail from "./EmpDetail";
import EmpEdit from "./EmpEdit";

function App() {
  return (
    <div className="App">
      <h1>CRUD React + Flask(Python)</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<EmpListing />} />
          <Route path="/users/create" element={<EmpCreate />} />
          <Route path="/users/detail/:empid" element={<EmpDetail />} />
          <Route path="/users/edit/:empid" element={<EmpEdit />} />
        </Routes>
      </BrowserRouter>
      ;
    </div>
  );
}

export default App;
