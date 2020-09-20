const jwt = require('../utils/jwt')
const { User } = require('../models')

const login = async (email, password) => {
  const user = await User.findOne({ email: email })
  if(!user) throw new Error('User Not Found')

  let authorized = await user.comparePassword(password)
  if(authorized) {
    const token = await jwt.generate(email)
    return {
      token: token
    }
  } else { throw new Error('Incorrect Password') }
}

const signup = async (data) => {
  const { value } = await User.validateModel(data)
  if(!value) throw new Error('Invalid Model')

  const existing = await User.findOne({ email: value.email })
  if(existing) throw new Error('User Already Exists')
  
  const user = new User(value)
  return user.save()
}

const me = async (token) => {
  const decoded = jwt.decode(token)

  const user = await User.findOne({ email: decoded.email })
  return user
}

module.exports = {
  login: login,
  signup: signup,
  me: me
}