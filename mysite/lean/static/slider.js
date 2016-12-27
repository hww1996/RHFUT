window.onload=function ()
{
    var oDiv1=document.getElementById('main');
    var oUl=oDiv1.getElementsByTagName('ul')[0];
    var aLi=oUl.getElementsByTagName('li');
    var oSpan1=document.getElementById('span1');
    var oSpan2=document.getElementById('span2');
    var timer1=null;
    var timer2=null;
    var v=210;

    oUl.innerHTML+=oUl.innerHTML;

    for(var i=0;i<8;i++)
    {
        aLi[i].style.left=-(1920-document.body.clientWidth)/2+'px';
    }

    function down()
    {
        v=v-12;
        if(v<-18)
        {
            clearInterval(timer1);
            clearInterval(timer2);
            v=210;
        }
    }

    oSpan1.onclick=function()
    {
        timer1=setInterval(function(){
            oUl.style.left=oUl.offsetLeft+v+'px';
            if(oUl.offsetLeft>=0)
            {
                oUl.style.left=oUl.offsetLeft-7680+'px';
            }
        }, 70);
        timer2=setInterval(down,70);
    };

    oSpan2.onclick=function()
    {
        timer1=setInterval(function(){
            oUl.style.left=oUl.offsetLeft+-v+'px';
            if(oUl.offsetLeft<=-oUl.offsetWidth/2)
            {
                oUl.style.left=0+'px';
            }
        }, 70);
        timer2=setInterval(down,70);
    };
};