
$(document).ready(function(){
    $("#Genre-filter").on('click',function(){
        var x = this.value;
        console.log('You selected: ', x);
        $.ajax({
            url:"/filter",
            data:{
                x:x
            },
            datatype:'json',
          
            success:function(res){
                console.log("success");
                $("#unique").html(res.data)
            }
        });
    });
});





