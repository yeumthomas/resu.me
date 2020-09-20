const mongoose = require('mongoose')
const bcrypt = require('bcryptjs')
const Joi = require('joi')

const schema = new mongoose.Schema({
  name: { type: String, required: 'Name Invalid' },
  password: { type: String },
  email: { type: String, unique: true, lowercase: true, required: 'Email Invalid' },
  location: { type: String },
  interests: { type: [String] },
  skills: { type: [ String ] },
  classes: { type: [{
    name: { type: String },
    desc: { type: String },
    lang: { type: String },
    rating: { type: String },
    img: { type: String },
    link: { type: String },
    platform: { type: String },
    provider: { type: String }
  }], default: [] },
  jobs: { type: [{
    name: { type: String },
    company: { type: String },
    location: { type: String },
    link: { type: String }
  }]}
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
    location: Joi.string().required(),
    interests: Joi.array().required(),
    skills: Joi.array().required(),
    classes: Joi.array().required(),
    jobs: Joi.array().required()
  })
  console.log(model)
  return joiSchema.validate(model)
}

module.exports = mongoose.model('User', schema)