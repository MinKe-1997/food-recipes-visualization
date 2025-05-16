peiliao<template>
    <el-tabs type="border-card" class="box">
        <el-tab-pane label="浏览量">
            <div class="itemCenter">
                <div style="height: 500px;float: left ;width: 49%;margin-top: -15px">

                    <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                        中国菜浏览量top10
                    </h2>
                    <div id="evaluation" style=" width: 100%;height: 80%" ref="map1"/>
                </div>
                <div style="height: 500px;margin-left: 50% ;width: 49%">
                        <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                            外国菜浏览量top10
                        </h2>
                        <div id="ts" style=" width: 100%;height: 80%" ref="map1"/>
                </div>
            </div>
            <div class="itemRight">
                <div style="height: 500px;float: left;width: 49%;margin-top: -15px">
                        <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                            各地小吃浏览量top10
                        </h2>
                        <div id="type2" style=" width: 100%;height: 100%" ref="map1"/>

                </div>
                <div style="height: 500px;margin-left: 50%;width: 49%">
                        <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                            菜式浏览量top10
                        </h2>
                        <div id="collection" style=" width: 100%;height: 85%" ref="map1"/>
                </div>
            </div>
        </el-tab-pane>
        <el-tab-pane label="浏览量top20">
            <div style="height: 800px">
                <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                    浏览量top20
                </h2>
                <div id="type" style=" width: 1800px;height:500px;margin-top: 200px" ref="map1"/>
            </div>
        </el-tab-pane>

    </el-tabs>
</template>

