<template>
  <div class="AllBody">
  	<table width="100%" cellspacing="2">
        <tr class="headTitle">
            <td colspan="3"> 
                <HeadTitle></HeadTitle>
            </td>
        </tr>
        <tr class="first">
            <td width="25%" rowspan="2" class="leftOne">
               <LeftOne @fade='Fade' ></LeftOne>
            </td>
            <td width="50%"  rowspan="3" class="centerBg">
                <CenterBg @fade='Fade'></CenterBg>
            </td>
            <td width="25%" class="rightOne" >
                  <RightOne @fade='Fade'></RightOne>
            </td>
        </tr>
        <tr class="second">
            <td width="25%" class="rightTwo list">
                <Environment></Environment>
            </td>
        </tr>
        <tr class="third">
            <td width="25%" class="leftTwo">
                <LeftTwo @fade='Fade'></LeftTwo>
            </td>
            <td width="25%" class="rightThree list">
                <RightTwo @fade='Fade'></RightTwo>
            </td>
        </tr>
	</table>
  </div>
</template>
<script type="text/babel">
import LeftOne from '../components/LeftOne.vue'
import LeftTwo from '../components/LeftTwo.vue'
import RightOne from '../components/RightOne.vue'
import RightTwo from '../components/RightTwo.vue'
import CenterBg from '../components/CenterBg.vue'
import HeadTitle from '../components/HeadTitle.vue'
import Environment from '../components/Environment.vue'
export default {
      components:{
        LeftOne,
        LeftTwo,
        RightOne,
        RightTwo,
        CenterBg,
        HeadTitle,
        Environment
      },
      methods:{
        Fade(msg) {
            var Fadeflag = true;
                var num = 10;
                if (Fadeflag) {
                    var st = setInterval(function(){
                        num--;
                        Fadeflag = false;
                        msg.style.opacity = num/10;
                        if (num<=0) {
                            clearInterval(st);
                            Fadeflag = true;
                            var num2 = 0;
                                var aa = setInterval(function(){
                                    num++;
                                    Fadeflag = false;
                                    msg.style.opacity = num/10;
                                    if (num>=10) {
                                        clearInterval(aa);
                                        Fadeflag = true;
                                    }
                                },30);
                        }
                    },30);
                }
        }
      }
}

</script>

<style scoped>
    .AllBody{
        height:100%;
    }
    table{
        height:100%;
        text-align:center;
	}
    .headTitle{
        height:1%;
    }
    .first td, .second td, .third td{
        position:relative;
        overflow:hidden;
        height:17%;
    }
    .echarts{
        position:absolute;
        top:17px;
        height:90%;
        width:100%;
    }
    .leftOne,.centerBg,.rightOne,.leftTwo,.rightTwo,.rightThree{
        background-repeat: no-repeat;
        background-size:100% 100%;
        background-repeat:no-repeat;
     }
</style>