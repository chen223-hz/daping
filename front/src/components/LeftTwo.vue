<template>
    <div class="echarts beside">
        <div class="up" style=" height:85%;">   

            <div class="titleLeft"><b>入园人数统计</b><TimeButton :qq="l2" @lthree='data' :values="values"></TimeButton></div>
            <IEcharts  id="leftTwo"  :option="tags" :loading="loading" ref='ref1'></IEcharts>

        </div>
    </div>
</template>
<script type="text/babel">
import TimeButton from './TimeButton.vue'
  export default {
    components:{
        TimeButton
    },
    name: 'view',
    props: {
    },
    data: () => ({
      loading: false,
      l2:'l2',
      values:[
        {
            value:"week",
            title:"一周"
        },
        {
            value:"month",
            title:"一个月"
        }
        ],
      tags : {
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#207dde'
                    }
                }
            },
            grid: {
                left: '5%',
                right: '8%',
                top:'13%',
                bottom:'2%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    axisLine:{
                        lineStyle:{
                            color:'#fff'
                        }
                    },
                    data : ['周一','周二','周三','周四','周五','周六','周日']
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    axisLine:{
                        lineStyle:{
                            color:'#fff'
                        }
                    }
                }
            ],
            series : [
                {
                    type:'line',
                    stack: '总量',
                    areaStyle: {normal: {
                        color:'#207dde'
                        //color:'#167f70'
                    }},
                    itemStyle : {  
                                normal : {  
                                    lineStyle:{  
                                        color:'#1a73d0'
                                         //color:'#167f70'  
                                    }  
                                }  
                            }, 
                    data:[220, 182, 191, 234, 290, 330, 310]
                },
            ],
            items:[]
        }
    }),

    methods: {
        update(){
            this.$http.get('/json/tags',{params:{date:'week'}}).then(response => {
                this.tags = response.data
            }, response => {
                //alert('读取远程资源失败')
            })
       },
       data(msg){
        this.tags = msg
       }
    },
    mounted(){
        this.update()
        let that = this
        setInterval(function(){that.update()},60000)
        var eComVisitChart = this.$refs.ref1
        window.addEventListener("resize", function () {
            eComVisitChart.resize()
    })
    }
  }
  
</script>
<style scoped>
    .select{
        left:20px;
    }  
</style>