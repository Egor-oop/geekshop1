window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var target = event.target;
        console.log(target.name); // ID of basket object
        console.log(target.value); // quantity of basket object

        $.ajax({
            url: '/baskets/edit/' + target.name + '/' + target.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
    });
}
