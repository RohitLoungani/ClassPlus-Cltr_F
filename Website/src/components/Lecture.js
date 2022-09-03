import React from 'react'

import { Button, Form, FormGroup, FormControl, FormLabel, Label, Input } from 'reactstrap'

function Lecture() {
    return (
        <div className="d-flex justify-content-center" style={{ marginTop: "30px" }}>
            <div className="d-flex flex-column">
                <div>
                    <img src="./images/logo.jpg" alt="" />
                </div>
                <div>
                    <img src="https://via.placeholder.com/1100x350" alt="" style={{ marginTop: "20px" }} />
                </div>

                <p>Class Name: </p>
                <p>Student Name: </p>
                <p style={{ display: "inline" }}>Attendance: <p style={{ color: "green", display: "inline" }}> Present </p></p>

            </div>

        </div>
    )
}

export default Lecture