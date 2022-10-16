import React from 'react';
import Entry from './Entry';
// import {Link} from "react-router-dom";
import { render } from '@testing-library/react';

const AssessmentEntry = ({entries}) => {
    return (
        <div className="assessmentEntryData">
            <div> {entries.date} </div>
            <div> {entries.name} </div>
            <a className="view-assessment" href='./Entry.js'> VIEW </a>
        </div>
    );
};

export default AssessmentEntry;