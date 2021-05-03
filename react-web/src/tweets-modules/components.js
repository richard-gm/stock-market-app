import React, {useEffect, useState}  from 'react'

import {TweetCreate} from './create'
import {Tweet} from "./detail"
import {apiTweetDetail} from "./lookup"
import {TweetsList} from './list'

export function TweetsComponent(props) {
        const [newTweets, setNewTweets] = useState([])
        const canTweet = props.canTweet === "false" ? false : true
        const handleNewTweet = (newTweet) =>{
            let tempNewTweets = [...newTweets]
            tempNewTweets.unshift(newTweet)
            setNewTweets(tempNewTweets)
        }
    return <div className={props.className}>
        {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-12 mb-3' />}
        <TweetsList newTweets={newTweets} {...props} />
    </div>
}

export function TweetDetailComponent(props){
    const {tweetId} = props
    const [didLookup, setDidLookup] = useState(false) // setting up the state of the tweet
    const [tweet, setTweet] = useState(null)
    const handleBackendLookup = (response, status)=> {
         if (status === 200){
             setTweet(response)
         } else {
             alert("There was an error! No tweet found")
             console.log(response)
         }
    }
    useEffect(()=>{
        if (didLookup === false){
            apiTweetDetail(tweetId, handleBackendLookup)
            setDidLookup(true)
        }
    }, [tweetId, didLookup, setDidLookup]) // arguments that the use effect function will use

    return tweet === null ? null : <Tweet tweet={tweet} className={props.className} />
}
