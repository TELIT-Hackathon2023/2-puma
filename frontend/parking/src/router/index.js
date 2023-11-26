import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/account',
      name: 'account',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/Account.vue')
    },
    {
      path: "/register",
      name: "register",
      component: () => import('../components/RegisterBox.vue')
    }
    // {
      // path: "/register",
      // name: "register",
      // component: () => import('../components/RegisterBox.vue')
    // }
  ]
})

export default router
