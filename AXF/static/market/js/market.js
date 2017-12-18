$(function () {
    $('.left_child_type').click(function () {
        $('.goods_child_category').css('display', 'block');
        $('.goods_order').hide();
    })

    $('.goods_child_category').click(function () {
        $(this).hide();
    })

    $('.right_order').click(function () {
        $('.goods_order').show();
        $('.goods_child_category').hide();
    })

    $('.goods_order').click(function () {
        $(this).hide();
    })


    //修改购物车
    var $sushops = $('#subshop');
    var $addshops = $('#addshop');
    for (var i = 0; i < $addshops.length; i++) {
        addShop = $addshops[i]
        addShop.addEventListener("click", function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/0/", {"productid": pid}, function (data) {
                if (data.status == "success") {
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                } else {
                    if (data.data == -1) {
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        })
    }


    for (var i = 0; i < $sushops.length; i++) {
        subShopping = $sushops[i]
        subShopping.addEventListener("click", function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/1/", {"productid": pid}, function (data) {
                if (data.status == "success") {
                    //添加成功，把中间的span的innerHTML变成当前的数量
                    document.getElementById(pid).innerHTML = data.data
                } else {
                    if (data.data == -1) {
                        window.location.href = "http://127.0.0.1:8000/login/"
                    }
                }
            })
        })
    }
})