import React, {useEffect, useState} from "react"; // run HTTP request from the backend
import logo from './logo.svg';
import './App.css';
//5h20min React tutorial
function loadTweets(callback) {
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

function ActionBtn(props) {
    const {tweet, action} = props
    const className = props.className ? this.props.className : 'btn btn-primary btn-sm'
        return action.type === 'like' ? <button className={className}> {tweet.likes} Likes </button> : null
}

function Tweet(props) { // Returns list of tweets
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className='btn btn-group'>
            <ActionBtn tweet={tweet} action={{type:'like'}}/>
        </div>
    </div>
}


function App() {
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
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {tweets.map((item, index)=>{
            return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`} />
          })}
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