<script>
    import axios from "axios";
    import * as echarts from 'echarts'

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
            this.evaluation()
            this.data1()
            this.date()
            this.ts()
        },
        methods: {
            data() {
                axios.post("api/echarts4/").then(res => {
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
                            name: '菜名',
                            label: {
                                textColor: 'break'
                            }
                        },
                        yAxis: {
                            type: 'value',

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
                    let r = res.data.cat
                    console.log(res)
                    let n = []
                    let v = []
                    let p = []
                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        // p[i] = r[i]["price"]
                    }
                    option.series[0].data = v,
                        option.series[1].data = v,
                        // option.series[2].data = v,
                        option.xAxis.data = n,
                        myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })
            },

            ts() {
                axios.post("api/echarts4/").then(res => {
                    const chart = document.getElementById('ts')
                    const myCharts = echarts.init(chart);
                    const option = {
                        tooltip: {
                            trigger: 'item'
                        },
                        legend: {
                            top: '5%',
                            left: 'center'
                        },
                        toolbox: {
                            show: true,
                            feature: {
                                mark: {show: true},
                                dataView: {show: true, readOnly: false},
                                restore: {show: true},
                                saveAsImage: {show: true}
                            }
                        },
                        series: [
                            {
                                name: '浏览量top10',
                                type: 'pie',
                                radius: ['40%', '70%'],
                                avoidLabelOverlap: false,
                                itemStyle: {
                                    borderRadius: 10,
                                    borderColor: '#fff',
                                    borderWidth: 2
                                },
                                label: {
                                    show: false,
                                    position: 'center'
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        fontSize: 40,
                                        fontWeight: 'bold'
                                    }
                                },
                                labelLine: {
                                    show: true
                                },
                                data: [
                                    {value: 1048, name: 'Search Engine'},
                                    {value: 735, name: 'Direct'},
                                    {value: 580, name: 'Email'},
                                    {value: 484, name: 'Union Ads'},
                                    {value: 300, name: 'Video Ads'}
                                ]
                            }
                        ]
                    };
                    let r = res.data.wg
                    let n = []
                    let v = []
                    let results = []

                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        results.push({name: n[i], value: v[i]})
                    }
                    console.log(v)
                    console.log(n)
                    option.series[0].data = results,
                        option.legend.data = n,
                        myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })
            },
            evaluation() {
                let results = []
                let v = []
                axios.post("api/echarts4/").then(res => {
                    const chart = document.getElementById('evaluation')
                    const myCharts = echarts.init(chart);
                    const option = {
                        tooltip:{
                            trigger: 'item'
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left'
                        },
                        toolbox: {
                            show: true,
                            feature: {
                                mark: {show: true},
                                dataView: {show: true, readOnly: false},
                                restore: {show: true},
                                saveAsImage: {show: true}
                            }
                        },
                        series: [
                            {
                                name: '浏览量top10',
                                type: 'pie',
                                show: 'true',
                                radius: [50, 180],
                                center: ['50%', '50%'],
                                roseType: 'area',
                                itemStyle: {
                                    borderRadius: 8
                                },
                                data: [
                                    {value: 40, name: 'rose 1'},
                                    {value: 38, name: 'rose 2'},
                                    {value: 32, name: 'rose 3'},
                                    {value: 30, name: 'rose 4'},
                                    {value: 28, name: 'rose 5'},
                                    {value: 26, name: 'rose 6'},
                                    {value: 22, name: 'rose 7'},
                                    {value: 18, name: 'rose 8'}
                                ]
                            }
                        ]
                    };
                    let r = res.data.zg
                    let n = []
                    let v = []
                    let results = []

                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        results.push({name: n[i], value: v[i]})
                    }
                    console.log(v)
                    console.log(n)
                    option.series[0].data = results,
                        option.legend.data = n,
                        myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })
            },

            data1() {
                axios.post("api/echarts4/").then(res => {
                    const chart = document.getElementById('type2')
                    const myCharts = echarts.init(chart);
                    const option = {
                        tooltip:{
                            trigger: 'item'
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left'
                        },
                        toolbox: {
                            show: true,
                            feature: {
                                mark: {show: true},
                                dataView: {show: true, readOnly: false},
                                restore: {show: true},
                                saveAsImage: {show: true}
                            }
                        },
                        series: [
                            {
                                name: '浏览量top10',
                                type: 'pie',
                                show: 'true',
                                radius: [50, 180],
                                center: ['50%', '50%'],
                                roseType: 'area',
                                itemStyle: {
                                    borderRadius: 8
                                },
                                data: [
                                    {value: 40, name: 'rose 1'},
                                    {value: 38, name: 'rose 2'},
                                    {value: 32, name: 'rose 3'},
                                    {value: 30, name: 'rose 4'},
                                    {value: 28, name: 'rose 5'},
                                    {value: 26, name: 'rose 6'},
                                    {value: 22, name: 'rose 7'},
                                    {value: 18, name: 'rose 8'}
                                ]
                            }
                        ]
                    };
                    let r = res.data.gd
                    let n = []
                    let v = []
                    let results = []

                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        results.push({name: n[i], value: v[i]})
                    }
                    console.log(v)
                    console.log(n)
                    option.series[0].data = results,
                        option.legend.data = n,
                        myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })
            },
            date() {
                axios.post("api/echarts4/").then(res => {
                    const chart = document.getElementById('collection')
                    const myCharts = echarts.init(chart);
                    const option = {
                        tooltip: {
                            trigger: 'item'
                        },
                        legend: {
                            orient: 'vertical',
                            left: '120px'

                        },
                        toolbox: {
                            show: true,
                            feature: {
                                mark: {show: true},
                                dataView: {show: true, readOnly: false},
                                restore: {show: true},
                                saveAsImage: {show: true}
                            }
                        },
                        series: [
                            {
                                name: '浏览量top10',
                                type: 'pie',
                                radius: ['40%', '70%'],
                                avoidLabelOverlap: false,
                                itemStyle: {
                                    borderRadius: 10,
                                    borderColor: '#fff',
                                    borderWidth: 2
                                },
                                label: {
                                    show: false,
                                    position: 'center'
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        fontSize: 40,
                                        fontWeight: 'bold'
                                    }
                                },
                                labelLine: {
                                    show: true
                                },
                                data: [
                                    {value: 1048, name: 'Search Engine'},
                                    {value: 735, name: 'Direct'},
                                    {value: 580, name: 'Email'},
                                    {value: 484, name: 'Union Ads'},
                                    {value: 300, name: 'Video Ads'}
                                ]
                            }
                        ]
                    };
                    let r = res.data.cs
                    let n = []
                    let v = []
                    let results = []

                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        results.push({name: n[i], value: v[i]})
                    }
                    console.log(v)
                    console.log(n)
                    option.series[0].data = results,
                        option.legend.data = n,
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
