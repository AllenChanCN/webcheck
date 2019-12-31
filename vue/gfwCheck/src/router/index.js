import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/index/index'
import favorite from '@/pages/favorite/favorite'
import crontab from '@/pages/crontab/crontab'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/favorite',
      name: 'favorite',
      component: favorite
    },
    {
      path: '/crontab',
      name: 'crontab',
      component: crontab
    }
  ]
})
