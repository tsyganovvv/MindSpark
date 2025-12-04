

export default function Auth(params){
  function getGoogleAuthUrl() {
    fetch('http://localhost:8000/auth/google/url', {method: 'POST'})
      .then(response => window.location = response.url);
  }
  return(
    <>
      <h1>Auth</h1>
      <a href="#" onClick={ getGoogleAuthUrl() }>Google</a>
    </>
  )
}