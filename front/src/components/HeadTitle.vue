<template>
    <div class="BgHead">
        <div class="lineHead">
            <h3>Hi游数据中心</h3>
        </div> 
        <p>{{date}}{{time}}</p>
        <span></span>
        <select @change="selectVal">
            <option v-for="value in values" :value="value.value">{{value.title}}</option>
        </select>
    </div>
</template>
<script type="text/babel">
    export default {
        data: () => ({
            loading: false,
            date:'',
            time:'',
            values:[
            {
                value:"5",
                title:"-----"
            },
            {
                value:"3",
                title:"网格"
            },
            {
                value:"2",
                title:"星空"
            },
            {
                value:"4",
                title:"绿色"
            },
            {
                value:"1",
                title:"紫色"
            }
            ]
        }),
    methods: {
        zeroPadding:function(num, digit) {
            var zero = '';
            for(var i = 0; i < digit; i++) {
                zero += '0';
            }
            return (zero + num).slice(-digit);
        },
        clock:function(){
            var cd = new Date();
            var week = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六'];
            this.time = this.zeroPadding(cd.getHours(), 2) + ':' + this.zeroPadding(cd.getMinutes(), 2) + ':' + this.zeroPadding(cd.getSeconds(), 2);
            this.date = this.zeroPadding(cd.getFullYear(), 4) + '-' + this.zeroPadding(cd.getMonth()+1, 2) + '-' + this.zeroPadding(cd.getDate(), 2) + ' ' + week[cd.getDay()]; 
        },
        selectVal(ele){
            var data = ele.target.value
            var links = document.getElementsByTagName("link")
            if(data != '5'){
                links[0].href = "/static/css/moban"+data+".css"
                document.cookie="theme="+data
            }
        }
    },
    mounted(){
        setInterval(this.clock, 100);
        this.clock();
    }
  }
  
</script>

<style>
    .BgHead{
        color:#fff;
        width:100%;
        background-size:cover;
		background-repeat: no-repeat;
    }
    
    .lineHead h3{
        font-size:1.9vw;
        letter-spacing:3px;
    }
    .headTitle p{
        color:#fff;
        font-size:0.9vw;
        margin:0px;
    }
    .BgHead span{
        position: absolute;
        top: 10px;
        right:30px; 
        z-index:2;
        width:20px;
        height:18px;
    }
    .BgHead select{
        position: absolute;
        top: 15px;
        right: 15px;
        border:0px;
        outline:none;
        background:none;
        font-size:12px;
        width:15px
    }
    .BgHead option{
        background-color:none;
        border:none;
        outline:none;
    }

    
    
</style>