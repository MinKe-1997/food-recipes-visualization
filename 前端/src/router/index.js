import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'login',
        component: () => import(/* webpackChunkName: "about" */ '@/views/login'),
    },
    {
        path: '/in',
        name: 'home',
        component: HomeView,
        redirect: '/index',
        children: [

            {
                path: '/index',
                name: 'index',
                component: () => import(/* webpackChunkName: "about" */ '@/views/index/index')
            },
            {
                path: '/list',
                name: 'list',
                component: () => import(/* webpackChunkName: "about" */ '@/views/menu/list')
            },
            {
                path: '/echarts',
                name: 'echarts',
                component: () => import(/* webpackChunkName: "about" */ '@/views/echarts/echarts-1')
            },
            {
                path: '/echarts1',
                name: 'echarts1',
                component: () => import(/* webpackChunkName: "about" */ '@/views/echarts/echarts-2')
            },
            {
                path: '/echarts3',
                name: 'echarts3',
                component: () => import(/* webpackChunkName: "about" */ '@/views/echarts/echarts-3')
            },
            {
                path: '/echarts4',
                name: 'echarts4',
                component: () => import(/* webpackChunkName: "about" */ '@/views/echarts/echarts-4')
            },
            {
                path: '/echarts5',
                name: 'echarts5',
                component: () => import(/* webpackChunkName: "about" */ '@/views/echarts/echarts-5')
            }
        ]
    },

    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '@/views/AboutView.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
