import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const initialState = {
  id: 4,
};

const EmpListing = () => {
  const [empdata, setEmpdata] = useState([]);

  useEffect(() => {
    const request = async (url) => {
      const response = await fetch(url);
      if (!response.ok) throw new Error("WARN", response.status);
      const data = await response.json();
      console.log(data);
      setEmpdata(data);
    };

    request("http://127.0.0.1:3001/api/users");
  }, []);

  return (
    <div className="container">
      <div className="card">
        <div className="card-title">
          <h2>Lista de Usuarios</h2>
        </div>
        <div className="card-body">
          <div className="divbtn">
            <Link to='users/create' className="btn btn-success">Add New User (+) </Link>
          </div>
          <table className="table table-bordered">
            <thead className="bg-dark text-white">
              <tr>
                <td>ID</td>
                <td>Name</td>
                <td>Email</td>
                <td>Created_at</td>
                <td>Action</td>
              </tr>
            </thead>
            <tbody>
              {empdata &&
                empdata.map((item) => (
                  <tr key={item.id}>
                    <td>{item.id}</td>
                    <td>{item.username}</td>
                    <td>{item.email}</td>
                    <td>{item.created_at}</td>
                    <td>
                      <a className="btn btn-success">Edit</a>
                      <a className="btn btn-danger">Remove</a>
                      <a className="btn btn-primary">Details</a>
                    </td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default EmpListing;
