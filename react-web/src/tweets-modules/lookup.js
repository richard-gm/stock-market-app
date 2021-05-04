import {backendLookup} from '../lookup'

//6h:40min
export function apiTweetCreate(newTweet, callback){ // Lookup method for POSTING new tweets
    backendLookup("POST", "/tweets/create/", callback, {content: newTweet})
}
//7h10min
export function apiTweetAction(tweetId, action, callback){ // Lookup method for POSTING new tweets
    const data = {id: tweetId, action: action}
    backendLookup("POST", "/tweets/action/", callback, data)
}

//7h:40min
export function apiTweetDetail(tweetId, callback) {
    backendLookup("GET", `/tweets/${tweetId}/`, callback)
}

//5h20min React tutorial
export function  apiTweetList(username, callback, nextUrl) {
    let endpoint =  "/tweets/"
    if (username){
        endpoint =  `/tweets/?username=${username}`
    }
    if (nextUrl !== null && nextUrl !== undefined){
        endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    backendLookup("GET", endpoint, callback)
}