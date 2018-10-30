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
MongoClient.connect(Mongourl, function (err, db) {
  if (err) throw err;
  var dbo = db.db("Baseball-Data");
  var query2 = {
    '$and': [{
        'ball': parseInt(query.balls)
      },
      {
        'strike': parseInt(query.strikes)
      },
      {
        'out': parseInt(query.outs)
      },
      {
        'scoreDiff': parseInt(query.scoreDiff)
      },
      {
        'first': query.first
      },
      {
        'second': query.second
      },
      {
        'third': query.third
      },
      {
        'inning': inning
      }
    ]
  };
  console.log(query)
  dbo.collection("pitches").find(query2).toArray(function (err, result) {
    if (err) throw err;
    filteredTotal = 0;
    for (i in result) {
      //   console.log(result[i])
      if (result[i].winningTeam == true) {
        filteredTotal++;
      }
      let gameId = result[i]["id"];
      if (gameId in games) {
        console.log(result[i]["id"]);
      }
      if (!gameId.endsWith("0")) {
        console.log(gameId);
        console.log(result[i]);
      }
      games.push(gameId);
    }
    console.log(games.length);
    console.log(filteredTotal);
    var result = ((filteredTotal / games.length) * 100).toFixed(2) + "%"
    res.send(result);
    db.close();
  });
});
});

app.use(express.static('public'));
app.listen(port, () => console.log(`Baseball Data listening on port ${port}!`));