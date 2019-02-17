function get_representative_information(){
  var rep_message = $("#rep_message").val();
  var get_zip = $
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/access_us_congress_info",
    "method": "POST",
    "headers": {
      'x-api-key': "2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c",
      'Content-Type': "application/x-www-form-urlencoded",
    },
    "processData": false,
    "data": "{\n\t\"zip_code\": \"" + zip_code + "\"\n}"
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
