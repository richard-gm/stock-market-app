import {backendLookup} from '../lookup'

//6h:40min
export function apiTweetCreate(newTweet, callback){ // Lookup method for POSTING new tweets
    backendLookup("POST", "/tweets/create/", callback, {content: newTweet})
}


//5h20min React tutorial
export function apiTweetList(callback) {
    backendLookup("GET", "/tweets/", callback)
}