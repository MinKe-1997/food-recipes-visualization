import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'  // 确保导入路径正确
import 'element-plus/dist/index.css'

import router from './router'
import store from './store'
import axios from 'axios'

// ✅ Vue3 版 datav（兼容 Vue3）
import dataV from '@kjgl77/datav-vue3'

const app = createApp(App)

// 设置全局 axios
app.config.globalProperties.$axios = axios

// 使用插件
app.use(router)
app.use(store)
app.use(ElementPlus, { locale: zhCn })
app.use(dataV)

// 挂载应用
app.mount('#app')