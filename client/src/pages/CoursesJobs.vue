<template>
    <div>
    <b-card no-body>
        <b-tabs card>
        <b-tab title="Tab 1" active>
            <b-card-text><CourseCard /></b-card-text>
        </b-tab>
        <b-tab title="Tab 2">
            <b-card-text><JobCard /></b-card-text>
        </b-tab>
        </b-tabs>
    </b-card>
    </div>

</template>

<script>


import CourseCard from "../components/CourseCard"
import JobCard from "../components/JobCard"
export default {
	name: 'coursesjobs',
	components: {
        CourseCard,
        JobCard
	}
}

</script>