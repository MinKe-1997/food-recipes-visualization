<template>
    <div class="ooooo" style="height: 1111px;">
        <div class="main-box" style="margin-top: 100px">
            <h2 style="font-size: 70px;text-align: center !important; color: #5E9AFD">
                美食
            </h2>
        </div>
        <el-row>
            <el-col span="10">
                <h1 style="text-align: right;margin-top: -5px;margin-right: 20px">账号</h1>
            </el-col>
            <el-col span="4">
                <el-input style="align-items: center"  v-model="info.name">

                </el-input>
            </el-col>
        </el-row>
        <el-row style="margin-top: 20px" >
            <el-col span="10" >
                <h1 style="text-align: right;margin-top: -5px;margin-right: 20px">密码</h1>
            </el-col>
            <el-col span="4">
                <el-input style="align-items: center"
                        type="password"  v-model="info.password">

                </el-input>
            </el-col>
        </el-row>
        <el-col align="center" >
            <el-button style="width: 100px; margin-bottom: 10px" size="small" type="primary"
                     @click="login" >登录
            </el-button>
            <el-button style="width: 100px; margin-bottom: 10px" size="small" type="primary"
               @click="zc">注册
            </el-button>
        </el-col>
    </div>

</template>
<script>
    import axios from "axios";
    import { Message } from 'element-ui';
    import router from "@/router/index.js";
    export default {
        data(){
            return{
                info: {
                    name: 'admin',
                    password: "admin",
                },
            }
        },
        methods:{
            login(){
            axios.post("api/login/",this.info).then(res=>{
                if (res.data.login==1){
                    Message({
                        message: '登陆成功',
                        type: 'success'
                    });
                    router.push("/index")
                }else {
                    Message({
                        message: '密码错误',
                        type: 'error'
                    });
                }
            })
            },
            zc(){
                axios.post("api/zc/",this.info).then(res=>{
                    if (res.data.login==1){
                        Message({
                            message: '注册成功',
                            type: 'success'
                        });
                    }else {
                        Message({
                            message: '注册错误',
                            type: 'error'
                        });
                    }
                })
            }
        },
        mounted() {

        }
    }
</script>

<style lang="less">
  .ooooo {
    min-width: 1200px;
    max-width: 3200px;
    height: 100%;
    margin: 0 auto;
    padding: .125rem .125rem 0;
    background-image: url(../assets/img.png);
    //?border:1px solid red;

    .main-box {
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;

    }
  }
</style>
