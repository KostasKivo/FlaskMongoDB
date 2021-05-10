$("form[name=signup-form]").submit(function(e) {

    var $form  = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();  

    $.ajax({
        url:"/user/register",
        type:"POST",
        data: data,
        dataType:"json",
        success: function(resp) {
            console.log(resp);
            $("#error-message").hide();
            window.location.href="/account/";
        },
        error: function(resp) {
            $("#error-message").css("display", "block");
        }  
    });
    e.preventDefault();
});


$("form[name=login-form]").submit(function(e) {

    var $form  = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();  

    $.ajax({
        url:"/user/login",
        type:"POST",
        data: data,
        dataType:"json",
        success: function(resp) {
            console.log(resp);
            $("#error-message").hide(); 
            window.location.href="/account/";
        },
        error: function(resp) {
            document.getElementsByClassName('error-message').style.display = "block";
        }  
    });
    e.preventDefault();
});


// function removeSignOutButton() {
//     document.getElementById('signout-button').style.display  = 'none';
// }
