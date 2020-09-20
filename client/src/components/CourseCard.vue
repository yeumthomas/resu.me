<template>
  <b-card no-body class="overflow-hidden">
    <b-row no-gutters>
      <b-col md="2">
        <b-card-img :src="course.img" class="h-100"></b-card-img>
      </b-col>
      <b-col md="10">
        <b-card-body :title="course.name.trim()">
          <b-card-text class="card-body">
            <div class="row">
              <div class="col">
                <button class="btn"><a :href="course.link">Go To</a></button>
              </div>
            </div>
          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
export default {
  name: 'CourseCard',
  props: [ 'course' ]
}
</script>

<style scoped>
a {
  text-decoration: none;
  color: #2a2a2a;
}

.card-body {
  text-align: left;
}

.card{
  color: #2a2a2a;
  border-color: #a2dce7;
  border-width: 0.3cm;
}

.btn{
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