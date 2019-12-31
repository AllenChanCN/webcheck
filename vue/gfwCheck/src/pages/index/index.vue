<template>
  <div>
    <left-index :activity="'index'"></left-index>
    <container></container>
    <log></log>
  </div>
</template>

<script>
import LeftIndex from '@/pages/communal/leftindex'
import container from './components/container'
import log from './components/log'
export default {
  name: 'index',
  components: {
    LeftIndex,
    container,
    log
  }
}
</script>

<style lang="stylus" scoped>
</style>
