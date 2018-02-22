<template>
    <div class="echarts">
        <div class="centerTitle">
            <div class="numGarden">
                <div class="real">
                    <h4>实时在园人数</h4>
                    <numData :datanow = 'usercount.realtime' :cl='data_now'></numData>
                </div>
                <div class="cumulative">
                    <h4>累计入园人数</h4>
                    <numData :datall = 'usercount.total' :cl='data_all'></numData>
                </div>
            </div>
        </div>
        <div class="centerMap">
            <!-- baidu-map class="map" :center="center" :zoom="zoom" @ready="handler"></baidu-map -->
            <!-- baidu-map class="map" :center="{lng: 116.404, lat: 39.915}" :zoom="14" :theme="darkStyle">
                <bml-heatmap :data="relitu" :max="100" :radius="20"></bml-heatmap>
            </baidu-map -->
            
            <baidu-map class="map" :center="{lng: 105.000, lat: 38.000}" :zoom="4" :theme="mapStyle" @ready="addPoints">
                <bm-point-collection :points="points" shape="BMAP_POINT_SHAPE_CIRCLE" color="rgba(255,255,255,0.6)" size="BMAP_POINT_SIZE_SMALL" @click="clickHandler"></bm-point-collection>
            </baidu-map>
        </div>
        <div class="centerbottom">
            <div class="numGarden">
                <div class="real">今日上网人数: {{usercount.portal_today}}</div>
                <div class="cumulative">累计上网人数: {{usercount.portal_total}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import {BmlHeatmap} from 'vue-baidu-map'
import numData from './num.vue'
export default {
    components: {
        BmlHeatmap,
        numData
    },
    computed: {
        usercount () {
            return this.$store.state.usercount;
        }
    },
    data () {
        return {
            data_now:'data_now',
            data_all:'data_all',
            mapStyle: [
                    {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {
                              "color": "#063856"
                    }
                    },
                    {
                    "featureType": "land",
                    "elementType": "all",
                    "stylers": {
                              "color": "#085da5",
                              "hue": "#0d80e1"
                    }
                    },
                     {
                    "featureType": "boundary",
                    "elementType": "geometry",
                    "stylers": {
                              "color": "#207dde"
                    }
                    },
                    // {"featureType": "water",
                    // "elementType": "all",
                    // "stylers": {
                    //           "color": "#167f70"
                    // }
                    // },
                    // {
                    // "featureType": "land",
                    // "elementType": "all",
                    // "stylers": {
                    //           "color": "#0ca58f"
                    // }
                    // },
                    // {
                    // "featureType": "boundary",
                    // "elementType": "geometry",
                    // "stylers": {
                    //           "color": "#167f70"
                    // }
                    // },
                    
                    {
                    "featureType": "label",
                    "elementType": "labels",
                    "stylers": {
                              "color": "#17acea",
                              "visibility": "off"
                    }
                    },
                    {
                    "featureType": "manmade",
                    "elementType": "all",
                    "stylers": {
                              "color": "#3d85c6",
                              "visibility": "on"
                    }
                    },
                    {
                    "featureType": "building",
                    "elementType": "all",
                    "stylers": {
                              "color": "#3d85c6"
                    }
                    },
                    {
                    "featureType": "green",
                    "elementType": "all",
                    "stylers": {
                              "color": "#a2c4c9"
                    }
                    },
                    {
                    "featureType": "highway",
                    "elementType": "all",
                    "stylers": {
                              "color": "#cccccc",
                              "weight": "0.6"
                    }
                    },
                    {
                    "featureType": "arterial",
                    "elementType": "all",
                    "stylers": {
                              "color": "#cccccc",
                              "weight": "0.1"
                    }
                    },
                    {
                    "featureType": "local",
                    "elementType": "all",
                    "stylers": {
                              "color": "#cccccc",
                              "weight": "0.1"
                    }
                    },
                    {
                    "featureType": "boundary",
                    "elementType": "all",
                    "stylers": {}
                    }
            ],
            
            points: []
           
        }
    },
    methods: {
        clickHandler (e) {
            alert(`单击点的坐标为：${e.point.lng}, ${e.point.lat}`);
        },
        update (e) {
            this.curveline = e.target.cornerPoints
        },
        addPoints () {
            const points = [];
            for (var i = 0; i < 50; i++) {
                const position = {lng: Math.random() * 40 + 85, lat: Math.random() * 30 + 21}
                points.push(position)
            }
            this.points = points
        },
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
                //var cur=start+dis*n/count;
                
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
        num(data){
            var oImg=document.getElementsByTagName("img")
            var data = data
            var num = data.toString().length
            var dd = this.buwei(num)+data.toString()
            for(var i=0;i<oImg.length;i++){
                this.move(oImg[i],{"marginTop":-35*dd.charAt(i)});
            }
        }
    },
    mounted(){
        this.$http.get('/json/num').then(response => {
                this.data = response.data['num_now']
                this.datall = response.data['num_all']
            }, response => {
                //alert('读取远程资源失败')
            })
    }
}
</script>
<style>
    .centerMap{
        height:100%;
    }
    .map {
        width:92%;
        height:103%;
        margin:auto;
    }
     .centerTitle{
        position: absolute;
        top:30px;
        width: 98%;
        letter-spacing: 2px;
        z-index: 2;
    }
    .numGarden li{
        border-radius:0px;
    }
    .numGarden{
        width:60%;
        margin:auto;
        overflow:hidden;
    }
    .numGarden .real{
        float:left;
    }
    .numGarden .cumulative{
        float:right;
    }
    .numGarden div{
        width:40%;
        padding:0 5px;
    }
    .centerTitle h4{
        width:100%;
        padding:5px 0;  
    }
    .centerTitle h2{
        font-size:2.3vw;
    }
    h1,h2,h3,h4{
        margin:0px;
    }
    .centerbottom{
        color:#fff;
        font-size:1.2vw;
        position:absolute;
        bottom:30px;
        width:100%;
    }
    .centerbottom .numGarden{
        width:60%;
    }
     @media screen and (min-width:1280px) and (max-width:1680px){ 
        .numGarden div{
            width:45%;
        }
    } 
    @media screen and (min-width:1024px) and (max-width:1280px){ 
        .numGarden{
            width:83%;
        }
        .numGarden div{
            width:45%;
        }
    } 
</style>
