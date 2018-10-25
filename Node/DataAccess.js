const MongoClient = require('mongodb').MongoClient;
const test = require('assert');
// Connection url
const url = 'mongodb://localhost:27017';
const dbName = 'BaseBall-Data';


function getStats() {
    MongoClient.connect(url, function(err, client) {
        if (err) throw err;
        var dbo = db.db("BaseBall-Data");
        var query = { address: "Park Lane 38" };
        dbo.collection("BaseBall-Data").filter(query).toArray(function(err, result) {
          if (err) throw err;
          console.log(result);
          db.close();
        });
    });
}

