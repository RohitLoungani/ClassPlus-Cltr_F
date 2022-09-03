import React, { useState, useCallback } from 'react';
import Webcam from 'react-webcam';

import { Button, Form, FormGroup, FormControl, FormLabel, Label, Input } from 'reactstrap'

const WebcamCapture = () => {
    const webcamRef = React.useRef(null);
    // const [imgSrc, setImgSrc] = React.useState(null);

    let imgSrc = null;

    const capture = React.useCallback(() => {

        imgSrc = webcamRef.current.getScreenshot();

    }, [webcamRef]);

    return (
        <>
            <Webcam
                audio={false}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                height="150px"
                widht="250px"
                minScreenshotWidth="250px"
                minScreenshotHeight="150px"
            />
            <Button color="info" style={{ marginTop: "20px" }} onClick={capture}>Retake</Button>
            {imgSrc && (
                <img
                    src={imgSrc}
                />
            )}
        </>
    );
}


function Verify() {
    return (
        <div className="d-flex flex-row justify-content-center align-items-center" style={{ marginTop: "100px" }}>
            <div className="d-flex flex-column">
                <div>
                    <img src="./images/logo.jpg" alt="" />
                </div>
                <WebcamCapture />

            </div>

            {/* Camera ka foto */}

            <div className="d-flex flex-column mx-5">

                <p style={{ color: "green" }}> <del> Face Recognized </del> </p>

                <p>Face registered</p>
                <p>Cofirm Detection</p>

                <Button color="success" style={{ marginTop: "20px" }}>Enter Class</Button>
            </div>

        </div>
    )
}

export default Verify
