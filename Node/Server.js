const express = require('express');
const DataAccess = require('./DataAccess');
const app = express();
const port = 3000;

app.get('/Calculate', function (req, res) {
  DataAccess.getStats(1, 1, 1, 1, 1, 1, 1, 01);
  res.send(`This Doesn't work Yet!`)
});

app.use(express.static('public'));
app.get('/', (req, res) => res.send('Hello World!'));
app.listen(port, () => console.log(`Example app listening on port ${port}!`));