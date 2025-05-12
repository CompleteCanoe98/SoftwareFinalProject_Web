const express = require('express');
const path = require('path');
const sqlite3 = require('sqlite3');
const { open } = require('sqlite');

PORT=8080;

/////////////////////////////////////////////
// connect to db

let db;
(async () => {
	db = await open({
		filename: 'users.sqlite3',
		driver: sqlite3.Database
	});
	console.log("database connected!");
})();

/////////////////////////////////////////////
// express and middleware setup

app = express();

// encoding for form POSTs
app.use(express.urlencoded({extended: false}));
app.use(express.json());

// serve static files
//app.use(express.static(path.join(__dirname, 'static')));

/////////////////////////////////////////////
// routes

app.get('/data', async (req, res) => {
    const data = await db.all('SELECT * FROM users');
	res.json(data);
});

/////////////////////////////////////////////
// start up server
 
app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));