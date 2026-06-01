import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: [
      'inventory-management-mskb.onrender.com',
      'inventory-management-1-nn7w.onrender.com'
    ]
  }
})
