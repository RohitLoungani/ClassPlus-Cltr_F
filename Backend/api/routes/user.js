const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const multer = require('multer');

const storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, './uploads/');
  },
  filename: function(req, file, cb) {
    cb(null, new Date().toISOString() + file.originalname);
  }
});

const fileFilter = (req, file, cb) => {
  // reject a file
  if (file.mimetype === 'image/jpeg' || file.mimetype === 'image/png') {
    cb(null, true);
  } else {
    cb(null, false);
  }
};

const upload = multer({
  storage: storage,
  limits: {
    fileSize: 1024 * 1024 * 5
  },
  fileFilter: fileFilter
});

const User = require("../models/user");

router.post("/", upload.single('userImage'), (req, res, next) => {
  const user = new User({
    contactNo: req.body.contactNo,
    name: req.body.name,
    userImage: req.file.path 
  });
  user
    .save()
    .then(result => {
      console.log(result);
      res.status(201).json({
        message: "Registered successfully",
        registeredUser: {
            contactNo: result.contactNo,
            name: result.name,
            request: {
                type: 'GET',
                url: "http://localhost:3000/user/" + result._id
            }
        }
      });
    })
    .catch(err => {
      console.log(err);
      res.status(500).json({
        error: err
      });
    });
});

router.get("/:contactNo", (req, res, next) => {
  const id = req.params.contactNo;

  User.findOne({contactNo: id})
    .select('contactNo name userImage')
    .exec()
    .then(doc => {
      console.log("From database", doc);
      if (doc) {
        res.status(200).json({
            user: doc,
            request: {
                type: 'GET',
                url: 'http://localhost:3000/user'
            }
        });
      } else {
        res
          .status(404)
          .json({ message: "No valid entry found for provided ID" });
      }
    })
    .catch(err => {
      console.log(err);
      res.status(500).json({ error: err });
    });
});
module.exports = router;