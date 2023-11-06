import React, { useEffect, useState, useContext } from "react";
import Register from "./components/Register";
import Header from "./components/Header";
import { UserContext } from "./context/UserContext";

const App = () => {
  const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const opts = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      }
    };
    const response = await fetch("/api", opts);
    const data = await response.json();

    if (!response.ok) {
      console.log("Error: " + JSON.stringify(response));
    } else {
      setMessage(data.message);
    }
    console.log(data.message);
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <div>
      <Header title={message} />
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds ">
          { !token ? (
            <div className="columns">
              <Register /> <p>Login</p>
            </div>
          ) : (
            <p>Table</p>
          )}
        </div>
        <div className="column"></div>
      </div>
    </div>
  );
}

export default App;
