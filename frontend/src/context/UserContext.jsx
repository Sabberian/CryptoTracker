import React, {createContext, useState, useEffect} from "react";
import { apiUrl } from "../config/config";

export const UserContext = createContext();

export const UserProvider = (props) => {
    const [token, setToken] = useState(localStorage.getItem("CryptoTrackerToken"))

    useEffect(() => {
        const fetchUser = async () => {
            const requestOptions = {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + token,
                },
            };
            const response = await fetch(`${apiUrl}/users/me`, requestOptions);

            if (!response.ok) {
                setToken(null);
            }
            localStorage.setItem("CryptoTrackerToken", token);
        };
        fetchUser();
    }, [token]);
    
    return (
        <UserContext.Provider value={[token, setToken]}>
            {props.children}
        </UserContext.Provider>
    )
}