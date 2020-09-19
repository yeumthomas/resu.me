const mongoose = require('mongoose')
const bcrypt = require('bcryptjs')
const Joi = require('joi')

const schema = new mongoose.Schema({
  name: { type: String, required: 'Name Invalid' },
  password: { type: String },
  email: { type: String, unique: true, lowercase: true, required: 'Email Invalid' },
  classes: { type: [{
    title: { type: String },
    description: { type: String },
    difficulty: { type: String },
    rating: { type: String },
    image: { type: String },
    href: { type: String }
  }], default: [] }
})

schema.pre('save', function (next) {
  let person = this
  if(!person.isModified('password')) return next()
  bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(person.password, salt, (err, hash) => {
      person.password = hash
      return next()
    })
  })
})

schema.methods.comparePassword = function (password) {
  let person = this
  return bcrypt.compare(password, person.password)
}

schema.statics.validateModel = (model) => {
  const joiSchema = Joi.object({
    email: Joi.string().required(),
    name: Joi.string().required(),
    password: Joi.string().required(),
    classes: Joi.array().required()
  })
  console.log(model)
  return joiSchema.validate(model)
}

module.exports = mongoose.model('User', schema)