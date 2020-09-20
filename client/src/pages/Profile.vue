<template>
  <div class="container-fluid">
    <h1 class="font-weight-bold"> Profile </h1>
    <div class="row justify-content-center mt-4">
      <div class="col-2 bio">
        <img src="../assets/img/placeholder.jpg" class="img-fluid">
      </div>
      <div class="col-2 bio d-flex align-items-center">
        <div class="">
          <div class="form-group">
            <input type="text" class="form-control my-2" :value="user.name" disabled />
          </div>
          <div class="form-group">
            <input type="text" class="form-control my-2" :value="user.email" disabled />
          </div>
          <div class="form-group">
            <input type="text" class="form-control my-2" :value="user.location" disabled />
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-5">
      <div class="col-2"></div>
      <div class="col-4">
        <h4> Interests </h4>
        <div class="row">
          <div class="col-12" v-for="(interest, index) in user.interests" :key="index">
            <Skill :name="interest" :color="setColor(index)" />
          </div>
        </div>
      </div>
      <div class="col-4">
        <h4> Skills </h4>
        <div class="row">
          <div class="col-12" v-for="(skill, index) in user.skills" :key="index">
            <Skill :name="skill" :color="setColor(index+1)" />
          </div>
        </div>
      </div>
      <div class="col-2"></div>
      <div class="col-6 mt-5">
        <h4> Classes </h4>
        <div class="row">
          <div class="col-12 my-3" v-for="(course, index) in user.classes" :key="index">
            <CourseCard :course="course" :bookmark="false" :remove="true" @destroy="removeCourse(course)" />
          </div>
        </div>
      </div>
      <div class="col-6 mt-5">
        <h4> Jobs </h4>
        <div class="row">
          <div class="col-12 my-3" v-for="(job, index) in user.jobs" :key="index">
            <JobCard :job="job" :bookmark="false" :remove="true" @destroy="removeJob(job)" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import Skill from '../components/Skill'
import CourseCard from '../components/CourseCard'
import JobCard from '../components/JobCard'

export default {
  components: { Skill, CourseCard, JobCard },
  data() {
    return {
      user: {}
    }
  },
  created() {
    this.getUserInformation()
  },
  methods: {
    getUserInformation() {
      axios({
        method: 'get',
        url: 'http://localhost:3000/api/v1/auth/me',
        headers: {
          'Authorization': 'Bearer ' + this.$cookies.get('token')
        }
      }).then( (response) => {
        this.user = response.data
      })
    },
    setColor(number) {
			return number % 2 == 0 ? 'ybox' : 'bbox'
    },
    removeCourse(course) {
      axios({
        method: 'delete',
        url: 'http://localhost:3000/api/v1/users/courses',
        headers: {
          'Authorization': 'Bearer ' + this.$cookies.get('token')
        },
        data: course
      }).then( () => {
        console.log('axios done')
        this.getUserInformation()
      })
    },
    removeJob(job) {
      axios({
        method: 'delete',
        url: 'http://localhost:3000/api/v1/users/jobs',
        headers: {
          'Authorization': 'Bearer ' + this.$cookies.get('token')
        },
        data: job
      }).then( () => {
        this.getUserInformation()
      })
    }
  }
}
</script>

<style scoped>
.bio {
  padding: 2rem 2rem;
  background-color: #fafafa;
}
</style>