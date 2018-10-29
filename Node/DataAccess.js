const MongoClient = require('mongodb').MongoClient;
const test = require('assert');
// Connection url
const url = 'mongodb://localhost:27017';
const dbName = 'BaseBall-Data';

games = [];
module.exports.getStats = getStats;

function getStats(ball, strike, out, scoreDiff, first, second, third, inning) {
    MongoClient.connect(url, function (err, db) {
        if (err) throw err;
        var dbo = db.db("Baseball-Data");
        var query = {
            '$and': [{
                    'ball': parseInt(ball)
                },
                {
                    'strike': parseInt(strike)
                },
                {
                    'out': parseInt(out)
                },
                {
                    'scoreDiff': parseInt(scoreDiff)
                },
                {
                    'first': first
                },
                {
                    'second': second
                },
                {
                    'third': third
                },
                {
                    'inning': inning
                }
            ]
        };
        dbo.collection("pitches").find(query).toArray(function (err, result) {
            if (err) throw err;
            filteredTotal = 0;
            for (i in result) {
                //   console.log(result[i])
                if (result[i].winningTeam == true) {
                    filteredTotal++;
                }
                let gameId = result[i]["id"];
                if (gameId in games) {
                    // console.log(result[i]["id"]);
                }
                if (!gameId.endsWith("0")) {
                    // console.log(gameId);
                    // console.log(result[i]);
                }
                games.push(gameId);

            }
            // console.log(games.length);
            // console.log(filteredTotal);
            var decimal = (filteredTotal / games.length) * 100;
            var percent = decimal.toFixed(2);
            db.close();
            console.log(percent + "%");
            return percent + "%";
        });
    });
}


// getStats(
//     ball=0,
//     strike=0,
//     out=0,
//     scoreDiff=0,
//     first=false,
//     second=false,
//     third=false,
//     inning='01'
// );