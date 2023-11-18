import React, { useState, useContext } from "react";
import ErrorMessage from "./ErrorMessage";
import { UserContext } from "../context/UserContext";
import { apiUrl } from "../config/config";

const ChartMenu = ({ direction, setDirection, currencyId }) => {
    const [price, setPrice] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [token] = useContext(UserContext);

    const getCurrentUser = async () => {
        try {
            const requestOptions = {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
            };
            const response = await fetch(`${apiUrl}/users/me`, requestOptions);
            if (response.ok) {
                const user = await response.json();
                return user;
            } else {
                console.error("Error while fetching current user: " + response);
                return null;
            }
        } catch (error) {
            console.error("Error while fetching current user:", error);
            return null;
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        const isPriceValid = parseFloat(price.replace(",", ".")) > 0;
        
        if (isPriceValid) {

            const currentUser = await getCurrentUser();

            const notificationData = {
                threshold: parseFloat(price),
                direction: direction,
                user_id: currentUser.id,
                currency_id: currencyId,
            };
            try {
                const requestOptions = {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`
                    },
                    body: JSON.stringify(notificationData),
                };
    
                const response = await fetch(`${apiUrl}/notifications`, requestOptions);
                if (response.ok) {
                    setPrice("");
                    setErrorMessage("");
                } else {
                    const data = await response.json();
                    setErrorMessage(data.detail);
                }
            } catch (error) {
                console.error("Error while sending notification: " + error);
                setErrorMessage("Error while sending notification");
            }
        } else {
            setErrorMessage("Invalid price. Please enter a valid number.");
        }
    };

    return (
        <div className="chart-menu">
            <input className="input is-primary" type="text" placeholder="Price" name="price" value={price} onChange={(e) => setPrice(e.target.value)}/>
            <button
                onClick={() => setDirection("up")}
                className={`button is-info ${direction === "up" ? "" : "is-light"}`}
            >
                Up
            </button>
            <button
                onClick={() => setDirection("down")}
                className={`button is-info ${direction === "down" ? "" : "is-light"}`}
            >
                Down
            </button>
            <button className="button is-primary" onClick={handleSubmit}>
                Start Tracking
            </button>
            <ErrorMessage message={errorMessage} />
        </div>
    );
};

export default ChartMenu;