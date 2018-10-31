const express = require('express');
const app = express();
var fs = require('fs');
const port = 3000;


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
  try {
    var obj = JSON.parse(fs.readFileSync('./Node/public/results.json', 'utf8'));
    console.log(obj["01"]["-1"]["2"]["0"]["0"]["0"]["0"]["0"]);
    console.log(obj["01"]["-1"]["2"]["0"]["0"]["0"]["0"]["1"]);
  } catch (e) {
    console.log(e);
  }

});

app.use(express.static('public'));
app.listen(port, () => console.log(`Baseball Data listening on port ${port}!`));