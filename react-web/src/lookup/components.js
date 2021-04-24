//5h20min React tutorial
export function loadTweets(callback) {
    const xhr = new XMLHttpRequest() // requesting data as HTTP
    const method = 'GET' // "POST"
    const url = "http://localhost:8000/profile/api/tweets/"   // Goes to this url
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
      callback(xhr.response, xhr.status)
    }
    xhr.onerror = function (e) {
      console.log(e)
      callback({"message": "The request was an error"}, 400)
    }
    xhr.send()
  }