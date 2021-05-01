import React, {useEffect, useState} from "react"
import {apiTweetList} from "./lookup";
import {Tweet} from "./detail";

//6h13
export function TweetsList(props) {
    const [tweetsInit, setTweetsInit] = useState([]) // Monitor changes
    const [tweets, setTweets] = useState([])
    const [tweetsDidSet, setTweetsDidSet] = useState(false)
    useEffect(()=>{
        const final = [...props.newTweets].concat(tweetsInit)
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweets, tweetsInit])

    useEffect(() => {
        if (tweetsDidSet === false){
            const handleTweetListLookup = (response, status) => {
                if (status === 200){
                    setTweetsInit(response)
                    setTweetsDidSet(true)
                } else {
                    alert("There was an error")
                }
            }
            apiTweetList(props.username, handleTweetListLookup) // Null value is needed by default. will be replaced by username
        }
    }, [tweetsInit, tweetsDidSet, setTweetsDidSet, props.username])
    const handleDidRetweet = (newTweet) => {
        const updateTweetsInit = [...tweetsInit]
        updateTweetsInit.unshift(newTweet)
        setTweetsInit(updateTweetsInit)
        const updateFinalTweets = [...tweets]
        updateFinalTweets.unshift(tweets)
        setTweets(updateFinalTweets)
    }
    // Returning tweets items - REMOVE the key in the future so it doest not show the ID TODO
    return tweets.map((item, index)=>{
        return <Tweet
            tweet={item}
            didRetweet={handleDidRetweet}
            className='my-5 py-5 border bg-white text-dark'
            key={`${index}-{item.id}`} />
    })
}