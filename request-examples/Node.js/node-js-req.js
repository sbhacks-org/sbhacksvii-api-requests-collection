/* 
This program shows you how to query an API in Node.js. (No Authentication)
*/
// Method 1
// The easier one
// Make sure to npm install axios!
const axios = require('axios');

axios.get('https://catfact.ninja/fact')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });

// Method 2
//The plain old Node one
const https = require('https')
const options = {
  hostname: 'catfact.ninja',
  port: 443,
  path: '/fact',
  method: 'GET'
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)

  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(error)
})

req.end()

/* 
For most requests, especially those with some kind of authentication, the API usually has a library wrapper that will make your life a lot easier 
Yelp example: https://github.com/Yelp/yelp-fusion/blob/master/fusion/node/sample.js
*/
