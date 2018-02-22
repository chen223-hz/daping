<template>
    <div class="echarts beside" >
        <div class="up" style=" height:100%;">
              <div class="titleRight"><b>环境质量</b></div>
             <IEcharts  id="environment" :option="radar" :loading="loading"></IEcharts>
        </div>
    </div>
 <!-- <div class="environment">
      <div>温度： {{ environment.temp }}</div>
      <div>空气湿度： {{ environment.humidity }}</div>
      <div>土壤湿度: {{ environment.moisture }}</div>
      <div>风力: {{ environment.winds }}</div>
  </div>!-->
</template>

<script>
export default {
    computed: {
        environment () {
            return this.$store.state.environment;
        }
    },
    data: () => ({
      loading: false,
      r3:'r3',
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
      radar : {
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
            legend: {
                data:['湿度','降水量','平均温度','风力'],
                textStyle:{
                    color:'#fff'
                }
            },
            xAxis: [
                {
                    type: 'category',
                    data: ['02','04','06','08','10','12','14','16','18','20','22','24'],
                    
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
                    name: '水量',
                    min: 0,
                    max: 250,
                    interval: 50,
                    axisLabel: {
                        formatter: '{value} ml'
                    },
                    axisLine:{
                        lineStyle:{
                            color:'#fff'
                        }
                    }
                },
                {
                    type: 'value',
                    name: '温度',
                    min: 0,
                    max: 25,
                    interval: 5,
                    axisLabel: {
                        formatter: '{value} °C'
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
                    name:'湿度',
                    type:'bar',
                    data:[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                    itemStyle:{
                            normal:{
                                color:['#207dde']
                                //color:['#167f70']
                            }
                    },
                    barGap: '10%', 
                },
                {
                    name:'降水量',
                    type:'bar',
                    data:[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                    itemStyle:{
                            normal:{
                                color:['#c23531']
                                //color:['#44a295']
                            }
                    }
                },
                {
                    name:'平均温度',
                    type:'line',
                    yAxisIndex: 1,
                    data:[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                    itemStyle:{
                            normal:{
                                color:['#FFF']
                            }
                    }
                },
                {
                    name:'风力',
                    type:'line',
                    yAxisIndex: 1,
                    data:[2.0,10.2, 20.3,16.5, 12.2,  23.4, 23.0, 3.3, 4.5, 6.3, 12.0, 6.2],
                    itemStyle:{
                            normal:{
                                color:['#FFF']
                            }
                    }
                }
                
            ]
        }
    })
}
</script>

<style scoped>
.environment {
    color: white;
}
</style>
