import React, { useState, useContext } from "react";

import { UserContext } from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [, setToken] = useContext(UserContext);

    const submitLogin = async () => {
        const requestOptions = {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: JSON.stringify(`grant_type=&username=${email}&password=${password}&scope=&client_id=&client_secret=`),
        };

        const response = await fetch("/api/token", requestOptions);
        const data = await response.json();
        
        if (!response.ok) {
            setErrorMessage(data.detail);
        } else {
            setToken(data.access_token);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (email.trim() === "" || password.trim() === "") {
            setErrorMessage("Email and password are required.");
        } else {
            submitLogin();
        }
    };

    return (
        <div className="column">
            <form className="box" onSubmit={handleSubmit}>
                <h1 className="title has-text-centered">
                    Login
                </h1>
                <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                        <input className="input" type="email" placeholder="Enter email"
                            value={email} onChange={(e) => { setEmail(e.target.value) }} />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Password</label>
                    <div className="control">
                        <input className="input" type="password" placeholder="Enter password"
                            value={password} onChange={(e) => { setPassword(e.target.value) }} />
                    </div>
                </div>
                <ErrorMessage message={errorMessage} />
                <br />
                <button type="submit" className="button is-primary">Submit</button>
            </form>
        </div>
    );
};

export default Login;