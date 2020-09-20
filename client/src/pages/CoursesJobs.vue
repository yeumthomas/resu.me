<template>
	<div class="container-fluid">
		<b-tabs content-class="mt-3" align="center">
			<b-tab title="Relevant Coursework" active>
				<div class="container justify-content-center">
					<b-spinner class="spinner" variant="primary" label="Loading Courses..." v-if="coursesLoading"></b-spinner>
					<div class="row" v-if="!coursesLoading">
						<div class="col-12 my-3" v-for="(course, index) in courses" :key="index">
							<CourseCard :course="course" />
						</div>
					</div>
				</div>
			</b-tab>
			<b-tab title="Related Jobs">
				<div class="container justify-content-center">
					<b-spinner class="spinner" variant="primary" label="Loading Jobs..." v-if="jobsLoading"></b-spinner>
					<div class="row" v-if="!jobsLoading">
						<div class="col-12 my-3" v-for="(job, index) in jobs" :key="index">
							<JobCard :job="job" />
						</div>
					</div>
				</div>
			</b-tab>
		</b-tabs>
	</div>
</template>

<script>
import axios from 'axios';

import CourseCard from "../components/CourseCard"
import JobCard from "../components/JobCard"
// import Navbar from "../components/Navbar"
export default {
	name: 'coursesjobs',
	components: {
		CourseCard,
		JobCard,
		// Navbar
	},
	data() {
		return {
			keyword: '',
			location: '',
			courses: [],
			jobs: [],
			coursesLoading: true,
			jobsLoading: true
		}
	},
	created() {
		console.log(this.$route.params)
		this.keyword = this.$route.params.keyword
		this.location = this.$route.params.location
		this.scrapeCourses()
		this.scrapeJobs()
	},
	methods: {
		scrapeCourses() {
			this.coursesLoading = true
			let formData = new FormData()
			formData.append('keyword', this.keyword)
			axios({
				method: 'post',
				url: 'http://127.0.0.1:5000/api/v1/scrapeCourses',
				data: formData
			}).then( (response) => {
				this.courses = this.mergeArrays(response.data.coursera, response.data.other)
				this.courses.sort(function(a, b) {
					if(a.rating == null) { return 1; }
					if(b.rating == null) { return 0; }
					return parseInt(a.rating.split('s')[0]) > parseInt(b.rating.split('s')[0])
				})
				console.log(this.courses)
				this.coursesLoading = false
			})
		},
		scrapeJobs() {
			this.jobsLoading = true
			let formData = new FormData()
			formData.append('keyword', this.keyword)
			formData.append('location', this.location)
			axios({
				method: 'post',
				url: 'http://127.0.0.1:5000/api/v1/scrapeJobs',
				data: formData
			}).then( (response) => {
				let aggregate = this.mergeArrays(response.data.monster, response.data.simplyhired)
				this.jobs = Array.from(new Set(aggregate.map(a => a.company.trim()))).map(company => { return aggregate.find(a => a.company === company) })
				console.log(this.jobs)
				this.jobsLoading = false
			})
		},
		mergeArrays(arr1, arr2) {
			let finalArr = []
			arr1.forEach( (value) => { finalArr.push(value) })
			arr2.forEach( (value) => { finalArr.push(value) })
			return finalArr
		}
	}
}

</script>

<style scoped>
.spinner {
	margin: 5rem;
}
</style>