import React from 'react';

const AssessmentEntry = ({entries}) => {
    return (
        <div className="assessmentEntryData">
            <div> {entries.date} </div>
            <div> {entries.name} </div>
            <a className="view-assessment" href='instagram.com'> VIEW </a>
        </div>
    );
};

export default AssessmentEntry;