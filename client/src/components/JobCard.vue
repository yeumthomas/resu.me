<template>
  <b-card no-body class="overflow-hidden">
    <b-row no-gutters>
      <b-col md="12">
        <b-card-body>
          <button class="bookmark" v-on:click="closeOverlay"><i class="far fa-bookmark"></i></button>
          <b-card-text class="card-body">
            <small class="text-muted">{{job.location.trim()}}</small>
            <h3 class="font-weight-bold">{{job.name.trim()}}</h3>
            <h4>{{job.company.trim()}}</h4>
            <div class="d-flex justify-content-start align-items-center">
              <button class="btn mt-2 mr-2"><a :href="job.link">See Details</a></button>
            </div>
          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
export default {
  name: 'JobCard',
  props: [ 'job' ]
}
</script>

<style scoped>
.bookmark {
  position: absolute;
  top: 0;
  right: 0;
}

.card {
  color: #2a2a2a;
  border-color: #ffb101;
  border-width: 0.3cm;
}

.card-body {
  text-align: left;
}

.btn {
  background: #a2dce7;
  color: #2a2a2a;
  border-color: #a2dce7;
  padding: 0.5rem 1.5rem;
  border-radius: .5rem;
}

.btn:hover {
  background: var(--BTNcolor-dark, #ffb101);
  color: var(--BTNcolor-text, #2a2a2a);
  border-color: #ffb101;
}

</style>