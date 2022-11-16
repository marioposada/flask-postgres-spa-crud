import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";

const EmpDetail = () => {
  const { empid } = useParams();
  const [empdata, setEmpdata] = useState([]);

  useEffect(() => {
    const request = async (url) => {
      const response = await fetch(url);
      if (!response.ok) throw new Error("WARN", response.status);
      const data = await response.json();
      console.log(data);
      setEmpdata(data);
    };

    request("http://127.0.0.1:3001/api/users/" + empid);
  }, []);

  return (
    <div className="container">
      <div className="card">
        <div className="card-title">
          <h2>User Details</h2>
        </div>
        <div className="card-body">
          <table className="table table-bordered">
            <thead className="bg-dark text-white">
              <tr>
                <td>ID</td>
                <td>Name</td>
                <td>Email</td>
                <td>Created_at</td>
              </tr>
            </thead>
            <tbody>
              {empdata && (
                <tr key={empdata.id}>
                  <td>{empdata.id}</td>
                  <td>{empdata.username}</td>
                  <td>{empdata.email}</td>
                  <td>{empdata.created_at}</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
        <div className="divbtn">
            <Link to="/" className="btn btn-success">
              Back {" "}
            </Link>
          </div>
      </div>
    </div>
  );
};

export default EmpDetail;
