import './App.css';
import logo from './logo.svg'
import React, {useState} from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import StudentProfile from './components/StudentProfile'
import AssessmentEntry from './components/AssessmentEntry'
import AssessmentData from './components/AssessmentData'
import Entry from './components/Entry'
import Pradeep from './pradeep.jpeg'

// import axios from 'axios';

const assessmentData = AssessmentData.assessments.entries;

function App() {

  // const [file, setFile] = useState()

  // function handleChange(event) {
  //   setFile(event.target.files[0])
  // }

  // function handleSubmit(event) {
  //   event.preventDefault()
  //   const url = 'http://localhost:3000/uploadFile';
  //   const formData = new FormData();
  //   formData.append('file', file);
  //   formData.append('fileName', file.name);
  //   const config = {
  //     headers: {
  //       'content-type': 'multipart/form-data',
  //     },
  //   };
  //   axios.post(url, formData, config).then((response) => {
  //     console.log(response.data);
  //   });

  // }

  return (
    <div className="App">
        {/* <form onSubmit={handleSubmit}>
          <h1>React File Upload</h1>
          <input type="file" onChange={handleChange}/>
          <button type="submit">Upload</button>
        </form> */}
      <Router>
        <Routes>
          <Route path='/Entry' element={<Entry/>}/>
        </Routes>
      </Router>
        <StudentProfile image={Pradeep} name="Pradeep Mani Rathnam" id="123456789"></StudentProfile>
        <div className='assessment-table'>
          <div className='assessment-table-header'>
            <h2> Date of Assessment </h2>
            <h2> Administrator </h2>
            <div class='new-instance-button'> + NEW</div>
          </div>

          <div className='assessment-data'>
            {assessmentData.map((entries) => (
              <AssessmentEntry entries={entries}> </AssessmentEntry>))}
          </div>
        </div>
    </div>
  );
}

export default App;
