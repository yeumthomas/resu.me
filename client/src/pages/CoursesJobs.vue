<template>
	<div>
		<Navbar />
		<div class="container-fluid">
			<b-tabs content-class="mt-3" align="center">
				<b-tab title="Relevant Coursework" active>
					<CourseCard />
				</b-tab>
				<b-tab title="Related Jobs">
					<JobCard />
				</b-tab>
			</b-tabs>
		</div>
	</div>
</template>

<script>


import CourseCard from "../components/CourseCard"
import JobCard from "../components/JobCard"
import Navbar from "../components/Navbar"
export default {
	name: 'coursesjobs',
	components: {
        CourseCard,
		JobCard,
		Navbar
	}
}

</script>

<style scoped>

</style>