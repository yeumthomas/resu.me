const config = require('../../config')
const jwt = require('jsonwebtoken')

const { User } = require('../models')

const generateToken = async (email) => {
  const user = await User.findOne({ email: email })
  const token = jwt.sign({
    name: user.name,
    email: user.email,
    classes: user.classes
  }, config.auth.secret, {
    expiresIn: '1h'
  })
  return token
}

/**
 * Express middleware function for validating JWT
 * 
 * @param {object} req Request object
 * @param {object} res Result object
 * @param {object} next Next callback in event loop
 */
const validateToken = (req, res, next) => {
  if(req.headers.authorization) {
    const token = req.headers.authorization.split(' ')[1]
    jwt.verify(token, config.auth.secret, (err, decoded) => {
      if(err) res.status(401).json({ error: 'Invalid Token' })
      return next()
    })
  } else {
    res.status(401).json({ error: 'Token Not Found' })
  }
}

const decodeToken = (token) => {
  const decoded = jwt.verify(token, config.auth.secret)
  return decoded
}

module.exports = {
  generate: generateToken,
  validate: validateToken,
  decode: decodeToken
}