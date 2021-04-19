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
    const className = props.className ? this.props.className : 'btn btn-primary btn-sm'
        return action.type === 'like' ? <button className={className}> {tweet.likes} Likes </button> : null
}

export function Tweet(props) { // Returns list of tweets
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className='btn btn-group'>
            <ActionBtn tweet={tweet} action={{type:'like'}}/>
        </div>
    </div>
}