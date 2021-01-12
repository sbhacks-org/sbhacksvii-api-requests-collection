//Your JavaScript code will go here!
window.onload = function() {
    document.getElementById("cat-fact-btn").addEventListener("click", function () {
        $.ajax({
            url: "https://catfact.ninja/fact",
            type: "GET",
            success: function(result) {
              console.log("JQuery API Request");
              console.log(result)
              document.getElementById("cat-fact-text").innerText = result.fact;
            },
            error: function(error) {
              document.getElementById("cat-fact-text").innerText = "API Request failed.";
            }
          });

        $.ajax({
            url: "https://api.thecatapi.com/v1/images/search",
            type: "GET",
            success: function(result) {
              console.log("JQuery API Request");
              console.log(result)
              if (result[0]['url']) {
                document.getElementById("cat-pic").src = result[0]['url'];
              }
            }
        });
    });
}