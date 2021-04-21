import React, {useEffect, useState} from "react"

import {loadTweets} from "../lookup";

export function TweetsComponent(props) { // Adding Text area so user can publish new posts
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault()
        const newVal = textAreaRef.current.value
        let tempNewTweets = [...newTweets]
        tempNewTweets.unshift({ // newest post will be displayed first using the unshift method
            // push this to a server using servercall function TODO
            content: newVal,
            likes: 0,
            id: 121212
        })
        setNewTweets(tempNewTweets)
        textAreaRef.current.value = ''
    }
    return <div className={props.className}>
        <div className='col-12 mb-3'>
            <form onSubmit={handleSubmit}>
                <textarea ref={textAreaRef} required={true} className='form-control' name='tweet'>

                </textarea>
                <button type='submit' className='btn btn-primary my-3'>Tweet</button>
            </form>
        </div>
        <TweetList newTweets={newTweets}/>
    </div>
}
//6h13
export function TweetList(props) {
    const [tweetsInit, setTweetsInit] = useState([]) //Monitoring this changes
    const [tweets, setTweets] = useState([])
    useEffect(()=>{
        const finalList = [...props.newTweets].concat(tweetsInit) //
        if (finalList.length !== tweets.length){
            setTweets(finalList)
        }
    }, [props.newTweets, tweets, tweetsInit])
    useEffect(() => {
        const myCallback = (response, status) => {
            console.log(response, status) // REMOVE THIS IN THE FUTURE TODO
            if (status === 200) {
                setTweetsInit(response)
            } else {
                alert("There was an error")
            }
        }
        loadTweets(myCallback)
    }, [tweetsInit])
    return tweets.map((item, index) => { // Returing tweets items - REMOVE the key in the furute so it doest not show the ID TODO
        return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>
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
        if (action.type === 'like') {
            if (userLike === true) { // if user liked the post, remove it
                setLikes(likes - 1)
                setUserLike(false)
            } else {
                setLikes(tweet.likes + 1)
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
            <ActionBtn tweet={tweet} action={{type: 'like', display: 'Likes'}}/>
            <ActionBtn tweet={tweet} action={{type: 'unlike', display: 'Unlikes'}}/>
            <ActionBtn tweet={tweet} action={{type: 'retweet', display: 'Retweet'}}/>


        </div>
    </div>
}