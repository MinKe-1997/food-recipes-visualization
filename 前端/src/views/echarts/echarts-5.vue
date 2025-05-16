peiliao
<template>
    <el-tabs type="border-card" class="box">
        <el-tab-pane label="作者分布图">
            <div style="height: 800px">
                <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                    作者分布图
                </h2>
                <div id="type" style=" width: 1800px;height:500px;margin-top: 200px" ref="map1"/>
            </div>
            <div style="height: 800px">
                <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                    作者分布图
                </h2>
                <div id="type1" style=" width: 1800px;height:500px;margin-top: 200px" ref="map1"/>
            </div>
        </el-tab-pane>
        <el-tab-pane label="菜谱分析">
            <h2 style="margin-top: 20px;
           text-align: center;color: #c6a854;font-size: 30px">
                <el-input v-model="info.name" style="width: 400px"></el-input>
                <el-button style="margin-left: 20px" @click="cat">查询</el-button>
            </h2>
            <div id="cat" style=" width: 1800px;height:500px;margin-top: 200px" ref="map1"/>
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
                info: {
                    name: '',
                },
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
            this.ts()
        },
        methods: {
            data() {
                let results = []
                let v = []
                axios.post("api/echarts5/", this.info).then(res => {
                    const chart = document.getElementById('type')
                    const myCharts = echarts.init(chart);
                    const option = {
                        title: {
                            // text: 'Basic Radar Chart'
                        },

                        radar: {
                            shape: 'circle',
                            indicator: results
                        },
                        series: [
                            {
                                name: '',
                                type: 'radar',
                                label: {
                                    show: true
                                },
                                areaStyle: {},
                                data: [{
                                    name: "",
                                    value: v
                                }
                                ]
                            }
                        ]
                    };
                    let r = res.data.name
                    console.log(res)
                    let n = []


                    for (let i = 0; i < 20; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        results.push({name: n[i], max: 600})
                    }

                    option.series[0].data.value = v,
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
                        tooltip: {
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

                axios.post("api/echarts5/", this.info).then(res => {
                    const chart = document.getElementById('type1')
                    const myCharts = echarts.init(chart);
                    const option = {

                        backgroundColor: '#fff',
                        tooltip: {
                            show: true
                        },
                        series: [{
                            name: '发布人',//数据提示窗标题
                            type: 'wordCloud',
                            sizeRange: [12, 64],//画布范围，如果设置太大会出现少词（溢出屏幕）
                            rotationRange: [-45, 90],//数据翻转范围
                            //shape: 'circle',
                            textPadding: 0,
                            autoSize: {
                                enable: true,
                                minSize: 6
                            },
                            textStyle: {
                                normal: {
                                    color: function () {
                                        return 'rgb(' + [
                                            Math.round(Math.random() * 160),
                                            Math.round(Math.random() * 160),
                                            Math.round(Math.random() * 160)
                                        ].join(',') + ')';
                                    }
                                },
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowColor: '#333'
                                }
                            },
                            data: res.data.name,
                        }]
                    };
                    myCharts.setOption(option)
                    window.addEventListener("resize", () => {	//根据屏幕尺寸绘制echarts
                        myCharts.resize();
                    })
                })

            },
            cat() {
                let p = 0
                axios.post("api/echarts5/",this.info).then(res => {
                    const chart = document.getElementById('cat')
                    const myCharts = echarts.init(chart);
                    const option = {
                        title: {
                            text: '配料分析图(浏览量 单位万)'
                        },
                        tooltip: {
                            trigger: 'item',
                        },
                        toolbox: {
                            feature: {
                                dataView: {readOnly: false},
                                restore: {},
                                saveAsImage: {}
                            }
                        },

                        series: [
                            {
                                name: '菜名',
                                type: 'funnel',
                                left: '10%',
                                top: 60,
                                bottom: 60,
                                width: '80%',
                                min: 0,
                                max: 10000,
                                minSize: '0%',
                                maxSize: '100%',
                                sort: 'descending',
                                gap: 2,
                                label: {
                                    show: true,
                                    position: 'inside'
                                },
                                labelLine: {
                                    length: 10,
                                    lineStyle: {
                                        width: 1,
                                        type: 'solid'
                                    }
                                },
                                itemStyle: {
                                    borderColor: '#fff',
                                    borderWidth: 1
                                },
                                emphasis: {
                                    label: {
                                        fontSize: 20
                                    }
                                },
                                data: [
                                    {value: 60, name: 'Visit'},
                                    {value: 40, name: 'Inquiry'},
                                    {value: 20, name: 'Order'},
                                    {value: 80, name: 'Click'},
                                    {value: 100, name: 'Show'}
                                ]
                            }
                        ]
                    };
                    let r = res.data.cat
                    let n = []
                    let v = []

                    let results = []

                    for (let i = 0; i < r.length; i++) {
                        n[i] = r[i]["name"]
                        v[i] = r[i]["value"]
                        p = r[0]["value"].split(".")[0]
                        results.push({name: n[i], value: v[i]})
                    }
                    console.log(p)
                    option.series[0].data = results,
                    option.series[0].max = p,
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
