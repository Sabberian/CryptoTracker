import React, { useEffect, useState } from "react";

const App = () => {
  const [message, setMessage] = useState("");

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
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <div>
      Hello, world!
    </div>
  );
}

export default App;
