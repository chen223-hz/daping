<template>
    <div class="select">
            <select :ww = "qq" @change="selectVal">
                <option v-for="value in values" :value= "value.value">{{value.title}}</option>
            </select>     
        </div>
</template>
<script type="text/babel">
import TimeButton from './TimeButton.vue'
import {bus} from '../js/bus.js'
  export default {
    components:{
        TimeButton
    },
    name: 'view',
    props: {
        qq:'',
        values:'',
    },
    data: () => ({
    }),
    methods: {
        selectVal(ele){
            if(ele.target.getAttribute('ww')=='r1'){
                this.$emit('ronef','ok')
                var date = ele.target.value
                this.$http.get('/json/bar',{params:{date:date}}).then(response => {
                    this.$emit('rone',response.data);
                  }, response => {
                    //alert('读取远程资源失败')
                })
            }
            else if(ele.target.getAttribute('ww')=='l1'){
                this.$emit('lonef','ok')
                var date = ele.target.value
                this.$http.get('/json/network',{params:{date:date}}).then(response => {
                    bus.$emit('lone',response.data);
                  }, response => {
                    //alert('读取远程资源失败')
                })
            }
             else if(ele.target.getAttribute('ww')=='l2'){
                var date = ele.target.value
                this.$http.get('/json/tags',{params:{date:date}}).then(response => {
                    this.$emit('lthree',response.data);
                  }, response => {
                    //alert('读取远程资源失败')
                })
            }
        }
    },
    mounted(){
    }
  }
</script>
<style >
    .select{
        z-index:2;
        display: initial;
        height:10%; 
        position:absolute;
    }
    .select select{
        height:25px;
        background: none;
        border:0px;
        color: #fff;
        outline:none;
    }
    
</style>