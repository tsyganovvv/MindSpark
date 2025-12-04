function getGoogleAuthUrl() {
  fetch('http://localhost:8000/auth/google/url', {method: 'POST'})
    .then(response => window.location = response.url);
}