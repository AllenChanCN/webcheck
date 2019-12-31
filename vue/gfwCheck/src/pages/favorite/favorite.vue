<template>
  <div >
    <left-index :activity="'favorite'"></left-index>
    <favorite-header></favorite-header>
    <favorite-list></favorite-list>
  </div>
</template>

<script>
import LeftIndex from '@/pages/communal/leftindex'
import FavoriteHeader from './components/header'
import FavoriteList from './components/favoritelist'
export default {
  name: 'favorite',
  components: {
    LeftIndex,
    FavoriteHeader,
    FavoriteList
  }
}
</script>

<style lang="stylus" scoped>

</style>
