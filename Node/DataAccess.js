const MongoClient = require('mongodb').MongoClient;
const test = require('assert');
// Connection url
const url = 'mongodb://localhost:27017';
const dbName = 'BaseBall-Data';


function getStats() {
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
        var dbo = db.db("Baseball-Data");
        var query = { inning: "116" };
        dbo.collection("pitches").find(query).toArray(function(err, result) {
          if (err) throw err;
          console.log(result);
          db.close();
        });
    });
}

getStats();