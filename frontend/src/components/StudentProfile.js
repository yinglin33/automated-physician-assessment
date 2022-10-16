import React from 'react';

const StudentProfile = (props) => {
    return (
        <div className='student-profile'>
            <img className='student-image' src={props.image} alt={props.alt}/>
            <h1> {props.name} </h1>
            <p className="student-id"> #{props.id}</p>
        </div>
    );
};

export default StudentProfile;