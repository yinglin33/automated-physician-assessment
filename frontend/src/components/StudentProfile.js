import React from 'react';

const StudentProfile = (props) => {
    return (
        <div className='student-profile'>
            <img className='student-image' src={props.image} alt={props.alt}/>
            <div style={{marginLeft: 50}}>
                <h1> {props.name} </h1>
                <p className="student-id"> #{props.id}</p>
            </div>
        </div>
    );
};

export default StudentProfile;