const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    contactNo: {
        type : String,
        maxlength: 20,
        primaryKey: true
    },
    name: { 
        type: String, 
        required: true 
    },
    userImage: { 
        type: String, 
        required: true 
    },
    
});

module.exports = mongoose.model('User', userSchema);