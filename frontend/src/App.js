import React, { useEffect, useState, useContext } from "react";
import Register from "./components/Register";
import Header from "./components/Header";
import { UserContext } from "./context/UserContext";
import Login from "./components/Login";
import CryptoChart from "./components/CryptoChart";

const App = () => {
  const [message, setMessage] = useState("");
  const [cryptoData, setCryptoData] = useState([]);
  const [token] = useContext(UserContext);

  const loadCryptoData = async () => {
    const opts = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      }
    };
    const cryptoListResponse = await fetch("/api/currencies", opts);
    console.log(cryptoListResponse);
    const cryptoList = await cryptoListResponse.json();
    console.log(cryptoList);

    const cryptoDataPromise = cryptoList.map(async (crypto) => {
      const response = await fetch(`/api/crypto-chart/${crypto.name}`, opts);
      const data = await response.json();
      return data;
    });

    const cryptoData = await Promise.all(cryptoDataPromise);
    setCryptoData(cryptoData);
  };

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
    loadCryptoData();
  }, []);

  return (
    <div>
      <Header title={message} />
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds ">
          { token ? (
            <div>              
              <h1>Crypto Price Chart</h1>
              {cryptoData.map((data, index) => (
                <CryptoChart key={index} data={data} />
              ))}
            </div>
          ) : (
            <div className="columns">
              <Register /> 
              <Login />
            </div>
          )}
        </div>
        <div className="column"></div>
      </div>
    </div>
  );
}

export default App;
