const CACHE_NAME = 'maliklang-v2-cache-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/manifest.json',
  '/assets/icon-192.png',
  '/assets/icon-512.png'
];

// 1. App को Mobile की memory में हमेशा के लिए Install करना
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW] Caching core genomic assets for offline mesh operation.');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// 2. पुराने Cache को साफ़ करना जब हम नया Version लाएं
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log('[SW] Clearing old buffer matrices.');
            return caches.delete(cache);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// 3. 🚨 महा-जादू: 0% Network पर भी Local Storage से App को 1 सेकंड में लाइव खोलना
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        // बिना इंटरनेट के लोकल मेमोरी से ऐप लोड करना
        return cachedResponse;
      }
      // अगर नेटवर्क उपलब्ध है, तो लाइव रेंडर सर्वर से कनेक्ट करना
      return fetch(event.request).catch(() => {
        console.log('[SW GRID] Dynamic fallback initiated due to low connectivity.');
      });
    })
  );
});
 
