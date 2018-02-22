<template>
    <ul class="num">
       <li><img src="/static/img/num.png" :ass="cl"/></li>
       <li><img src="/static/img/num.png" :ass="cl"/></li>
       <li><img src="/static/img/num.png" :ass="cl"/></li>
       <li><img src="/static/img/num.png" :ass="cl"/></li>
       <li><img src="/static/img/num.png" :ass="cl"/></li>
       <li><img src="/static/img/num.png" :ass="cl"/></li>
       <li><img src="/static/img/num.png" :ass="cl"/></li>
    </ul>
</template>
<script type="text/babel">
    export default {
        props: {
            datall:'',
            datanow:'',
            cl:''
        },
        methods:{
            getStyle(obj,name){
                if(obj.currentStyle){
                    return obj.currentStyle[name];
                }else{
                    return getComputedStyle(obj,false)[name];   
                }
            },
            move(obj,json,options){
                options=options||{};
                options.duration=options.duration||700;
                options.easing=options.easing||'ease-in';
                var count=Math.floor(options.duration/30);
                var start={};
                var dis={};
                for(var name in json){
                    start[name]=parseFloat(this.getStyle(obj,name));
                    dis[name]=json[name]-start[name];
                }
                var n=0;
                clearInterval(obj.timer);
                obj.timer=setInterval(function(){
                    n++;
                    for(var name in json){
                        switch(options.easing){
                            case 'linear':
                                var cur=start[name]+dis[name]*n/count;
                            break;
                            case 'ease-in':
                                var a=Math.pow(n/count,3);
                                var cur=start[name]+dis[name]*a;
                            break;  
                            case 'ease-out':
                                var a=Math.pow(1-n/count,3);
                                var cur=start[name]+dis[name]*(1-a);
                            break;
                        }
                        if(name=='opacity'){
                            obj.style[name]=cur;
                            obj.style.filter='alpha(opacity:'+(cur*100)+')';    
                        }else{
                            obj.style[name]=cur+'px';       
                        }
                    }
                    if(n==count){
                        clearInterval(obj.timer);
                        
                        options.complete&&options.complete();
                    }
                    
                },30);
            },
            buwei(n){
                var aa = ''
                for(var i=0;i<7-n;i++){
                    aa = aa + '0'
                }
                return aa
            },
            num(datall,ele){
                var cc=document.getElementsByTagName("img")
                var oImg = []
                for(var i=0;i<cc.length;i++){
                    if(cc[i].getAttribute('ass') == ele){
                        oImg.push(cc[i])
                    }
                }
                var data = datall
                var num = data.toString().length
                var dd = this.buwei(num)+data.toString()
                for(var i=0;i<oImg.length;i++){
                    this.move(oImg[i],{"marginTop":-35*dd.charAt(i)});
                }
            }
        },
        watch:{
            datall: function(){
                this.num(this.datall,'data_all')
            },
            datanow:function(){
                this.num(this.datanow,'data_now')
            }
        },
        mounted(){
        }
    }
</script>
<style>
    .num li{ 
        float:left; 
        height:35px; 
        overflow:hidden; 
        line-height:35px;
    }
    .num{
        margin-top:10px;
        padding-left:1.4vw;
    }
    @media screen and (min-width:1366px) and (max-width:1680px){ 
        .num{
            padding-left:1vw;
        }
    }
    @media screen and (min-width:1280px) and (max-width:1366px){ 
        .num{
            padding-left:0vw;
        }
    } 
    @media screen and (min-width:1024px) and (max-width:1280px){ 
        .num{
            padding-left:1.4vw;
        }
    } 
</style>