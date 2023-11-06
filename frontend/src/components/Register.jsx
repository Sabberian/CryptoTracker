import React from "react";
import { UserContext } from "../context/UserContext";
import { useContext, useState } from "react";
import ErrorMessage from "./ErrorMessage";

const PASSWORD_MIN_LENGTH = 5

const Register = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirmation, setConfirmation] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [, setToken] = useContext(UserContext);

    const submitRegistration = async () => {
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username: username, password: password }),
                };

            const response = await fetch("/api/users", requestOptions);
            const data = await response.json();
            if (!response.ok) {
                setErrorMessage(data.detail);
            } else {
                setToken(data.access_token);
            }
        };

        const handleSubmit = (e) => {
            e.preventDefault();
            
            const isPasswordValid = password === passwordConfirmation && password.length >= PASSWORD_MIN_LENGTH;
            const isUsernameValid = username.trim() !== "";

            if (isPasswordValid && isUsernameValid) {
                submitRegistration();
            } else {
                const passwordErrorMessage = isPasswordValid ? "" : "Passwords must match and be at least " + PASSWORD_MIN_LENGTH + " characters.";
                const usernameErrorMessage = isUsernameValid ? "" : "Username is required.";
        
                setErrorMessage(`${passwordErrorMessage} ${usernameErrorMessage}`.trim());
            }
        }

        return (
            <div className="column">
                <form className="box" onSubmit={handleSubmit}>
                    <h1 className="title has-text-centered">
                        Registration
                    </h1>
                    <div className="field">
                        <label className="label">Username</label>
                        <div className="control">
                            <input className="input" type="username" placeholder="Enter username"
                                value={username} onChange={(e) => { setUsername(e.target.value) }} />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Password</label>
                        <div className="control">
                            <input className="input" type="password" placeholder="Enter password"
                                value={password} onChange={(e) => { setPassword(e.target.value) }} />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Confirm password</label>
                        <div className="control">
                            <input className="input" type="password" placeholder="Confirm password"
                                value={passwordConfirmation} onChange={(e) => { setConfirmation(e.target.value) }} />
                        </div>
                    </div>
                    <ErrorMessage message={errorMessage} />
                    <br />
                    <button type="submit" className="button is-primary">Submit</button>
                </form>
            </div>
        );
    };

    export default Register;