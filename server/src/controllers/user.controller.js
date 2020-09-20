const express = require('express')
const jwt = require('../utils/jwt')
const { user } = require('../services')

const router = express.Router()

router.post('/onboard', jwt.validate, async (req, res) => {
  try {
    let data = {
      email: jwt.decode(req.headers.authorization.split(' ')[1]).email,
      ...req.body
    }
    let update = await user.addOnboardInfo(data)
    res.status(200).json(update)
  } catch (err) {
    res.status(400).json(err.message)
  }
})

router.post('/courses', jwt.validate, async (req, res) => {
  try {
    let email = jwt.decode(req.headers.authorization.split(' ')[1]).email
    let update = await user.addFavoriteCourse(email, req.body)
    res.status(200).json(update)
  } catch (err) {
    res.status(400).json(err.message)
  }
})

router.delete('/courses', jwt.validate, async (req, res) => {
  try {
    let email = jwt.decode(req.headers.authorization.split(' ')[1]).email
    let update = await user.removeCourse(email, req.body)
    res.status(200).json(update)
  } catch (err) {
    res.status(400).json(err.message)
  }
})

router.post('/jobs', jwt.validate, async (req, res) => {
  try {
    let email = jwt.decode(req.headers.authorization.split(' ')[1]).email
    let update = await user.addFavoriteJob(email, req.body)
    res.status(200).json(update)
  } catch (err) {
    res.status(400).json(err.message)
  }
})

router.delete('/jobs', jwt.validate, async (req, res) => {
  try {
    let email = jwt.decode(req.headers.authorization.split(' ')[1]).email
    let update = await user.removeJob(email, req.body)
    console.log(update)
    res.status(200).json(update)
  } catch (err) {
    res.status(400).json(err.message)
  }
})

module.exports = router