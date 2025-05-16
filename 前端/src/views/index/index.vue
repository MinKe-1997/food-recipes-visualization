<template>
    <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
        <el-tab-pane label="菜式" name="first">
            <div class="tag-group" style="margin-top: 10px">
                <span class="tag-group__title">菜式</span>
                <el-tag style="margin-left: 20px"
                        v-for="item in items"
                        :key="item.label"
                        :type="item.type"
                        effect="dark">
                    {{ item.label }}
                </el-tag>
            </div>
            <div style="width: 100%;height: 600px; margin-top: 50px">
                <dv-border-box-7 ref="box">
                    <el-carousel :interval="4000" type="card"
                                 height="500px" style="width: 90%; margin-left: 100px">
                        <el-carousel-item v-for="(item,index) in img" :key="index">
                            <el-image
                                    style="width: 100%; height: 100%;align-content: center"
                                    :src="item.img"></el-image>
                        </el-carousel-item>
                    </el-carousel>
                </dv-border-box-7>
            </div>
        </el-tab-pane>
        <el-tab-pane label="中国菜" name="second">
            <div class="tag-group" style="margin-top: 10px">
                <span class="tag-group__title">中国菜</span>
                <el-tag style="margin-left: 20px"
                        v-for="item in items"
                        :key="item.label"
                        :type="item.type"
                        effect="dark">
                    {{ item.label }}
                </el-tag>
            </div>
            <div style="width: 100%;height: 600px; margin-top: 50px">
                <dv-border-box-7 ref="box">
                    <el-carousel :interval="4000" type="card"
                                 height="500px" style="width: 90%; margin-left: 100px">
                        <el-carousel-item v-for="(item,index) in img" :key="index">
                            <el-image
                                    style="width: 100%; height: 100%;align-content: center"
                                    :src="item.img"></el-image>
                        </el-carousel-item>
                    </el-carousel>
                </dv-border-box-7>
            </div>
        </el-tab-pane>
        <el-tab-pane label="外国菜" name="third">
            <div class="tag-group" style="margin-top: 10px">
                <span class="tag-group__title">外国菜</span>
                <el-tag style="margin-left: 20px"
                        v-for="item in items"
                        :key="item.label"
                        :type="item.type"
                        effect="dark">
                    {{ item.label }}
                </el-tag>
            </div>
            <div style="width: 100%;height: 600px; margin-top: 50px">
                <dv-border-box-7 ref="box">
                    <el-carousel :interval="4000" type="card"
                                 height="500px" style="width: 90%; margin-left: 100px">
                        <el-carousel-item v-for="(item,index) in img" :key="index">
                            <el-image
                                    style="width: 100%; height: 100%;align-content: center"
                                    :src="item.img"></el-image>
                        </el-carousel-item>
                    </el-carousel>
                </dv-border-box-7>
            </div>
        </el-tab-pane>
        <el-tab-pane label="各地小吃" name="fourth">
            <div class="tag-group" style="margin-top: 10px">
                <span class="tag-group__title">各地小吃</span>
                <el-tag style="margin-left: 20px;margin-top: 10px"
                        v-for="item in items"
                        :key="item.label"
                        :type="item.type"
                        effect="dark">
                    {{ item.label }}
                </el-tag>
            </div>
            <div style="width: 100%;height: 600px; margin-top: 50px">
                <dv-border-box-7 ref="box">
                    <el-carousel :interval="4000" type="card"
                                 height="500px" style="width: 90%; margin-left: 100px">
                        <el-carousel-item v-for="(item,index) in img" :key="index">
                            <el-image
                                    style="width: 100%; height: 100%;align-content: center"
                                    :src="item.img"></el-image>
                        </el-carousel-item>
                    </el-carousel>
                </dv-border-box-7>
            </div>
        </el-tab-pane>
    </el-tabs>
