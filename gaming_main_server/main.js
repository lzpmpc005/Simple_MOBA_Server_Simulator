// Main Server (port:3000)

const express = require('express');
const socketIO = require('socket.io');
const http = require('http');
const path = require('path');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

app.use(cors({
    origin: [
      'http://localhost:2000', 'http://localhost:3000', 'http://localhost:4000', 'http://localhost:8000'],
    methods: 'GET,POST,PUT,DELETE',
    allowedHeaders: ['Content-Type', 'Authorization']
  }));

let validKeys = {};
let playerList = {};

app.use(express.static(path.join(__dirname, 'client')));
app.use(express.json());

app.post('/authenticate', (req, res) => {
    const { username, key } = req.body;
    validKeys[username] = key;
    console.log('validKeys:', validKeys);
});


io.on('connection', (socket) => {
    console.log('New client connected');

    socket.on('authenticate', ({ username, key }) => {
        if (validKeys[username] === key) {
            socket.emit('authenticated', { success: true });
        } else {
            socket.emit('authenticated', { success: false, message: 'Invalid key' });
        }
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

const port = 3000;
server.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
