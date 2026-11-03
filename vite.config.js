import { fileURLToPath } from 'node:url';
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/static/dist/',
  plugins: [react()],
  build: {
    outDir: 'static/dist',
    emptyOutDir: true,
    assetsDir: 'assets',
    rollupOptions: {
      input: {
        home: fileURLToPath(new URL('./frontend/src/home.jsx', import.meta.url)),
        about: fileURLToPath(new URL('./frontend/src/about.jsx', import.meta.url))
      },
      output: {
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name][extname]'
      }
    }
  }
});