</template>
<script>
    import axios from "axios";

    export default {
        data() {
            return {
                activeName: 'first',
                info: {
                    type: "菜式",
                },
                img: [],
                items: [
                    {label: '标签一'},
                    {label: '标签二'},
                    {type: 'info', label: '标签三'},
                    {type: 'danger', label: '标签四'},
                    {type: 'warning', label: '标签五'}
                ]
            };
        },
        mounted() {
            this.data()
        },
        methods: {
            one() {
                this.info.type = "菜式"
                this.data()
            },
            one1() {
                console.log(111111111111111111111)
                this.info.type = "中国菜"

                this.data()
            },
            one2() {
                this.info.type = "中国菜"
            },
            one3() {
                this.info.type = "中国菜"
            },
            data() {
                axios.post('api/index/', this.info).then(res => {
                    this.img = res.data.img
                    console.log(this.img)
                    this.items = res.data.items
                })
            },
            handleClick(tab, event) {
                console.info(tab.index)
                switch (tab.index) {
                    case "0":
                        this.info.type = "菜式";
                        break;
                    case "1":
                        this.info.type = "中国菜";
                        break;
                    case "2":
                        this.info.type = "外国菜";
                        break;
                    case "3":
                        this.info.type = "各地小吃";
                        break;
                    default
                    :
                        break;

                }
                console.log(this.info.type)
                this.data()
                // console.log(tab, event);
            }
        }
    };
</script>

