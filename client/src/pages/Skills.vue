<template>
	<div id="skills">
		<div class = Title>Learn Skills</div>
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
.Title{
	font-size: 50px;
	display: flex;
    justify-content: center;
	font-weight: bold;
}
</style>