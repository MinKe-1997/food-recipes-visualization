<template>
    <el-tabs type="border-card" class="box">
        <el-tab-pane label="分类可视化top10">
            <div style="height: 800px">
            <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                分类可视化top10
            </h2>
            <div id="type" style=" width: 100%;height:500px;margin-top: 200px" ref="map1"/>
            </div>
        </el-tab-pane>

        <el-tab-pane label="类型可视化top10">
            <div style="height: 800px">
                <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                    类型可视化top10
                </h2>
                <div id="time" style=" width: 1800px;height:500px;margin-top: 200px" ref="map"/>
            </div>
        </el-tab-pane>

    </el-tabs>

</template>

<script>
    import axios from "axios";
    import * as echarts from 'echarts'
    import "@/components/echarts-wordcloud.min.js"

    export default {
        name: "echarts-1",
        data() {
            return {
                config1: {
                    number: [100],
                    content: '{nt}个'
                }
            }

        },

        mounted() {
            this.data()
            this.time()
        },
        methods: {
            data() {
                axios.post("api/echarts/").then(res => {
                    const chart = document.getElementById('type')
                    const myCharts = echarts.init(chart);
                    const option = {
                        tooltip: {
                            // 鼠标停放时提示数据
                            trigger: 'axis'
                        },

                        grid: {
                            y: 30,
                            y2: 30
                        },
                        xAxis: {
                            type: 'category',
                            data: [],
                            label: {
                                textColor: 'blue'
                            }
                        },
                        yAxis: {
                            type: 'value',

                            max:10000,
                            min:0,
                            splitNumber:10,
                        },
                        series: [
                            {
                                name: '数量',
                                data: [],
                                type: 'bar',
                                barWidth: '30%',
                                label: {
                                    //数据显示的位置
                                    show: true, //数值是否显示
                                    rotate: 60, //数值显示的角度
                                    position: "top", //数值相对于柱状图显示的位置
                                },
                                itemStyle: {
                                    color: function (d) {
                                        return "#" + Math.floor(Math.random() * (256 * 256 * 256 - 1)).toString(16);
                                    }
                                }
                            },
                            {
                                name: '数量',
                                data: [],
                                type: 'line',
                                barWidth: '30%',
                                label: {
                                    //数据显示的位置
                                    show: true, //数值是否显示
                                    rotate: 60, //数值显示的角度
                                    position: "top", //数值相对于柱状图显示的位置
                                },
                                itemStyle: {
                                    color: function (d) {
                                        return "#" + Math.floor(Math.random() * (256 * 256 * 256 - 1)).toString(16);
                                    }
                                }
                            }
                        ]
                    }
                    let r = res.data.big
                    let n = []
                    let v = []
                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                    }
                    option.series[0].data = v,
                        option.series[1].data = v,
                        option.xAxis.data = n,
                        myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })
            },

            time() {
                axios.post("api/echarts/").then(res => {
                    const chart = document.getElementById('time')
                    const myCharts = echarts.init(chart);
                    const option = {
                        tooltip: {
                            // 鼠标停放时提示数据
                            trigger: 'axis'
                        },

                        grid: {
                            y: 30,
                            y2: 30
                        },
                        xAxis: {
                            type: 'category',
                            data: [],
                            label: {
                                textColor: 'break'
                            }
                        },
                        yAxis: {
                            type: 'value',
                            max:1000,
                            min:0,
                            splitNumber:20,
                        },
                        series: [

                            {
                                name: '数量',
                                data: [],
                                type: 'line',
                                barWidth: '30%',
                                label: {
                                    //数据显示的位置
                                    show: true, //数值是否显示
                                    rotate: 60, //数值显示的角度
                                    position: "top", //数值相对于柱状图显示的位置
                                },
                                itemStyle: {
                                    color: function (d) {
                                        return "#" + Math.floor(Math.random() * (256 * 256 * 256 - 1)).toString(16);
                                    }
                                }
                            }
                        ]
                    }
                    let r = res.data.type
                    let n = []
                    let v = []
                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                    }
                    option.series[0].data = v,
                        option.xAxis.data = n,
                        myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })
            },


        }

    }
</script>

<style lang="less">
  .box{
    //background-image: url(../../assets/img.png);
  }

  .app {
    min-width: 1200px;
    max-width: 3200px;
    margin: 0 auto;
    padding: .125rem .125rem 0;
    //background-color: gray;
    //?border:1px solid red;
    display: flex;

    .itemLeft, .itemRight {
      flex: 3;
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
</style>
