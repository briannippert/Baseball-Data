const express = require('express');
const dataAccess = require('./DataAccess.js');
const app = express();
const port = 3000;

app.get('/Calculate', function (req, res) {
  var url = require('url');
  var url_parts = url.parse(request.url, true);
  var query = url_parts.query;
  dataAccess.getStats(query.balls, 1, 1, 1, 1, 1, 1, "01");
  res.send(`This Doesn't work Yet!`);
});

app.use(express.static('public'));
app.get('/', (req, res) => res.send('Hello World!'));
app.listen(port, () => console.log(`Example app listening on port ${port}!`));