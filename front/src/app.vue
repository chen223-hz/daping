<template>
    <div id="app">
        <section class="main-content">
            <div class="wrapper">
                <transition name="fade" mode="out-in" appear>
                    <router-view></router-view>
                </transition>
            </div>
        </section>
    </div>
</template>

<script>
    import Vue from 'vue'
    export default {
        name: 'app'
    }
</script>

<style lang="less">
body, html {
    height: 100%;
    margin:0;
    padding:0;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s
}
.fade-enter, .fade-leave-active {
  opacity: 0
}
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    overflow: hidden;
    position: absolute;
    width: 100%;
    height: 100%;
}
#app .main-content {
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    overflow: hidden;
}
#app .main-content .wrapper{
    height:100%;
    overflow:auto;
}

</style>
