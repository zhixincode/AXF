   $(fu$(function () {
            $('#username').change(function () {
                var uname = $('#username').val();
                var upass = $('#password').val();
                var url = 'http://127.0.0.1:8001/axf/logincheck';
                $.get(url, {'username': uname, 'password': upass}, function (result) {
                    if (result.status === 'userNotExist') {
                        alert('该用户不存在 ，请确认后重新输入或注册');
                        window.location=('/axf/login')
                    }
                })
                $('#password').change(function () {
                    var uname = $('#username').val();
                    var upass = $(this).val();
                    var url = 'http://127.0.0.1:8001/axf/logincheck';
                    $.get(url, {'username': uname, 'password': upass}, function (result) {
                        if (result.status === 'pwdError') {
                            alert('密码错误，请重新输入');
                            window.location.href='http://127.0.0.1:8001/axf/login/'
                        }

                    })
                })
            })
        })