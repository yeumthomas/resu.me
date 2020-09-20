<template>
	<div id="skills">
		<h1 class = Title>Skills</h1>
		<Skill />
	</div>
</template>

<script>

import Skill from "../components/Skill"
export default {
	name: 'skills',
	components: {
		Skill
	}
}
</script>

<style scoped>
Title{
	font-size: 60px;
}
</style>