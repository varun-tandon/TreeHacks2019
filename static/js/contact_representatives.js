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
    window.open("http://edgepdf.rasteredge.com/RasterEdge_Cache/base/a3214e5f7d36406127741c22f7a98079/input/Fax%20Letter%20to%20Senators.pdf", "_blank");
    boolSend = false;
    $("#send_button").text("Fax Sent!");
  });

  $('#call_graph').click(function(){
    twitter_scrape_machine();
  });

});
