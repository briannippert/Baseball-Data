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

  var result = dataAccess.getStats(query.balls, query.strikes, query.outs, query.scoreDiff, query.first, query.second, query.third, inning).then(function (value) {
    console.log(value);
    res.send(value);
  });
  // console.log(result);

});

app.use(express.static('public'));
app.listen(port, () => console.log(`Baseball Data listening on port ${port}!`));