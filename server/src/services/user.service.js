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

const addFavoriteCourse = async (email, course) => {
  let user = await User.findOne({ email: email })
  Object.keys(course).map(k => course[k] = course[k].trim())
  user.classes.push(course)
  return user.save()
}

const addFavoriteJob = async (email, job) => {
  let user = await User.findOne({ email: email })
  Object.keys(job).map(k => job[k] = job[k].trim())
  user.jobs.push(job)
  return user.save()
}

const removeCourse = async (email, course) => {
  return User.findOneAndUpdate({ email: email }, { $pull: { classes: { name: course.name } } })
}

const removeJob = async (email, job) => {
  return User.findOneAndUpdate({ email: email }, { $pull: { jobs: { name: job.name } } })
}

module.exports = {
  addOnboardInfo: addOnboardInfo,
  addFavoriteCourse: addFavoriteCourse,
  addFavoriteJob: addFavoriteJob,
  removeCourse: removeCourse,
  removeJob: removeJob
}