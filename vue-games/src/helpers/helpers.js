export function getRandomInteger(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

export function getCSRFToken() {
  let csrfToken = null;
  const cookies = document.cookie.split(';');
  cookies.forEach(cookie => {
    if (cookie.trim().startsWith('csrftoken=')) {
      csrfToken = cookie.split('=')[1];
    }
  });
  return csrfToken;
}