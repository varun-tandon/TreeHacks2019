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

  $('#submit_button').click(function(){
    send_text_verification();
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
    if(JSON.parse(response).status == 200){
      sessionStorage.setItem("pass_key", JSON.parse(response).pass_key);
      window.location.href = "/homepage", true;
    }else{
      presentAlert();
    }
  });
}

async function presentAlert() {
  const alertController = document.querySelector('ion-alert-controller');
  await alertController.componentOnReady();

  const alert = await alertController.create({
    header: 'Invalid Credentials',
    message: 'Please try logging in again.',
    buttons: ['OK']
  });
  return await alert.present();
}

async function presentInvalidPhoneAlert() {
  const alertController = document.querySelector('ion-alert-controller');
  await alertController.componentOnReady();

  const alert = await alertController.create({
    header: 'Invalid Phone Number',
    message: 'Please try again.',
    buttons: ['OK']
  });
  return await alert.present();
}

function send_text_verification(){
  var phone_number = $("#phone_number").val();
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/send_sms_to_user",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "processData": false,
    "data": "{\n\t\"phone_number\": \"" + phone_number + "\"\n}"
  }
  $.ajax(settings).done(function (response) {
    console.log(response);
    if(JSON.parse(response).status == 200){
      $(".hidden_pre_text").removeAttr("hidden");
    }else{
      presentInvalidPhoneAlert();
    }
  });
}
