const express = require('express');
const app = express();
const port = 3000;
const dbName = 'BaseBall-Data';
games = [];
const MongoClient = require('mongodb').MongoClient;
const test = require('assert');
const Mongourl = 'mongodb://localhost:27017';


app.get('/Calculate', function (req, res) {
  var url = require('url');
  var url_parts = url.parse(req.url, true);
  var query = url_parts.query;
  var inning = query.topBottom + "" + query.inning;
  if (query.first == null) {
    query.first = false;
  } else {
    query.first = true;
  }
  if (query.second == null) {
    query.second = false;
  } else {
    query.second = true;
  }
  if (query.third == null) {
    query.third = false;
  } else {
    query.third = true;
  }
  
});

app.use(express.static('public'));
app.listen(port, () => console.log(`Baseball Data listening on port ${port}!`));