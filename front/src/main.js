import Vue from 'vue'
import VueRouter from 'vue-router'
import IEcharts from 'vue-echarts-v3'
import BaiduMap  from 'vue-baidu-map'
import axios from './utils/http.js'
import Websocket from './utils/websocket.js'
import router from './router'
import store from './store'
import App from './app'
Vue.use(BaiduMap, {
  // ak 是在百度地图开发者平台申请的密钥 详见 http://lbsyun.baidu.com/apiconsole/key */
  ak: 'F0i6SrLmHquLVNLCqpExxPrj8mWVdFwx'
})
Vue.use(Websocket, 'ws://' + window.location.host + '/echo')
Vue.component('IEcharts', IEcharts)
Vue.prototype.$http = axios
Vue.config.debug = false
Vue.config.devtools = true

let Docs = Vue.component('app', App)
Docs = new Docs({
    router,
    store,
}).$mount('#app')
