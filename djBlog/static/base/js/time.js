function time()

    {

    var now= new Date();

    var year=now.getFullYear();

    var month=now.getMonth();

    var date=now.getDate();

    //写入相应id

    document.getElementById("time").innerHTML=+year+"年"+(month+1)+"月"+date+"日";

    }