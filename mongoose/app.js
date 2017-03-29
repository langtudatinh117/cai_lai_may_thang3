var express = require('express'),
    User = require('./model/db.js');


var app = express();
var userOne = new User({ name: 'Simon' });
var userTwo = new User({ name: 'Sally' });
console.log(userOne.name); // 'Simon'
userOne.name = 'Simon Holmes';
console.log(userOne.name); // 'Simon Holmes'
userTwo.save();
userOne.save();


// respond with "hello world" when a GET request is made to the homepage
app.get('/', function(req, res) {
    res.send('hello world')
})

app.listen(3000);