<style lang="less">
  .app {
    min-width: 1200px;
    max-width: 3200px;
    margin: 0 auto;
    padding: .125rem .125rem 0;
    //background-color: gray;
    //?border:1px solid red;
    display: flex;

    .itemLeft, .itemRight {
      flex: 6;
    }

    .itemCenter {
      flex: 5;
      height: 12rem;
      //background-image: url("../assets/images/dashboard/line.png");
      //border: 1px solid blue;
      padding: 0.125rem;
      margin: 0.25rem;
    }
  }

  .over {
    .over-1 {
      background-color: #ffffff;
      width: 49.7%;
      border-radius: 4px;

      .box_7 {
        background-color: rgba(234, 240, 255, 1);
        border-radius: 4px 4px 0px 0px;
        width: 100%;
        height: 2.71vw;
      }

      .section_1 {
        width: 8.29vw;
        height: 1.31vw;
        margin: 0.72vw 0 0 1.56vw;
      }

      .section_2 {
        background-color: rgba(94, 154, 253, 1);
        width: 0.27vw;
        height: 0.84vw;
        margin-top: 0.27vw;
      }

      .text_11 {
        width: 7.5vw;
        height: 1.31vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.93vw;
        font-family: AlibabaPuHuiTi-Medium;
        text-align: left;
        white-space: nowrap;
        line-height: 1.31vw;
      }

      .section_3 {
        width: 52.56vw;
        height: 0.06vw;

        margin-top: 0.63vw;
      }

      .box-main {

        width: 100%;
      }
    }

    .over-2 {
      background-color: #ffffff;
      width: 49.7%;
      border-radius: 4px;
      height: 19.17vw;

      .block_2 {
        background-color: rgba(255, 255, 255, 1);
        border-radius: 4px;
        width: 100%;
        height: 19.17vw;
      }

      .box_25 {
        background-color: rgba(234, 240, 255, 1);
        border-radius: 4px 4px 0px 0px;
        width: 100%;
        height: 2.71vw;
      }

      .box_26 {
        background-color: rgba(253, 168, 69, 1);
        width: 0.27vw;
        height: 0.84vw;
        margin: 0.98vw 0 0 1.56vw;
      }

      .text_22 {
        width: 4.64vw;
        height: 1.31vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.93vw;
        font-family: AlibabaPuHuiTi-Medium;
        text-align: left;
        white-space: nowrap;
        line-height: 1.31vw;
        margin: 0.72vw 27.96vw 0 0.52vw;
      }

      .text-wrapper_7 {
        background-color: rgba(247, 248, 250, 1);
        width: 100%;
        height: 2.3vw;
      }

      .text_23 {
        width: 2.19vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Medium;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin: 0.62vw 0 0 1.56vw;
      }

      .text_24 {
        width: 2.92vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Medium;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin: 0.62vw 0 0 11.87vw;
      }

      .text_25 {
        width: 2.92vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Medium;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin: 0.62vw 1.61vw 0 11.87vw;
      }


      .image-text_1 {
        width: 2.61vw;
        height: 1.05vw;
        margin-top: 0.11vw;
      }


      .text-group_1 {
        width: 1.72vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Regular;
        text-align: left;
        white-space: nowrap;
        line-height: 1.05vw;
      }

      .text_26 {
        width: 1.36vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Regular;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin: 0.1vw 0 0 12.03vw;
      }

      .image-text_2 {
        width: 2.92vw;
        height: 1.25vw;
        margin-left: 12.66vw;
      }

      .text-group_2 {
        width: 1.36vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(80, 201, 168, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Regular;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin-top: 0.11vw;
      }


      .box_28 {
        width: 31.78vw;
        height: 1.25vw;
        margin: 0.93vw 0 9.68vw 1.56vw;
      }

      .text_27 {
        width: 3.39vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Regular;
        text-align: left;
        white-space: nowrap;
        line-height: 1.05vw;
        margin-top: 0.11vw;
      }

      .text_28 {
        width: 1.36vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Regular;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin: 0.1vw 0 0 11.45vw;
      }

      .image-text_3 {
        width: 2.92vw;
        height: 1.25vw;
        margin-left: 12.66vw;
      }

      .text-group_3 {
        width: 1.36vw;
        height: 1.05vw;
        overflow-wrap: break-word;
        color: rgba(80, 201, 168, 1);
        font-size: 0.72vw;
        font-family: AlibabaPuHuiTi-Regular;
        text-align: center;
        white-space: nowrap;
        line-height: 1.05vw;
        margin-top: 0.11vw;
      }

    }

    .over-3 {
      background-color: #ffffff;
      width: 49.7%;
      border-radius: 4px;

      .box_7 {
        background-color: rgba(234, 240, 255, 1);
        border-radius: 4px 4px 0px 0px;
        width: 100%;
        height: 2.71vw;
      }

      .section_1 {
        width: 8.29vw;
        height: 1.31vw;
        margin: 0.72vw 0 0 1.56vw;
      }

      .section_2 {
        background-color: rgba(94, 154, 253, 1);
        width: 0.27vw;
        height: 0.84vw;
        margin-top: 0.27vw;
      }

      .text_11 {
        width: 7.5vw;
        height: 1.31vw;
        overflow-wrap: break-word;
        color: rgba(51, 51, 51, 1);
        font-size: 0.93vw;
        font-family: AlibabaPuHuiTi-Medium;
        text-align: left;
        white-space: nowrap;
        line-height: 1.31vw;
      }

      .section_3 {

        height: 0.06vw;
        background-size: 52.65vw 0.1vw;
        margin-top: 0.63vw;
      }

      .box-main {
        height: 16.46vw;
        width: 100%;
      }
    }
  }

  .over-3 {
    background-color: #ffffff;
    width: 45%;
    border-radius: 4px;
  }

  .group_4 {
    background-color: rgba(234, 240, 255, 1);
    border-radius: 4px 4px 0px 0px;
    width: 100%;
    height: 2.71vw;
  }

  .dia-left {
    width: 10px;
    height: 15px;
    padding-top: 3px;
    background: #5E9AFD;
    margin-right: 5px;
  }

  .justify-end {
    display: flex;
    justify-content: flex-end;
  }

  .text-wrapper {
    width: 23.5%;
    height: 6vw;
    padding-left: 10px;
    margin: 10px;
    background-size: 100% 100%;
  }

  .atom-color-fff {
    color: #fff;
  }

  .atom-mt-10 {
    margin-top: 10px;
  }

  .wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
  }

  .atom-flex {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
  }

  .atom-flex-column {
    flex-direction: column;
  }

  .atom-justify-center {
    justify-content: center;
    align-items: center;
  }


  .flex-col {
    display: flex;
    flex-direction: column;
  }


  .justify-between {
    display: flex;
    justify-content: space-between;

  }

  .section_5 {
    width: 6.36vw;
    height: 2.31vw;
    margin: 0.72vw 0 0 1.56vw;
  }

  .text_29 {
    font-size: 0.8vw;
    font-family: AlibabaPuHuiTi-Medium;
    text-align: left;
  }

  .box-main {
    height: 16.46vw;
    width: 100%;
  }

  .justify-around {
    display: flex;
    justify-content: space-around;

  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
