<template>
    <div class="app-container">
        <div class="r-head" style="margin-top: -10px">
            <el-form ref="form" label-width="80px">
                <el-row :gutter="8">
                    <el-col :span="3">
                        <el-select v-model="selectInfo.value" clearable placeholder="请选择分类">
                            <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="4">
                        <el-form-item label="菜名">
                            <el-input placeholder="菜名" v-model="selectInfo.name" type="text"
                                      clearable></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="4">
                        <el-form-item label="菜谱数量">
                            <el-input placeholder="菜名数量" v-model="selectInfo.num" type="text"
                                      clearable></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="5" style="margin-left: 15px ">
                        <el-button type="primary" @click="qry">搜索</el-button>
                        <el-button type="reset" @click="res">重置</el-button>
                    </el-col>
                </el-row>
            </el-form>
        </div>
        <div class="r-table" style="margin-top: 20px">
            <el-table :data="dataFrom"
                      stripe
                      :border="false"
                      :row-style="{height: '60px'}"
                      :header-cell-style="{background:'rgba(137,234,55,0.66)',color:'#222276' }"
                      style="width: auto;font-size: 18px;">


                <el-table-column prop="big_type" show-overflow-tooltip label="分类" align="center"/>
                <el-table-column prop="type" show-overflow-tooltip label="类型" align="center"/>
                <el-table-column prop="img" show-overflow-tooltip label="图片" align="center">
                    <template #default="scope">
                        <el-image style="width: 100px; height: 100px" lazy
                                  referrerpolicy="no-referrer" :src="scope.row.img"/>
                    </template>
                </el-table-column>
                <el-table-column prop="name" show-overflow-tooltip label="菜名" align="center">
                    <template #default="scope">
                        <a :href="scope.row.url">{{ scope.row.name }}</a>
                    </template>
                </el-table-column>
                <el-table-column prop="peiliao" label="配料" show-overflow-tooltip align="center">
                </el-table-column>
                <el-table-column prop="zz" label="发布人" align="center">
                    <template #default="scope">
                        <el-image style="width: 100px; height: 100px" lazy
                                  referrerpolicy="no-referrer" :src="scope.row.imgze"/>
                    </template>
                </el-table-column>
                <el-table-column prop="zz" label="发布人" align="center"/>
                <el-table-column prop="sc" show-overflow-tooltip label="收藏人数" align="center"/>
                <el-table-column prop="cat" label="浏览人数" align="center"/>
                <el-table-column prop="num" show-overflow-tooltip label="配料数量" align="center"/>

            </el-table>
            <div class="atom-flex atom-justify-center" style="margin-bottom: 10px; margin-top: 10px">
                <el-pagination
                        :page-sizes="[10, 20, 50, 100]"
                        :disabled="false"
                        :total="selectInfo.total"
                        background
                        layout="total, sizes, prev, pager, next, jumper"
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";


    export default {
        data() {
            return {
                selectInfo: {
                    name: '',
                    total: 0,
                    num: '',
                    value: '',
                    pageIndex: 1,
                    pageSize: 10,
                },

                options: [],
                dataFrom: [],
            }
        },
        mounted() {
         axios.post("api/info/", this.selectInfo).then(res => {
                    this.options = res.data.items;
                    console.log(this.options)
                })
            this.hotelList()
        },
        methods: {
            hotelList() {
                axios.post("api/info/", this.selectInfo).then(res => {
                    this.selectInfo.total = res.data.total;
                    this.dataFrom = res.data.list;
                    this.options = res.data.items;
                    console.log(this.options)
                })
            },
            res() {
                this.selectInfo.name = ''
                this.selectInfo.value = ''
                this.selectInfo.num = ''
                this.selectInfo.pageIndex = 1
                this.selectInfo.pageSize = 10
                this.hotelList()
            },
            qry() {
                this.hotelList()
            },
            handleCurrentChange(val) {
                this.selectInfo.pageIndex = val
                this.selectInfo.pageSize = 10
                this.hotelList()
            },
            handleSizeChange(val) {
                this.selectInfo.pageSize = val
                this.selectInfo.pageIndex = 1;
                this.hotelList()
            }
        }
    }
</script>


<style lang="css">
    .dialog-footer button:first-child {
        margin-right: 60px;
    }


    el-row:last-child {
        margin-bottom: 0;
    }

    .atom-flex {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
    }

    .atom-justify-center {
        margin-top: 20px;
        justify-content: right;
    }

    .r-table {
        margin-top: 10px;
        border-radius: 4px;
        border: 1px solid #EEEEEE;
    }

    .r-option {
        margin-top: 10px;
        border-radius: 4px;
        background-color: #F7F8FA;
        padding: 5px;
    }

    .ds-box {
        background: #F3F4F9;
        padding: 20px;
    }

    .box-14 {
        padding-left: 20px;
        border-radius: 4px;
        background-color: rgba(255, 255, 255, 1) !important;
    }

    .r-select {
        margin-top: 10px;
        height: 40px;
        padding-top: 20px;
        padding-left: 20px;
        border-radius: 4px;
        background-color: #faf9f7;
    }

    .r-head {
        margin-top: 0px;
        padding-top: 20px;
        padding-left: 20px;
        border-radius: 4px;
        background-color: #faf9f7;
    }

    el-col {
        border-radius: 4px;
    }

    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
</style>
