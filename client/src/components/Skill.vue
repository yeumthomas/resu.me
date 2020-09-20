<template>
  <div :class="color" v-on:click="emitClick">
    {{ name.toLowerCase() }}
  </div>
</template>

<script>

export default {
  name: 'Skill',
  props: [ 'name', 'color' ],
  methods: {
    emitClick() {
      this.$emit('clicked', this.name)
    }
  }
}
</script>

<style scoped>
.ybox,
.bbox {
  height: 5rem;
  padding: 1rem 4rem;
  margin: 1rem 2rem;
  transition: 1s;
  color: #2a2a2a;
  font-weight: bold;
  font-size: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 1rem;
}

.ybox {
  background-color: #ffb101;
}

.bbox {
  background-color: #a2dce7;
}

.ybox:hover,
.bbox:hover {
  transform: scale(1.1);
}


</style>