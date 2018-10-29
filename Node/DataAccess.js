const MongoClient = require('mongodb').MongoClient;
const test = require('assert');
// Connection url
const url = 'mongodb://localhost:27017';
const dbName = 'BaseBall-Data';

games = [];

async function getStats(ball, strike, out, scoreDiff, first, second, third, inning) {
    MongoClient.connect(url, async function (err, db) {
        if (err) throw err;
        var dbo = db.db("Baseball-Data");

        var myPromise = () => {
            return new Promise((resolve, reject) => {
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
                //console.log(query)
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
                    //console.log("Games :" + games.length);
                    //console.log("Games :" + filteredTotal);
                    var decimal = (filteredTotal / games.length) * 100;
                    var percent = decimal.toFixed(2);
                    //    console.log(percent + "%");
                    resolve(percent + "%");
                });
            });
        };
        // var result = myPromise().then(ret_val => {
        //     // console.log(ret_val);
        //     return ret_val;
        // });
        return await myPromise();

    });
}

module.exports.getStats = getStats;
var output = getStats(
    ball = 0,
    strike = 0,
    out = 0,
    scoreDiff = 0,
    first = false,
    second = false,
    third = false,
    inning = '01'
);