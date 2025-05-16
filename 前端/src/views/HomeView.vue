<template>
  <el-container>
    <el-header style="width: 100%;height: 50px;background-color: #5E9AFD">
      <el-row>
        <el-col span="8">
          <h1></h1>
        </el-col>
        <el-col span="8">
          <h1 style="text-align: center;font-size: 36px;margin-top: -5px;color: chartreuse"> 美食菜谱可视化</h1>
        </el-col>
        <el-col span="8">
          <h2 style="text-align: right">
            {{ this.nowDateref }} {{ this.nowTimeref }} {{ this.nowWeekref }}
          </h2>
        </el-col>
      </el-row>

    </el-header>
    <el-container>
      <el-aside width="200px" style="height: auto ;background-color: #545c64">
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            background-color="#545c64"
            text-color="#fff"
            router
            active-text-color="#ffd04b">
          <el-menu-item index="/index">
            <i class="el-icon-menu"></i>
            <span slot="title">首页</span>
          </el-menu-item>
          <el-menu-item index="/list">
            <i class="el-icon-menu"></i>
            <span slot="title">菜谱数据列表</span>
          </el-menu-item>
          <el-menu-item index="/echarts">
            <i class="el-icon-document"></i>
            <span slot="title">类型分析可视化</span>
          </el-menu-item>
          <el-menu-item index="/echarts1">
            <i class="el-icon-document"></i>
            <span slot="title">配料分析可视化</span>
          </el-menu-item>
          <el-menu-item index="/echarts3">
            <i class="el-icon-document"></i>
            <span slot="title">收藏分析可视化</span>
          </el-menu-item>
          <el-menu-item index="/echarts4">
            <i class="el-icon-document"></i>
            <span slot="title">浏览分析可视化</span>
          </el-menu-item>
          <el-menu-item index="/echarts5">
            <i class="el-icon-setting"></i>
            <span slot="title">发布人配料分析</span>
          </el-menu-item>
          <el-menu-item index="/">
            <i class="el-icon-setting"></i>
            <a href="http://localhost:8000/admin" target="_blank">
              <span class="text fw-b" style="color: #fff">后台管理</span>
            </a>
          </el-menu-item>
          <el-menu-item index="/">
            <i class="el-icon-setting"></i>
            <span slot="title">退出登陆</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </el-container>


</template>

<script>
import axios from "axios";
import * as echarts from 'echarts'
import "@/components/echarts-wordcloud.min.js"
import router from "@/router/index.js";

export default {
  name: "index",
  data() {
    return {
      img: [],
      date: [],
      info: [],
      nowDateref: '',
      nowTimeref: '',
      nowWeekref: '',

    }
  },
  methods: {
    getDate1() {
      var _this = this;
      let yy = new Date().getFullYear();
      let mm = new Date().getMonth() + 1;
      let dd = new Date().getDate();
      let week = new Date().getDay();
      let hh = new Date().getHours();
      let ms =
          new Date().getSeconds() < 10 ?
              "0" + new Date().getSeconds() :
              new Date().getSeconds();
      let mf =
          new Date().getMinutes() < 10 ?
              "0" + new Date().getMinutes() :
              new Date().getMinutes();
      if (week == 1) {
        this.nowWeekref = "周一";
      } else if (week == 2) {
        this.nowWeekref = "周二";
      } else if (week == 3) {
        this.nowWeekref = "周三";
      } else if (week == 4) {
        this.nowWeekref = "周四";
      } else if (week == 5) {
        this.nowWeekref = "周五";
      } else if (week == 6) {
        this.nowWeekref = "周六";
      } else {
        this.nowWeekref = "周日";
      }
      this.nowTimeref = hh + "点" + mf + "分" + ms + "秒";
      //ms是秒，这里可以根据自己需要调整格式
      // nowTimeref.value = hh + "点" + mf+"分";
      this.nowDateref = yy + "年" + mm + "月" + dd + "日";
      // nowDateref.value = yy + "-" + mm + "-" + dd;
    }
  },
  mounted() {
    setInterval(this.getDate1, 500);
    // this.getDate1()
    setTimeout(() => {
      this.$refs.box.initWH()
    }, 1)


  }

}
</script>
<style lang="less">

.el-header {
  margin: 0;
  padding: 0;
}

.el-container {
  min-height: 100vh;
}

.box {
  height: 100%;
}

.head {
  height: 80px !important;
  width: 100%;
}

.el-main {
  height: calc(100% - 100px) !important;
}
</style>
