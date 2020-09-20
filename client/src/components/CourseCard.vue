<template>
  <b-card no-body class="overflow-hidden">
    <b-row no-gutters>
      <b-col md="2">
        <b-card-img :src="course.img" class="h-100"></b-card-img>
      </b-col>
      <b-col md="10">
        <b-card-body>
          <button ref="bookmark" class="bookmark" v-if="bookmark" v-on:click="bookmarkCourse"><i class="far fa-bookmark"></i></button>
          <b-card-text class="card-body">
            <small class="text-muted">{{course.provider}} on {{course.platform}}</small>
            <h4 class="font-weight-bold">{{course.name}}</h4>
            <div class="d-flex justify-content-start align-items-center">
              <button class="btn mt-2 mr-2">See Details</button>
              <button class="btn mt-2 mr-2"><a :href="course.link">Go To {{course.platform}}</a></button>
              <span class="ml-2 mt-2 kufam" v-if="course.rating"> {{course.rating.split('s')[0]}}/5 stars </span>
            </div>
          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CourseCard',
  props: [ 'course', 'bookmark' ],
  methods: {
    bookmarkCourse() {
      axios({
        method: 'post',
        url: 'http://localhost:3000/api/v1/users/courses',
        headers: {
          'Authorization': 'Bearer ' + this.$cookies.get('token')
        },
        data: this.course
      }).then( (response) => {
        console.log(response.data)
        this.$refs['bookmark'].style.backgroundColor = '#a2dce7'
      })
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');

.bookmark {
  position: absolute;
  top: 0;
  right: 0;
  border-radius: 4px;
}

.kufam {
  font-size: 1.2rem;
  font-family: 'Roboto', sans-serif;
}

a {
  text-decoration: none;
  color: #2a2a2a;
  font-weight: bold;
}

.card-body {
  text-align: left;
}

.card{
  color: #2a2a2a;
  border-color: #a2dce7;
  border-width: 0.3cm;
}

.btn {
  background: #ffb101;
  color: #2a2a2a;
  border-color: #ffb101;
  padding: 0.5rem 1.5rem;
  border-radius: .5rem;
}

.btn:hover {
  background: var(--BTNcolor-dark, #a2dce7);
  color: var(--BTNcolor-text, #2a2a2a);
  border-color: #a2dce7;
}

</style>