$( document ).ready(function() {
  $("#login_page_nav_button").click(function() {
    window.location.href = "/login";
  });

  $('#login_form_button').click(function(){
    console.log("CLICKED");
    login($("#loginEmailInput").val(), $("#loginPasswordInput").val());
  });

  $('#signup_page_nav_button').click(function() {
    document.location.href = "/onboarding";
  });

  $('#submit_phone_number').click(function(){
    send_text_verification();
  });

  $('#submit_verification_code').click(function(){
    send_verification_code_submission();
  });

});

var full_name = "";
var email = "";
var password = "";
var zipcode = 0;
var phone_number = 0;

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


/* Alerts */
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

async function presentVerifiedAlert() {
  const alertController = document.querySelector('ion-alert-controller');
  await alertController.componentOnReady();

  const alert = await alertController.create({
    header: "That's it!",
    message: "Your account is ready!",
    buttons: ['OK']
  });
  return await alert.present();
}

async function presentFailedVerificationAlert() {
  const alertController = document.querySelector('ion-alert-controller');
  await alertController.componentOnReady();

  const alert = await alertController.create({
    header: "Invalid Verification Code",
    message: "Please try again.",
    buttons: ['OK']
  });
  return await alert.present();
}

function send_text_verification(){
  phone_number = $("#phone_number").val();
  sessionStorage.setItem("phone_number", phone_number);
  // all the user data
  full_name = $("#first_name").val() + " " + $("#last_name").val();
  email = $("#email").val()

  sessionStorage.setItem("email", email);

  password = $("#password").val()
  sessionStorage.setItem("password", password);
  zipcode = $("#zipcode").val()

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
    if(JSON.parse(response).status == 200){
      document.location.href = "/verify_code_page"
    }else{
      presentInvalidPhoneAlert();
    }
  });
}

function send_verification_code_submission(){
  var verification_code = $('#verification_code_submit_input').val();
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/verify_user",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "processData": false,
    "data": "{\n\t\"phone_number\": \"" + sessionStorage.getItem("phone_number") + "\",\n\t\"verification_code\": \"" + verification_code + "\"\n}"
  }
  $.ajax(settings).done(function (response) {
    if(JSON.parse(response).status == 200){
      register_user(sessionStorage.getItem("email"), sessionStorage.getItem("password"));
      presentVerifiedAlert();
      document.location.href = "/homepage";
    }else{
      presentFailedVerificationAlert();
    }
  });
}



function register_user(email, password){
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/create_user",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "processData": false,
    "data": "{\n\t\"email\": \""+ email + "\",\n\t\"password\": \"" + password + "\"\n\}"
  }
  $.ajax(settings).done(function (response) {
    console.log(response)
    //document.location.href = "/verify_code_page";
  });
}
