$(document).ready(function() {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
    let result = data.hello;
    $("DIV#hello").text(result);
  });
});
