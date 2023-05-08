import '@/assets/main.css'

import { createApp } from 'vue'
import App from '@/App.vue'

createApp(App).mount('#app')

// To make the app take up the full height of the screen
// See: https://ilxanlar.medium.com/you-shouldnt-rely-on-css-100vh-and-here-s-why-1b4721e74487
function calculateVh() {
  var vh = window.innerHeight * 0.01
  document.documentElement.style.setProperty('--vh', vh + 'px')
}

// Initial calculation
calculateVh()

// Re-calculate on resize
window.addEventListener('resize', calculateVh)

// Re-calculate on device orientation change
window.addEventListener('orientationchange', calculateVh)
