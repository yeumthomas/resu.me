<template>
    <div class="card" style="width: 20rem;">
        <img src="../assets/img/logo-bee.png" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Job 1</h5>
            <p class="card-text">Where the job is from, short description.</p>
            <a href="https://www.monster.com/" target="_blank" class="btn btn-primary">Link to external website</a>
        </div>
</div>
</template>

<script>
export default {
    name: 'JobCard',
}
</script>

<style scoped>
.card{
    color: #2a2a2a;
    border-color: #ffb101;
    border-width: 0.3cm;
    
}

.btn{
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