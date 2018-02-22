<template>
    <div class="echarts beside" >
        <div class="titleRight"><b>{{ title }}</b></div>
        <ul>
            <li class="Dan" v-for="(item,index) in recent_userlist"><b>NO.{{index+1}}</b>{{item.title}}</li>
        </ul> 
    </div> 
</template>

<script type="text/babel">
export default {
    data: () => ({
        title: '最新认证用户上线通知'
    }),
    computed: {
        recent_userlist () {
            return this.$store.state.recent_users;
        }
    }
}
</script>

<style scoped>
     ul{
        padding:0px 25px;
        margin-top:15px;
    }
    li{
        list-style:none;
        color:#fff;
        text-align:left;
        margin-top:0.7vw;
        letter-spacing:2px;
        font-size:0.9vw;
        padding:0.3vw 0;
    }
    li b{
        margin-right:18px;
    }
    .title{
        color:#fff;
        text-align:left;
        margin-left:1.8vw;
        margin-top:0.1vw;
    }
</style>
