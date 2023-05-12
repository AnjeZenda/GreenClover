import { createRouter, createWebHistory } from 'vue-router'
import EventsView from '../views/EventsView.vue'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/events',
      name: 'events',
      component: EventsView
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
})

export default router
