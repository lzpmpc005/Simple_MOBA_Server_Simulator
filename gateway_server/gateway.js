// Gateway Server (port:2000)

const express = require('express');
const httpProxy = require('http-proxy');
const cors = require('cors');

const app = express();
const apiProxy = httpProxy.createProxyServer();

const DJANGO_SERVER = 'http://127.0.0.1:8000';
const AUTH_SERVER = 'http://127.0.0.1:4000';
const MAIN_SERVER = 'http://127.0.0.1:3000';

app.use(cors({
  origin: [
    'http://localhost:2000', 'http://localhost:3000', 'http://localhost:4000', 'http://localhost:8000'],
  methods: 'GET,POST,PUT,DELETE',
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use('/django', (req, res) => {
    apiProxy.web(req, res, { target: DJANGO_SERVER });
});
app.use('/auth', (req, res) => {
    apiProxy.web(req, res, { target: AUTH_SERVER });
});
app.use('/main', (req, res) => {
  apiProxy.web(req, res, { target: MAIN_SERVER });
});

const port = 2000;
app.listen(port, () => {
  console.log(`Authentication server is running on http://localhost:${port}`);
});

