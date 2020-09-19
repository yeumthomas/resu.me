const express = require('express')
const jwt = require('../utils/jwt')
const { auth } = require('../services')

const router = express.Router()

router.post('/login', async (req, res) => {
  try {
    let user = await auth.login(req.body.email, req.body.password)
    res.status(200).json(user)
  } catch (err) {
    console.log(err)
    res.status(400).json({ error: err.message })
  }
})

router.post('/signup', async (req, res) => {
  try {
    let newser = await auth.signup(req.body)
    let user = await auth.login(newser.email, req.body.password)
    res.status(201).json(user)
  } catch (err) {
    console.log(err)
    res.status(400).json({ error: err.message })
  }
})

router.get('/me', jwt.validate, async (req, res) => {
  try {
    let user = await auth.me(req.headers.authorization.split(' ')[1])
    res.status(200).json(user)
  } catch (err) {
    console.log(err)
    res.status(400).json({ error: err.message })
  }
})

module.exports = router