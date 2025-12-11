export default function Auth(params){
  async function GetGoogleAuthUrl(e) {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/auth/google/url', {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
        },
      });
      if (!response.ok){
        throw new Error('Failed to get Google URL');
      }
      const data = await response.json();
      window.location.href = data.url;
    } catch (error){
      console.error('Error:', error);
    }
  };
  return(
    <>
      <h1>Auth</h1>
      <a href="#" onClick={ GetGoogleAuthUrl }>Google</a>
    </>
  )
}