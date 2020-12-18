import './App.css';
import {Bar} from 'react-chartjs-2';
import api from './api'
import { useEffect } from 'react';
import React from 'react';
import {Image, Badge} from "react-bootstrap";

function App() {
  let [weeklycommitlabelData, setweeklycommitlabelData] = React.useState('')
  let [weeklycommitvalueData, setweeklycommitvalueData] = React.useState('')
  let [monthlycommitlabelData, setmonthlycommitlabelData] = React.useState('')
  let [monthlycommitvalueData, setmonthlycommitvalueData] = React.useState('')
  let [committersData, setcommittersData] = React.useState([])
  let [languagesData, setlanguagesData] = React.useState({})

  useEffect(() => {
    api.getWeeklyCommitsList()
    .then((response)=>{
        setweeklycommitlabelData(response.data.map((item, index, items) => { return item['_id'] }))
        setweeklycommitvalueData(response.data.map((item, index, items) => { return item['count'] }))
    })
    api.getMonthlyCommitsList()
    .then((response)=>{
        setmonthlycommitlabelData(response.data.map((item, index, items) => { return item['_id'] }))
        setmonthlycommitvalueData(response.data.map((item, index, items) => { return item['count'] }))
    })
    api.getCommittersList()
    .then((response)=>{
        console.log(response.data)
        setcommittersData(response.data)
    })
    api.getLangaguesList()
    .then((response)=>{
        console.log(response.data)
        setlanguagesData(response.data)
    })
  }, []);

  const weekly_state = {
    labels: weeklycommitlabelData,
    datasets: [
      {
        label: 'Commits',
        backgroundColor: 'rgba(75,192,192,1)',
        borderColor: 'rgba(0,0,0,1)',
        borderWidth: 2,
        data: weeklycommitvalueData
      }
    ]
  }

  const monthly_state = {
    labels: monthlycommitlabelData,
    datasets: [
      {
        label: 'Commits',
        backgroundColor: 'rgba(75,192,192,1)',
        borderColor: 'rgba(0,0,0,1)',
        borderWidth: 2,
        data: monthlycommitvalueData
      }
    ]
  }

  return (
    <div className="App">
      <div>
        <h3>My solution: I get all commits in from 01/10 from api and store to mongo, after that I build apis to get data and render</h3>
        <h3>I have problem with limitation of github api although I have used github personal token, I only get 1000 records per search so maybe data in this page isn't totally corrected</h3>
      </div>
      <div class="container">
        <div class="col-2">
          <div>
            <Bar
            data={weekly_state}
            options={{
              title:{
                display:true,
                text:'Commits per week in last 3 months',
                fontSize:20
              }
            }}
          />
          </div>
          <div>
          <Bar
            data={monthly_state}
            options={{
              title:{
                display:true,
                text:'Commits per month',
                fontSize:20
              }
            }}
          />
        </div>
        <ul></ul>
        {Object.keys(languagesData).map(l => <li>{l}</li>)}
        </div>
        <div class="col-3">
        {committersData.map(img =>  <Image src={img._id} rounded />)}
        </div>
      </div>
    </div>
  );
}

export default App;
