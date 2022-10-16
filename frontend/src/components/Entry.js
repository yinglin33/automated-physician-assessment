import React from "react";
import backArrow from '../back-arrow.png'
function Entry() {
    return (
        <div className="entry-body">
            <a href='App.js' class='back-button'> <img src={backArrow} />  Back </a>

            <div className="entry-header">

                <div className="info">
                    <h1> Pradeep Mani Rathnam's Exam Score</h1>
                    <h3> Date: 10/15/2022</h3>
                    <h3> Administered By: Kelly Ye</h3>
                </div>

                <div className='score'>
                    <h4 style={{marginRight: 'auto', marginLeft: 'auto', textAlign:'center'}}> Overall Score </h4>
                    <div class="score-circle">
                        <p class="score-num"> 7 </p>
                        <p class="out-of"> of 9 points </p>
                    </div>
                </div>
            </div>

            <div className="entry-field">
                <h4> Transcript </h4>
                <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eu turpis molestie, dictum est a, mattis tellus. Sed dignissim, metus nec fringilla accumsan, risus sem sollicitudin lacus, ut interdum tellus elit sed risus. Maecenas eget condimentum velit, sit amet feugiat lectus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent auctor purus luctus enim egestas, ac scelerisque ante pulvinar. </p>
            </div>

            <div className="entry-field">
                <h4> Type of Questions </h4>
                <p> This criteria analyzes the physician's strategy to  gain  accurate information  in  an  organized  and  efficient  manner,  the  interviewer  should  follow  a  line  of inquiry  that  progresses  from  the  open-ended  to  the  specific  to  the  direct. </p>

                <h4 style={{marginTop: 25}}> AI Generated Feedback </h4>
                <p> The AI has given you a comment about the spectrum of concern. </p>
            </div>

            <div className="entry-field">
                <h4> Use of Jargon </h4>
                <p>  This criteria analyzes the physician’s ability to refrain from using medical jargon when not absolutely necessary, and their ability to communicate a patient’s condition to the patient clearly. </p>

                <h4 style={{marginTop: 25}}> AI Generated Feedback </h4>
                <p> The AI has given you a comment about the spectrum of concern. </p>
            </div>
        </div>
    );
}

export default Entry;