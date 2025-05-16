import { defineConfig } from 'vite'
import path from 'path'
import vue from '@vitejs/plugin-vue' // 引入 vue 插件

export default defineConfig({
  plugins: [vue()], // 使用 vue 插件

  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // 设置 '@' 别名指向 'src' 目录
    }
  },

  server: {
    host: '0.0.0.0',
    port: 8020, // 设置端口
    open: false,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '') // 解决跨域问题，重写路径
      }
    }
  }
})