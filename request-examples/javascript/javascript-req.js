// XMLHttpRequest API Request
// Good choice for vanilla JavaScript projects
let request = new XMLHttpRequest();
    request.open("GET", "https://catfact.ninja/facts");
    request.send();
    request.onload = () => {
        if (request.status === 200) {
            // by default the response comes in the string format, we need to parse the data into JSON
            console.log("XMLHttpRequest API");
            console.log(JSON.parse(request.response));
        } else {
            console.log(`error ${request.status} ${request.statusText}`);
        }
    };

// JQuery API Request
// Good choice for JavaScript projects
$.ajax({
  url: "https://catfact.ninja/fact",
  type: "GET",
  success: function(result) {
    console.log("JQuery API Request");
    console.log(result);
  },
  error: function(error) {
    console.log(error);
  }
});

//Fetch API Request
fetch('https://catfact.ninja/fact')
  .then(response => {
    console.log("Fetch API Request");
    return response.json();
  })
  .then(data => console.log(data));

// Async API Request
async function getLitCatFact() {
  let response = await fetch(
    "https://catfact.ninja/fact"
  );
  let data = await response.json();
  console.log("Async API Request");
  return data;
}
getLitCatFact().then(data => console.log(data));

// Axios API Request
// A good choice for Node.js or React projects
// Since you can just do npm install axios or yarn add axios
axios
  .get("https://catfact.ninja/fact")
  .then(response => {
    console.log("Axios API Request");
    console.log(response.data);
  })
  .catch(error => console.error(error));

/* 
Note that many APIs do not allow you do call their APIs with a key through JavaScript because it is insecure, which is why there are no examples here.
If you are using an API that needs a key, you should set up a backend, or do some searching to see if it is possible to do it in plain JavaScript.
*/