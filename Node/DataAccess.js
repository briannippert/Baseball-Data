const MongoClient = require('mongodb').MongoClient;
const test = require('assert');
// Connection url
const url = 'mongodb://localhost:27017';

const dbName = 'BaseBall-Data';


function getStats() {

    MongoClient.connect(url, function(err, client) {
 
    });
}

