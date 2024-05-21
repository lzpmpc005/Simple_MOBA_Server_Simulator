// Authentification Server (port:4000)

const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const crypto = require('crypto');
const axios = require('axios');
const app = express();

const cors = require('cors');

app.use(cors({
  origin: [
    'http://localhost:2000', 'http://localhost:3000', 'http://localhost:4000', 'http://localhost:8000'],
  methods: 'GET,POST,PUT,DELETE',
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(bodyParser.json());

const pool = mysql.createPool({
    connectionLimit: 10,
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: 'hellomysql',
    database: 'Moba_Simulator'
  });

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    console.log('Authentication request:', username);
    
    pool.query('SELECT * FROM player_profile_player WHERE account = ? AND password = ?', [username, password], (error, results) => {
        if (error) {
          console.error('Database query error:', error);
          res.status(500).json({ success: false, message: 'Database error' });
        } else {
          if (results.length > 0) {
            const key = crypto.randomBytes(16).toString('hex');
            console.log('Key generated:', key);
            res.json({ success: true, key });
            axios.post('http://localhost:3000/authenticate', { username, key })
                    .then(response => {
                        console.log('Sent username and key to main server:', response.data);
                    })
                    .catch(error => {
                        console.error('Error sending to main server:', error);
                    });

          } else {
            res.status(401).json({ success: false, message: 'Invalid username or password' });
          }
        }
      });
});

const port = 4000;
app.listen(port, () => {
  console.log(`Authentication server is running on http://localhost:${port}`);
});