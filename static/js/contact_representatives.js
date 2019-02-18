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
    "data": "{\n\"fax_1\": \"" + "+18447054354" + "\"\n}"
  }
  $.ajax(settings).done(function (response) {
    console.log(response);

  });
}

function twitter_scrape_machine(){
  //var textbox = $("#textbox").val();
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "http://localhost:5000/twitter_scrape_machine",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "processData": false
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
    window.open("https://drive.google.com/file/d/1gTT9nBphwek_aDkgIv_88kX_Vrs-b-rv/view?usp=sharing", "_blank");
    boolSend = false;
    $("#send_button").text("Fax Sent!");
  });

  $('#call_graph').click(function(){
    twitter_scrape_machine();
  });

});
