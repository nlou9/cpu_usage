import './App.css';
import React, { useRef, useState, useEffect } from "react";
// import Highcharts, { setOptions } from 'highcharts';
// import HighchartsReact from 'highcharts-react-official';
import { Line } from "react-chartjs-2"

const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: ''
    }
  }
}


function App() {
  const [chartData, setChartData] = useState({});
  const ref = useRef();
  //fetch from backend
  const fetchData = async()=>{
    let timeList = [];
    let usage = [] 
    const url = 'http://localhost:8000/cpu/1/realtime'

    const res = await fetch(url);
    
    if (res.status === 200) {
      const data = await res.json();
      console.log(data);
      if (data) {
        for (const dataObj of data){
          timeList.push(dataObj.created)
          usage.push(dataObj.sys_usage + dataObj.user_usage)      
        } 
      console.log(timeList.slice(0,10))
      console.log(usage.slice(0,10)) 

      setChartData({
        labels: timeList,
        datasets: [{
          label: 'CPU Total Usage',
          data: usage,
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      });
      console.log("chartdata...")
      console.log(chartData);
      }else{
        console.error("Response body is empty");
      }
    }else{
      console.error("Response code error");
    }
  };
  useEffect(() => {
    let interval = setInterval(() => fetchData(), (1000 * 15))
    //destroy interval on unmount
    return () => clearInterval(interval);
  }, []);


  if (chartData.datasets){
    return(
      <div className="App">
          <h1>Server Real Time CPU Usage Monitor</h1>  
            <Line data={chartData} options={options} />  
      </div>
    )   
  }
  return (<div>Loading..</div>)
}

export default App;
