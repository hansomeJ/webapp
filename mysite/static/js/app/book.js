// <!--  切换图书列表与图书添加页面  -->
$('.addbook').on('click', function () {
    // alert('添加图书'
    $('.title,.content,.addbook').toggleClass('hidden');
});
//点击书名输入框会给出提示
$('#book_name').on('click', function () {
    $('.book_name').empty().append('<h5 class="text-primary">请输入一个书名</h5>');
    $('#book_name').on('change', function () {
        var $book_name = $('#book_name').val();
        $.ajax({

            url: '/booket/book_name/',
            data: {'book_name': $book_name},
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                if (data.isempty) {
                    $('.book_name').empty().append('<h5 class="text-danger">书名不能为空！</h5>')
                } else if (data.isexists) {
                    $('.book_name').empty().append('<h5 class="text-danger">该书已经存在！</h5>')
                } else if (data.issuccess) {
                    $('.book_name').empty().append('<h5 class=text-success>该书名可以使用！</h5>');
                    $('#author').removeAttr('disabled')
                }
            }
        })
    })
});


//    点击作者输入框会给出一个提示
$('#author').on('click', function () {
    $('.author').empty().append('<h5 class="text-primary">输入该书的作者</h5>')
    $('#author').on('change', function () {
        let $auther = $('#author').val();
        $.ajax({
            url: '/booket/author/',
            data: {'author': $auther},
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                if (data.issuccess) {
                    $('.author').empty().append('<h5 class="text-success">该作者可以使用！</h5>');
                    $('#type').removeAttr('disabled')
                } else {
                    $('.author').empty().append('<h5 class="text-danger">作者不能为空！</h5>')
                }
            }

        })
    })
});
//    点击类型输入框给出提示
$('#type').on('click', function () {
    $('.type').empty().append('<h5 class="text-primary">输入该书的类型</h5>');
    $('#type').on('change', function () {
        let $type = $('#type').val();
        $.ajax({
            url: '/booket/type/',
            data: {'type': $type},
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                if (data.issuccess) {
                    $('.type').empty().append('<h5 class="text-success"> 类型输入正确！ </h5>')
                    $('#addbtn').removeAttr('disabled')
                } else {
                    $('.type').empty().append('<h5 class="text-danger"> 类型不能为空！</h5>')
                }
            }
        })
    });

});
$('#addbtn').on('click', function () {
    let $book_name = $('#book_name').val();
    let $author = $('#author').val();
    let $type = $('#type').val();
    $.ajax({
        url: '/booket/add/',
        data: {'book_name': $book_name, 'author': $author, 'type': $type},
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.issuccess) {
                $('#book_name,#author,#type').empty();
                $('#author,#type,#addbtn').attr('disabled');
                $('#msg').empty().append('<h4>添加书籍成功</h4>')
            }else{
                $('#msg').empty().append('<h4>添加书籍失败</h4>')
            }
        }
    })
});

