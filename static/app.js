$("#ledon").click(function(e){
    $.post("/ledapi", {"state":"on"})
        .done(function(string) {
            $("#ledoff").prop("disabled", false);
            $("#ledon").prop("disabled", true);
        });
    e.preventDefault();
});

$("#ledoff").click(function(e){
    $.post("/ledapi", {"state":"off"})
        .done(function(string) {
            $("#ledoff").prop("disabled", true);
            $("#ledon").prop("disabled", false);
        });
    e.preventDefault();
});

$.get( "ledapi", function(data) {
  if (data === "on") {
      $("#ledoff").prop("disabled", false);
  }
  else {
      $("#ledon").prop("disabled", false);
  }
});