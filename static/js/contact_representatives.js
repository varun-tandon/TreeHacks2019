function send_fax(){
  //var textbox = $("#textbox").val();
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/fax",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "processData": false,
    "data": "{\n\"fax_1\": \"" + " +18665192390" + "\"\n}"
  }
  $.ajax(settings).done(function (response) {
    console.log(response);

  });
}

$( document ).ready(function() {
  let boolSend = true;
  if (true) {

  }
  $('#send_button').click(function(){
    if (boolSend){
      console.log("CLICKED");
      send_fax();
    }
    boolSend = false;
    $("#send_button").text("Sent!");
  });

});
