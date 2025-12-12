import React, { useState} from "react"

export default function Chat(params) {
  const CheackAccessToken = () =>{
    const cookies = document.cookie;
    const hasAccessToken = cookies.includes("access_token")
    return hasAccessToken
  }
  
  return(
    <>
      { CheackAccessToken() ? (
        <>
          <h1>CHAT</h1>
        </>
      ) :
        <>
          <h1>You are not authorized</h1>
          <button onClick={ ()=>location.href="/auth" }>AUTH</button>
        </>
      }
    </>
  )
};