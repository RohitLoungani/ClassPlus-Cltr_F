const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const userInfo=require('./api/models/user');
const userRoute=require('./api/routes/user');
//console.log(userSchema);
const DB="mongodb+srv://classplus:hackfest21@cluster0.sfamx.mongodb.net/classplus?retryWrites=true&w=majority";
mongoose.connect(DB,{
    useNewUrlParser:true,
    useCreateIndex:true,
    useUnifiedTopology:true,
    useFindAndModify:false
}).then(()=>{console.log("Connection Succesfull!")}).catch((err)=>{console.log("No Connection")});

app.use('/uploads', express.static('uploads'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


// Routes which should handle requests
app.use("/user", userRoute);

app.listen(3000);



