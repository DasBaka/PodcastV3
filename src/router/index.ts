// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/Player.vue'),
      },
      {
        path: 'podcasts', name: 'Podcasts',
        component: () => import('@/views/Podcasts.vue'),
      },
      {
        path: 'filters', name: 'Filters',
        component: () => import('@/views/Filters.vue'),
      },
      {
        path: 'profile', name: 'Profile',
        component: () => import('@/views/Profile.vue'),
      },
      {
        path: 'player', name: 'Player', 
        component: () => import('@/views/Player.vue'),
      },
      {
        path: 'queue', name:'Queue',
        component: () => import('@/views/Queue.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
