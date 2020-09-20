const { User } = require('../models')

const addOnboardInfo = async (data) => {
  let user = await User.findOne({ email: data.email })
  user.interests = []
  user.skills = []
  
  data.interests.forEach( (interest) => { user.interests.push(interest.trim()) })
  data.skills.forEach( (skill) => { user.skills.push(skill.trim()) })
  user.location = data.location
  return user.save()
}

module.exports = {
  addOnboardInfo: addOnboardInfo
}