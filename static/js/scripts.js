$( document ).ready(function() {
  $("#login_page_nav_button").click(function() {
    window.location.href = "/login";
  });

  $('#login_form_button').click(function(){
    console.log("CLICKED");
    login($("#loginEmailInput").val(), $("#loginPasswordInput").val());
  });

  $('#signup_page_nav_button').click(function() {
    window.location.href = "/onboarding";
  });
});

function login(email, password){
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/login",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "processData": false,
    "data": "{\n\t\"email\": \"" + email + "\",\n\t\"password\": \"" + password + "\"\n}"
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
}
