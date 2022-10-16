import React from 'react';
import logo from '../logo.svg'
import StudentProfile from '../assets/StudentProfile'
import AssessmentEntry from '../assets/AssessmentEntry'
import AssessmentData from '../assets/AssessmentData'
import '../App.css';


const Home = () => {
  const assessmentData = AssessmentData.assessments.entries;
  return (
    <div>
      {/* <header className="Automated Physician Assessment"> */}
      <StudentProfile image={logo} name="Pradeep Mani Rathnam" id="123456789"></StudentProfile>

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
        
      {/* </header> */}
    </div>
  );
};

export default Home;
