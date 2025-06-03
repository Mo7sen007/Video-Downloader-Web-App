self.addEventListener('install', event => {
  console.log('Service worker installing...');
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  console.log('Service worker activated.');
});

self.addEventListener('fetch', event => {
  // Offline caching can be added here if needed
});
