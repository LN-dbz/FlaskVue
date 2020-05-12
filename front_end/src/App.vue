<template>
  <div id="app">
    <el-container id="container">
      <el-header height="50px" id="container-header">
        <a href="index2.html" class="logo" v-bind:style="{ width: isCollapse ? '65px': '200px'}">
          <!-- mini logo for sidebar mini 50x50 pixels -->
          <span class="logo-mini" v-if="isCollapse  === true">
            <b>A</b>LT
          </span>
          <!-- logo for regular state and mobile devices -->
          <span class="logo-lg" v-if="isCollapse  === false">
            <b>Admin</b>LTE
          </span>
        </a>
        <div style="color:#ffffff; font-size:20px; margin-left:5px;float:left">
          <i class="el-icon-s-fold" @click="isCollapse = true" v-if="isCollapse  === false"></i>
          <i class="el-icon-s-unfold" @click="isCollapse = false" v-if="isCollapse === true"></i>
        </div>

        <div class="header-right">
          <div class="div-inline">
            <el-badge :value="12" class="item">
              <i class="el-icon-bell"></i>
            </el-badge>
          </div>
          <div class="div-inline">
            <el-badge :value="12" class="item">
              <i class="el-icon-chat-dot-round"></i>
            </el-badge>
          </div>
          <div class="div-inline">
            <el-badge :value="12" class="item">
              <i class="el-icon-chat-dot-round"></i>
            </el-badge>
          </div>
          <el-avatar size="large" :src="circleUrl" class="div-inline" style="margin-left:15px"></el-avatar>
          <div class="div-inline" style="margin-right:20px;">
            <span>管理者xx</span>
          </div>
        </div>
      </el-header>

      <el-container>
        <el-menu
          @open="handleOpen"
          @close="handleClose"
          default-active="1-4-1"
          class="el-menu-vertical-demo"
          background-color="#222d32"
          text-color="#ffffff"
          :collapse="isCollapse"
          :collapse-transition="false"
          :style="{width: isCollapse ? '65px':'200px'}"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span slot="title">导航一</span>
            </template>
            <el-menu-item-group>
              <span slot="title">分组一</span>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <span slot="title">选项4</span>
              <el-menu-item index="1-4-1">选项1</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">导航二</span>
          </el-menu-item>
          <el-menu-item index="3" disabled>
            <i class="el-icon-document"></i>
            <span slot="title">导航三</span>
          </el-menu-item>
          <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">导航四</span>
          </el-menu-item>
        </el-menu>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      isCollapse: false,
      menu_width: "200px"
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      this.menu_width = "65px";
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      this.menu_width = "200px";
      console.log(key, keyPath);
    }
  }
};
</script>

<style>
body {
  margin: 0;
}
a {
  text-decoration: none;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#container {
  height: 100%;
  position: absolute;
  left: 0;
  right: 0;
}

#container-header {
  padding: 0;
  background-color: #3c8dbc;
  line-height: 50px;
}
.logo {
  width: 200px;
  border-bottom: none;
  display: block;
  float: left;
  background-color: #367fa9;
  font-weight: 700;
  color: #ffffff;
  text-align: center;
  font-size: 24px;
}
.sidebar {
  background-color: #222d32;
}
.header-right {
  float: right;
  color: #ffffff;
}

.header-right .el-badge {
  margin-right: 10px;
  height: 25px;
  line-height: 25px;
}
.header-right > .div-inline > .el-badge > i {
  font-size: 20px;
}
.header-right sup {
  height: 10px;
  line-height: 10px;

  font-size: 1px;
  padding: 0 2px;
}
.div-inline {
  display: inline-block;
  vertical-align: middle;
}
</style>

