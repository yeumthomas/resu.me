<template>
  <div id="navbar" margin-top="0px" width-min="100%" clear="left" display="inline-block" height="40px">
    <header margin-top="0px">
      <aside margin-top="0px">
        <el-row>
          <el-col :span="10">
            <img src="../assets/img/logo-paper.png" alt="logo" class="logo">
          </el-col>
          <el-col :span="10">
          </el-col>
          <el-col :span="4">
            <el-button round type="circle" src="button" class="logbutton" v-on:click="nukeCookies">Log Out</el-button>
          </el-col>
        </el-row>
      </aside>
    </header>
  </div>
</template>
    
<script>
export default {
}
</script>
    
<style scoped>
.navbar {
  margin-top:0px;
}
.logo {
  height: 80px;
  width: 130px;
  position: left;
  float:left;
  margin-top: -40px;
  margin-left: 10px;
}
.logbutton {
  background-color: #C998C3;
  color: #ffffff;
  font-family: 'Kumbh Sans', sans-serif;
  text-align: center;
  font-size: 20px;
  width: 150px;
  height: 50px;
  margin-right: 50px;
  margin-top: -30px;
}
.logbutton:hover {
   background-color: #E4CEE0;
   color: #C998C3;
   
}
</style>