<template>
    <div class="card" style="width: 20rem;">
        <img src="../assets/img/logo-bee.png" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Course 1</h5>
            <p class="card-text">Where the course is from, short description.</p>
            <a href="https://www.coursera.org/" target="_blank" class="btn btn-primary">Link to external website</a>
        </div>
</div>
</template>

<script>
export default {
    name: 'CourseCard',
}
</script>

<style scoped>
.card{
    color: #2a2a2a;
    border-color: #a2dce7;
    border-width: 0.3cm;
}

.btn{
    background: #ffb101;
    color: #2a2a2a;
    border-color: #ffb101;
}
</style>