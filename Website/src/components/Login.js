import React from 'react'
import { Button, Form, FormGroup, FormControl, FormLabel, Label, Input } from 'reactstrap'


function Login() {
    return (
        <div className="d-flex flex-row justify-content-center align-items-center" style={{ marginTop: "100px" }}>
            <div className="d-flex flex-column">
                <div>
                    <img src="./images/logo.jpg" alt="" />
                </div>
                <h4 >Enter Class</h4>

                <Form className="login-form" style={{ maxWidth: "300px" }}>
                    <FormGroup>
                        <Input type="name" placeholder="Name" />
                    </FormGroup>
                    <FormGroup>
                        <Input type="tel" placeholder="Mobile Number" />
                    </FormGroup>
                    <FormGroup>
                        <Button color="info" onClick={alert('Name & contact saved in store')} >Enter</Button>
                    </FormGroup>
                </Form>

                <p>not registered yet? <b>Register Now</b></p>

            </div>

            <div className="d-flex">
                <img src="./images/robot.jpg" alt="" />
            </div>

        </div>
    )
}

export default Login
