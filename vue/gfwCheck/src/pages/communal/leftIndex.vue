<template>
    <div class="navigation">
        <div class="indexlist">
          <router-link
            :to="'/'+cls"
            :key='cls'
            v-for='(text, cls) of menulist'
            class="router-link"
          >
            <div
              :class="{'links':true, 'activated':iscurrent(cls)}"
            >
              <span>{{text}}</span>
            </div>
          </router-link>
        </div>
    </div>
</template>

<script>
export default {
  name: 'LeftIndex',
  data () {
    return {
      'menulist': {
        'index': '查询',
        'favorite': '我的收藏',
        'crontab': '定时任务'
      }
    }
  },
  props: {
    activity: {
      default: 'favorite'
    }
  },
  methods: {
    iscurrent (cls) {
      return cls === this.activity
    }
  }
}
</script>

<style lang="stylus" scoped>
  .navigation
    width: 20%
    height: 100%
    float: left
    border-right: solid
    padding-left: 0
    margin-left: 0
    .indexlist
      position: relative
      top: 50px
      margin: 2px
      .router-link
        text-decoration: none
        .links
          background-color: #ccc
          border-bottom: solid #eee
        .activated
          background-color: #888
</style>
