<template>
	<div id="skills">
		<div class="title my-5"> Pick a skill/interest to explore! </div>
		<div class="container">
			<div class="row">
				<div class="col-4" v-for="(interest, index) in interests" :key="index">
					<Skill :name="interest" :color="setColor(index)" @clicked="findCoursesJobs" />
				</div>
			</div>
		</div>
		</div>
</template>

<script>
import axios from 'axios';

import Skill from "../components/Skill"
export default {
	components: {
		Skill
	},
	data() {
		return {
			interests: [],
			location: ''
		}
	},
	created() {
		this.getInterests()
	},
	methods: {
		getInterests() {
			axios({
				method: 'get',
				url: 'http://localhost:3000/api/v1/auth/me',
				headers: {
					'Authorization': 'Bearer ' + this.$cookies.get('token')
				}
			}).then( (response) => {
				this.interests = response.data.interests
				this.location = response.data.location
				console.log(this.interests)
			}).catch( (err) => {
				console.log(err)
			})
		},
		setColor(number) {
			return number % 2 == 0 ? 'ybox' : 'bbox'
		},
		findCoursesJobs(keyword) {
			this.$router.push({ name: 'results', params: { keyword: keyword, location: this.location } })
		}
	}
}
</script>

<style scoped>
.title {
	font-size: 3rem;
	font-weight: bold;
}
</style>