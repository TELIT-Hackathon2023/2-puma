<script setup>
import TheWelcome from '../components/TheWelcome.vue'
import LoginBox from '../components/LoginBox.vue'

// make variable logged in false
let loggedIn = false
const url = "http://localhost:8000"


// check cookie
if (document.cookie.indexOf('token') === -1) {
  console.log('no token');

  // window.location.href = '/login'
}
else {
  console.log('token');
  loggedIn = true
}


</script>

<template>
  <main>
    <!-- render if not logged in -->
    <LoginBox v-if="!loggedIn"/>
    <TheWelcome v-if="loggedIn"/>
  </main>
</template>
