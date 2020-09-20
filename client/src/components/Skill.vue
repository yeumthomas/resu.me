<template>
    <div class="container">
        <div class="row">
            <div class="col-4">
                <div class="ybox">
                    Skill 1
                </div>
            </div>
            <div class="col-4">
                <div class="bbox">
                    Skill 2
                </div>
            </div>
            <div class="col-4">
                <div class="ybox">
                    Skill 3
                </div>
            </div>
            <div class="col-4">
                <div class="bbox">
                    Skill 4
                </div>
            </div>
            <div class="col-4">
                <div class="ybox">
                    Skill 5
                </div>
            </div>
            <div class="col-4">
                <div class="bbox">
                    Skill 6
                </div>
        <h3 class="title">Text fadeIn top</h3>
        <div class="content">
            <div class="content-overlay"></div>
            <img class="content-image" src="../assets/img/logo-bee.png">
            <div class="content-details fadeIn-top">
                <h3>This is a title</h3>
                <p>This is a short description</p>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Skill',
}
</script>

<style scoped>
.container{
    width: 100%;
    padding: 10px;
    margin: auto;
    background: #ffffff;
    display: flex;
    flex-direction: row;
}

.ybox{
    width: 250px;
    height: 250px;
    margin: 40px 40px;
    background: #ffb101;
    transition: 1s;
    color: #2a2a2a;
    font-weight: bold;
    font-size: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.bbox{
    width: 250px;
    height: 250px;
    margin: 40px 40px;
    background: #2a2a2a;
    transition: 1s; 
    color: #ffb101;
    font-weight: bold;
    font-size: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.ybox:hover{
    transform: scale(1.3);
    background: #ffb101;
    z-index: 2;
    box-shadow: 2px 2px 2px #2a2a2a;
}

.bbox:hover{
    transform: scale(1.3);
    background: #2a2a2a;
    z-index: 2;
    box-shadow: 2px 2px 2px #ffb101;
}


</style>