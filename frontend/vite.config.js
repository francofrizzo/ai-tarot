import { fileURLToPath, URL } from 'node:url'

import viteImagemin from 'vite-plugin-imagemin'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    process.env.NODE_ENV === 'production'
      ? viteImagemin({
          optipng: {
            optimizationLevel: 7
          },
          mozjpeg: {
            quality: 20
          },
          pngquant: {
            quality: [0.8, 0.9],
            speed: 4
          }
        })
      : null
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  base: process.env.NODE_ENV === 'production' ? '/tarot/' : '/'
})
