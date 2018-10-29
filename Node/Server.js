const express = require('express');
const dataAccess = require('./DataAccess.js');
const app = express();
const port = 3000;

app.get('/Calculate', function (req, res) {
  var url = require('url');
  var url_parts = url.parse(req.url, true);
  var query = url_parts.query;
  var inning = query.topBottom + "" + query.inning;
  if (query.first == null) {
    query.first = false;
  }
  if (query.second == null) {
    query.second = false;
  }
  if (query.third == null) {
    query.third = false;
  }
  console.log("First Base: " + query.first);
  console.log(inning);
  var nums = dataAccess.getStats(query.balls, query.strikes, query.outs, query.scoreDiff, query.first, query.second, query.third, inning);
  res.send(nums);
});

app.use(express.static('public'));
app.listen(port, () => console.log(`Example app listening on port ${port}!`));