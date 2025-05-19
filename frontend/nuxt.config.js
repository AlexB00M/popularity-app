// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  devServer: {
    host: "192.168.1.8", // Сюда свой ip 
    port: "3000"
  },
  css: [
    "@/assets/styles/main.css",
    '@fortawesome/fontawesome-free/css/all.min.css',
  ],
  modules: ['@pinia/nuxt', 'nuxt-icons', '@nuxt/ui', 'vue3-carousel-nuxt'],
  app: {
    head: {
      script: [
        { src: 'https://telegram.org/js/telegram-web-app.js', defer: true }
      ],
      meta: [
        {
          name: "viewport",
          content: "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"
        }
      ],
      link:[
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=SanFrancisco:wght@400;500;700&display=swap',
        }
      ]
    },
  },
})