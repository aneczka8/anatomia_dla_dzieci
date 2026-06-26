const CACHE = 'anatomia-v2';
const ASSETS = [
  './',
  './index.html',
  './regions.js',
  './manifest.json',
  './obrazki/jpg2png/boy_front.png',
  './obrazki/jpg2png/girl_front.png',
  './obrazki/jpg2png/boy_back.png',
  './obrazki/jpg2png/girl_back.png',
  './obrazki/jpg2png/boy_head.png',
  './obrazki/jpg2png/girl_head.png',
  './dzwieki/bark.wav','./dzwieki/biodro.wav','./dzwieki/brew.wav','./dzwieki/broda.wav',
  './dzwieki/brzuch.wav','./dzwieki/czolo.wav','./dzwieki/dekolt.wav','./dzwieki/dlon.wav',
  './dzwieki/glowa.wav','./dzwieki/jezyk.wav','./dzwieki/kark.wav','./dzwieki/klatka_piersiowa.wav',
  './dzwieki/kolano.wav','./dzwieki/kostka.wav','./dzwieki/lokiec.wav','./dzwieki/lydka.wav',
  './dzwieki/moszna.wav','./dzwieki/nadgarstek.wav','./dzwieki/nos.wav','./dzwieki/oko.wav',
  './dzwieki/pachwina.wav','./dzwieki/palec.wav','./dzwieki/penis.wav','./dzwieki/pepek.wav',
  './dzwieki/pieta.wav','./dzwieki/plecy.wav','./dzwieki/policzek.wav','./dzwieki/posladek.wav',
  './dzwieki/powieka.wav','./dzwieki/przedramie.wav','./dzwieki/ramie.wav','./dzwieki/reka.wav',
  './dzwieki/rzesy.wav','./dzwieki/skron.wav','./dzwieki/srom.wav','./dzwieki/stopa.wav',
  './dzwieki/szyja.wav','./dzwieki/tulow.wav','./dzwieki/ucho.wav','./dzwieki/udo.wav',
  './dzwieki/usta.wav','./dzwieki/wlosy.wav','./dzwieki/zeby.wav',
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});

// Logika (HTML / JS / manifest) — ZAWSZE z sieci gdy online (network-first),
// żeby poprawki nigdy nie utknęły w cache. Obrazki i dźwięki — z cache (szybko, offline).
self.addEventListener('fetch', e => {
  const path = new URL(e.request.url).pathname;
  const isLogic = path.endsWith('/') || path.endsWith('index.html') ||
                  path.endsWith('regions.js') || path.endsWith('manifest.json');
  if (isLogic) {
    e.respondWith(
      fetch(e.request).then(r => {
        const copy = r.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy));
        return r;
      }).catch(() => caches.match(e.request))
    );
  } else {
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
  }
});
