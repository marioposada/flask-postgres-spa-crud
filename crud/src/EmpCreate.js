import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

const EmpCreate = () => {
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [active, setActive] = useState(true);

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log({ username, email, password });

    (async () => {
      const response = await fetch("http://127.0.0.1:3001/api/users", {
        method: "POST",
        headers: {
          Accept: "application/json, text/plain, */*",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          email: email,
          password: password,
        }),
      });
      if (!response.ok) console.log(response);
      const data = await response.json();
      alert("User saved");
      navigate("/");
    })();
  };
  return (
    <div>
      <div className="row">
        <div className="offset-lg-3 col-lg-6">
          <form className="container" onSubmit={handleSubmit}>
            <div className="card" style={{ "text-align": "left" }}>
              <div className="card-title">
                <h2>Crear Usuario</h2>
              </div>
              <div className="card-body">
                <div className="row">
                  <div className="col-lg-12">
                    <div className="form-group">
                      <label>Name</label>
                      <input
                        value={username}
                        onChange={(e) => setUserName(e.target.value)}
                        className="form-control"
                      ></input>
                    </div>
                  </div>
                  <div className="col-lg-12">
                    <div className="form-group">
                      <label>Email</label>
                      <input
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="form-control"
                      ></input>
                    </div>
                  </div>
                  <div className="col-lg-12">
                    <div className="form-group">
                      <label>Password</label>
                      <input
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="form-control"
                      ></input>
                    </div>
                  </div>
                  <div className="col-lg-12">
                    <div className="form-check">
                      <input
                        checked={active}
                        type="checkbox"
                        className="form-check-input"
                        onChange={(e) => setActive(e.target.checked)}
                      ></input>
                      <label className="form-check-label">Is active</label>
                    </div>
                  </div>
                  <div className="col-lg-12">
                    <div className="form-group">
                      <button type="submit" className="btn btn-success">
                        Save
                      </button>
                      <Link to="/" className="btn btn-danger">
                        Back
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default EmpCreate;
