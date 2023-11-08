import React from "react";
import { UserContext } from "../context/UserContext";
import { useContext, useState } from "react";
import ErrorMessage from "./ErrorMessage";

const PASSWORD_MIN_LENGTH = 5

const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirmation, setConfirmation] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [, setToken] = useContext(UserContext);

    const submitRegistration = async () => {
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email: email, password: password }),
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
            const isEmailValid = email.trim() !== "";

            if (isPasswordValid && isEmailValid) {
                submitRegistration();
            } else {
                const passwordErrorMessage = isPasswordValid ? "" : "Passwords must match and be at least " + PASSWORD_MIN_LENGTH + " characters.";
                const emailErrorMessage = isEmailValid ? "" : "Email is required.";
        
                setErrorMessage(`${passwordErrorMessage} ${emailErrorMessage}`.trim());
            }
        }

        return (
            <div className="column">
                <form className="box" onSubmit={handleSubmit}>
                    <h1 className="title has-text-centered">
                        Registration
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