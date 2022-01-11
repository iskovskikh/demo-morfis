export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'app',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''},
      {name: 'format-detection', content: 'telephone=no'}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'},
      {rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css'},
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    // '@nuxtjs/auth-next',
  ],

  axios: {
    baseURL: 'http://localhost:8000/api/v1/',
  },

  // auth: {
  //   strategies: {
  //     local: {
  //       scheme: 'refresh',
  //       token: {
  //         property: 'access_token',
  //         maxAge: 1800,
  //         global: true,
  //         // type: 'Bearer'
  //       },
  //       refreshToken: {
  //         property: 'refresh_token',
  //         data: 'refresh_token',
  //         maxAge: 60 * 60 * 24 * 30
  //       },
  //       user: {
  //         property: 'user',
  //         // autoFetch: true
  //       },
  //       endpoints: {
  //         login: {url: '/api/auth/login', method: 'post'},
  //         refresh: {url: '/api/auth/refresh', method: 'post'},
  //         user: {url: '/api/auth/user', method: 'get'},
  //         logout: {url: '/api/auth/logout', method: 'post'}
  //       },
  //     }
  //   }
  // },


  publicRuntimeConfig: {
    axios: {
      browserBaseURL: process.env.BROWSER_BASE_URL
    }
  },

  privateRuntimeConfig: {
    axios: {
      baseURL: process.env.BASE_URL
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {}
}
