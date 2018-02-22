<template>
  <div class="echarts"  id="up" >
    <div class="titleLeft"><b>游客数据分析</b><TimeButton :qq="l1" :values="values" @lonef = 'fade'></TimeButton></div>

    <div class="up"style=" height:50%;">
        <IEcharts  ref='ref1' id="upCharts":option="network" :loading="loading" ></IEcharts>
    </div>
    <div class="down" style="height:50%;">
       <IEcharts id='leftone' ref='ref2'  :option="network2" :loading="loading" ></IEcharts>
    </div>   

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
    },
    data: () => ({
      loading: false,
      l1:'l1',
      values:[{
            value:"today",
            title:"今天"
        },
        {
            value:"yesterday",
            title:"昨天"
        },
        {
            value:"week",
            title:"一周"
        },
        {
            value:"month",
            title:"一个月"
        }
        ],
        network:{
             tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            
            series: [
                {
                    name:'访问来源',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '30%'],
                    center : ['50%', '55%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:679, name:'男游客'},
                        {value:1548, name:'女游客'}
                    ],
                    color:['#3daafc','#207dde']
                    //color:['#167f70','#44a295']
                },
                {
                    name:'访问来源',
                    type:'pie',
                    radius: ['40%', '60%'],
                    center : ['50%', '55%'],
                    label: {
                        normal: {
                           
                            rich: {
                                a: {
                                    color: '#999',
                                    lineHeight: 22,
                                    align: 'center'
                                },
                                hr: {
                                    borderColor: '#aaa',
                                    width: '100%',
                                    borderWidth: 0.5,
                                    height: 0
                                },
                                b: {
                                    fontSize: 16,
                                    lineHeight: 33
                                },
                                per: {
                                    color: '#eee',
                                    backgroundColor: '#334455',
                                    padding: [2, 4],
                                    borderRadius: 2
                                }
                            }
                        }
                    },
                    data:[
                        {value:335, name:'新游客'},
                        {value:310, name:'老游客'}
                    ],
                    color:['#fff','#207dde']
                    //color:['#fff','#167f70']
                    }
                
            ]
        },
        network2:{
            tooltip: {
            trigger: 'axis',
            axisPointer: {
                crossStyle: {
                    color: '#fff'
                }
            }
            },
            grid: {
                left: '5%',
                right: '5%',
                bottom:'18%',
                containLabel: true
            },
            xAxis: [
                {
                    type: 'category',
                    data: ['男/女','新/老'],
                    
                    axisLine:{
                        lineStyle:{
                            color:'#fff'
                        }
                    }
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '百分比',
                    min: 0,
                    max: 100,
                    interval: 20,
                    axisLabel: {
                        formatter: '{value} %'
                    },
                    axisLine:{
                        lineStyle:{
                            color:'#fff'
                        }
                    }
                }
            ],
            series: [
                {
                    name:'男/女',
                    type:'bar',
                    data:[84.0, 50.4],
                    barWidth :35,
                    itemStyle:{
                            normal:{
                                color:['#207dde']
                                //color:['#167f70']
                            }
                    },
                    barGap: '10%', 
                },
                {
                    name:'新/老',
                    type:'bar',
                    barWidth : 35,
                    data:[37.7, 20.0],
                    itemStyle:{
                            normal:{
                                color:['#c23531']
                                //color:['#44a295']
                            }
                    }
                }
                
            ]
        }
    }),

    methods: {
        update(date){
            this.$http.get('/json/network',{params:{date:date}}).then(response => {
                this.network = response.data
            }, response => {
                //alert('读取远程资源失败')
            })
        },
        fade(msg){
            if(msg=='ok'){
                this.$emit('fade',document.getElementById('leftone'))
            }
        }
    },
    mounted(){
        this.update('today')
        bus.$on('lone', value => { //Hub接收事件
            this.network = value
        })
        let that = this
        setInterval(function(){that.update('today')},600000)
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

