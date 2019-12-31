<template>
    <div class="main">
        <div class="header">
          警告：本页面只可测试91的域名
        </div>
        <div class="inputArea">
              <textarea class="inputBlock" v-model="urlTexts"></textarea>
        </div>
        <div class="actionArea">
            <div class="btn">
                <div class="singlebtn"><button @click="resetInput" class="warningbtn">重置内容</button></div>
                <!-- <div class="singlebtn"><button class="infobtn">保存查询内容</button></div> -->
                <div class="singlebtn"><button @click="handleSubmit" class="infobtn">提交查询</button></div>
                <!-- <div class="singlebtn"><button class="errorbtn">终止查询</button></div> -->
            </div>
        </div>
        <div class="logarea">
            <table>
              <th v-if="hasRetInfo">
                <td>域名</td>
                <td>检测结果</td>
              </th>
              <tr v-for='item of retInfo' :key='item[0]'>
                <td>{{item[0]}}</td>
                <td v-if="item[1]">域名正常</td>
                <td v-else>域名异常, 原因: {{item[2]}}</td>
              </tr>
            </table>
        </div>
    </div>
</template>

<script>
export default {
  name: 'container',
  data () {
    return {
      urlTexts: '',
      retInfo: [],
      hasRetInfo: false
    }
  },
  watch: {
    retInfo () {
      if (this.retInfo.length === 0) {
        this.hasRetInfo = false
      } else {
        this.hasRetInfo = true
      }
    }
  },
  methods: {
    resetInput () {
      this.urlTexts = ''
    },
    handleSubmit () {
      let urls = this.urlTexts
      urls = urls.split(/[\s\n]/)
      for (let i in urls) {
        var u = urls[i]
        if (!u) {
          return
        }
        var url = '/check/' + u
        this.$axios.get(url, '')
          .then(response => {
            if (response.status === 200) {
              var rd = response.data
              for (let k in rd) {
                if (rd[k]) {
                  this.retInfo.push([k, true, rd[k]])
                } else {
                  this.retInfo.push([k, false, '标识文件检测失败'])
                }
              }
            } else {
              this.retInfo.push([u, false, '后台查询失败'])
            }
          }, err => {
            this.retInfo.push([u, false, '操作异常，原因:' + err])
          })
          .catch((error) => {
            this.retInfo.push([u, false, '操作异常，原因:' + error])
          })
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .main
    width: 50%
    float: left
    .header
      color: red
    .inputArea
      margin: 10px
      padding: 2px
      .inputBlock
        height: 200px
        width: 100%
    .actionArea
      text-align: center
      .btn
        position: relative
        left: 0
        .singlebtn
          padding: 5px
          display: flex
          float: left
    .logarea
      clear: both
  .warningbtn
    background-color: #ff0
    color: red
  .infobtn
    background-color: green
    color: white
  .errorbtn
    background-color: red
    color: white
</style>
