function lookup(method, endpoint, callback, data){
    let jsonData;
    if (data){
        jsonData = JSON.stringify(data)
    }
    const xhr = new XMLHttpRequest() // requesting data as HTTP
    const url = `http://localhost:8000/profile/api${endpoint}`   // Goes to this url
    xhr.responseType = "json"
    xhr.open(method, url)
    xhr.onload = function() {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = function (e) {
        console.log(e)
        callback({"message": "The request was an error"}, 400)
    }
    xhr.send(jsonData)
}

//5h20min React tutorial
export function loadTweets(callback) {
    lookup("GET", "/tweets", callback)
  }