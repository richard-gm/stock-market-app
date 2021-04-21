import React, {useEffect, useState} from "react"

import {loadTweets} from "../lookup";


export function TweetList (props){
      const [tweets, setTweets] = useState([])
  useEffect(() => {
    const myCallback = (response, status) => {
      console.log(response, status)
      if (status === 200){
        setTweets(response)
      } else {
        alert("There was an error")
      }
    }
    loadTweets(myCallback)
  }, [])
    return tweets.map((item, index)=>{
            return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`} />
          })
}

export function ActionBtn(props) {
    const {tweet, action} = props
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'action'
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === 'like'){
            if (userLike === true){ // if user liked the post, remove it
                setLikes(likes - 1)
                setUserLike(false)
            } else {
                setLikes(tweet.likes+1)
                setUserLike(true)
            }
        }
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
        return <button className={className} onClick={handleClick}> {display} </button>
}

export function Tweet(props) { // Returns list of tweets
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className='btn btn-group'>
            <ActionBtn tweet={tweet} action={{type:'like', display:'Likes'}}/>
            <ActionBtn tweet={tweet} action={{type:'unlike', display:'Unlikes'}}/>
            <ActionBtn tweet={tweet} action={{type:'retweet', display:'Retweet'}}/>


        </div>
    </div>
}