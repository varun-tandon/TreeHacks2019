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
    "data": "{\n\"fax_1\": \"" + " +12022240454" + "\"\n}"
  }
  $.ajax(settings).done(function (response) {
    console.log(response);

  });
}
( document ).ready(function() {

  $('#send_button').click(function(){
    console.log("CLICKED");
    send_fax();
  });

});
