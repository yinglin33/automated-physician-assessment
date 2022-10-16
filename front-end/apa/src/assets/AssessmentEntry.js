import React from 'react';

const AssessmentEntry = ({entries}) => {
    return (
        <div className="assessmentEntryData">
            <div> {entries.date} </div>
            <div> {entries.name} </div>
            <a className="view-assessment" href={entries.url}> VIEW </a>
        </div>
    );
};

export default AssessmentEntry;