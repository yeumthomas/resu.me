const http = require('http')
const express = require('express')
const bodyParser = require('body-parser')
const moment = require('moment')
const mongoose = require('mongoose')

const routes = require('../src/controllers')

moment().format()

const run = (port, dbUri) => {
  // Initialize web server object
  const app = express()
  const server = http.createServer(app)

  // Setup request handling
  app.use(bodyParser.json())
  app.use('/api/v1', routes)

  // Listen to DB and HTTP
  mongoose.connect(dbUri, { useNewUrlParser: true, useUnifiedTopology: true })
  mongoose.connection.on('error', (err) => { console.log('Could not connect to MongoDB'); console.log(err); process.exit(1); })
  server.listen(port, () => {
    console.log('Listening on http://localhost:' + port)
  })
}

module.exports = run