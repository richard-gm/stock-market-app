(this["webpackJsonpreact-web"]=this["webpackJsonpreact-web"]||[]).push([[0],{12:function(e,t,n){},13:function(e,t,n){},15:function(e,t,n){"use strict";n.r(t);var c=n(1),a=n.n(c),s=n(6),r=n.n(s),o=(n(12),n.p+"static/media/logo.6ce24c58.svg"),i=(n(13),n(7)),l=n(2);var j=n(0);function b(e){var t=a.a.createRef(),n=Object(c.useState)([]),s=Object(l.a)(n,2),r=s[0],o=s[1];return Object(j.jsxs)("div",{className:e.className,children:[Object(j.jsx)("div",{className:"col-12 mb-3",children:Object(j.jsxs)("form",{onSubmit:function(e){e.preventDefault();var n=t.current.value,c=Object(i.a)(r);c.unshift({content:n,likes:0,id:121212}),o(c),t.current.value=""},children:[Object(j.jsx)("textarea",{ref:t,required:!0,className:"form-control",name:"tweet"}),Object(j.jsx)("button",{type:"submit",className:"btn btn-primary my-3",children:"Tweet"})]})}),Object(j.jsx)(u,{newTweets:r})]})}function u(e){var t=Object(c.useState)([]),n=Object(l.a)(t,2),a=n[0],s=n[1],r=Object(c.useState)([]),o=Object(l.a)(r,2),b=o[0],u=o[1];return Object(c.useEffect)((function(){var t=Object(i.a)(e.newTweets).concat(a);t.length!==b.length&&u(t)}),[e.newTweets,b,a]),Object(c.useEffect)((function(){!function(e){var t=new XMLHttpRequest;t.responseType="json",t.open("GET","http://localhost:8000/profile/api/tweets/"),t.onload=function(){e(t.response,t.status)},t.onerror=function(t){console.log(t),e({message:"The request was an error"},400)},t.send()}((function(e,t){200===t?s(e):alert("There was an error")}))}),[a]),b.map((function(e,t){return Object(j.jsx)(p,{tweet:e,className:"my-5 py-5 border bg-white text-dark"},"".concat(t,"-{item.id}"))}))}function d(e){var t=e.tweet,n=e.action,a=Object(c.useState)(t.likes?t.likes:0),s=Object(l.a)(a,2),r=s[0],o=s[1],i=Object(c.useState)(!0===t.userLike),b=Object(l.a)(i,2),u=b[0],d=b[1],p=e.className?e.className:"btn btn-primary btn-sm",m=n.display?n.display:"Action",O="like"===n.type?"".concat(r," ").concat(m):m;return Object(j.jsx)("button",{className:p,onClick:function(e){e.preventDefault(),"like"===n.type&&(!0===u?(o(r-1),d(!1)):(o(r+1),d(!0)))},children:O})}function p(e){var t=e.tweet,n=e.className?e.className:"col-10 mx-auto col-md-6";return Object(j.jsxs)("div",{className:n,children:[Object(j.jsxs)("p",{children:[t.id," - ",t.content]}),Object(j.jsxs)("div",{className:"btn btn-group",children:[Object(j.jsx)(d,{tweet:t,action:{type:"like",display:"Likes"}}),Object(j.jsx)(d,{tweet:t,action:{type:"unlike",display:"Unlike"}}),Object(j.jsx)(d,{tweet:t,action:{type:"retweet",display:""}})]})]})}var m=function(){return Object(j.jsx)("div",{className:"App",children:Object(j.jsxs)("header",{className:"App-header",children:[Object(j.jsx)("img",{src:o,className:"App-logo",alt:"logo"}),Object(j.jsxs)("p",{children:["Edit ",Object(j.jsx)("code",{children:"src/App.js"})," and save to reload."]}),Object(j.jsx)("div",{children:Object(j.jsx)(b,{})}),Object(j.jsx)("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer",children:"Learn React"})]})})};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var O=document.getElementById("root");O&&r.a.render(Object(j.jsx)(m,{}),O);var h=document.getElementById("tweetme-2");h&&r.a.render(Object(j.jsx)(b,{}),h),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[15,1,2]]]);
//# sourceMappingURL=main.048635e1.chunk.js.map