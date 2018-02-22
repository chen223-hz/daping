<template>
    <div class="echarts beside" >
        <div class="up" style=" height:80%;">
             <div class="titleRight"><b>手机系统占比</b><TimeButton :qq="r1" @rone="data" @ronef='fade' :values="values"></TimeButton></div>
             <IEcharts id='rightone' :option="bar" :loading="loading"  ref='ref1'></IEcharts>
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
      r1:'r1',
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
      bar: {
           
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            color:['#a84f5c','#884750','#2c8acb','#1b9cc3','#7773c2','ffffff','#c23531','#1a3d75'],
            //color:['#04342d','#0b6154','#167f70','#44a295','#68baae','99d4cc','#34f4da','#8aefe1'],
            series: [
                {
                    name:'访问来源',
                    type:'pie',
                    selectedMode: 'single',
                    radius: [0, '30%'],
                    center : ['50%', '60%'],
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
                        {value:335, name:'其他', selected:true},
                        {value:679, name:'ios'},
                        {value:1548, name:'android'}
                    ]
                },
                {
                    name:'访问来源',
                    type:'pie',
                    radius: ['40%', '60%'],
                    center : ['50%', '60%'],
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
                        {value:335, name:'苹果'},
                        {value:310, name:'华为'},
                        {value:234, name:'小米'},
                        {value:102, name:'其他'}
                    ]
                }
            ]
      }
    }),

    methods: {
        onReady(instance) {
            console.log(instance);
        },
        onClick(event, instance, echarts) {
            console.log(arguments);
        },
        data(msg){
            this.bar = msg
        },
        update(){
            this.$http.get('/json/bar',{params:{date:'today'}}).then(response => {
                this.bar = response.data
            }, response => {
                //alert('读取远程资源失败')
            })
        },
        fade(msg){
            if(msg=='ok'){
                this.$emit('fade',document.getElementById('rightone'))
            }
        }
    },
    mounted(){
        this.update()
        let that = this;
        setInterval(function(){that.update()},60000);
        var eComVisitChart = this.$refs.ref1
        window.addEventListener("resize", function () {
            eComVisitChart.resize()
    })
    }
  }
</script>
<style scoped>
    .select{
        right:20px;
    }
</style>