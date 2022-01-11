<template>
  <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
    <div class="mt-8 bg-white overflow-hidden shadow sm:rounded-lg p-6">
      <input type="text"
             class="flex-1 appearance-none border border-gray-300 w-full my-2 py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
             placeholder="Логин"
             v-model="form.login"
      />

      <input type="password"
             class="flex-1 appearance-none border border-gray-300 w-full my-2 py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
             placeholder="Пароль"
             v-model="form.password"
      />
      <p>{{ form.login }}</p>
      <p>{{ form.password }}</p>
      <b-button @click="login">отправить</b-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        login: '',
        password: '',
      }
    }
  },
  // methods: {
  //   login() {
  //     return this.$auth.loginWith('refresh',
  //       {
  //         data: {
  //           email: form.login,
  //           password: form.password
  //         }
  //       }
  //     )
  //       .then(() => console.log(login))
  //   }
  // }
}
</script>
