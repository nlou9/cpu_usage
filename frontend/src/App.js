import './App.css';
import React, { useState, useEffect } from "react";

function App() {
  const [cpu, setCpu] = useState(null);
  //fetch from backend
  const fetchData = async()=>{
    const url = 'http://127.0.0.1:8000/cpu/1'
    const res = await fetch(url);
    if (res.status === 200) {
      const cpuInfo = await res.json();

      if (cpuInfo) {
        setCpu(cpuInfo);
      } else {
        console.error("Error");
      }
    } else {
      console.error("Error response code");
    }
  };
  useEffect(() => {
    fetchData();
  }, []);
  if (!cpu){
    return <div>Loading.....</div>
  }
    return (
      <h1>got data</h1>
    );
}

export default App;
