import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import ProductList from '../views/ProductList.vue' // Asegúrate de que esta línea esté presente

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/products',
    name: 'ProductList',
    component: ProductList, // Asegúrate de que esta línea esté presente
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
