<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <main>
    <header>
      <div class="navbar">
        <img src="/Telekom.png" alt="" class="logo">
        <RouterLink to="/account">
          <!-- <img src="/user-solid.svg" alt="" class="people"> -->
          <i class="fa-solid fa-user people fa-2xl black"></i>
        </RouterLink>
        
      </div>
      <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

      <!-- <div class="wrapper"> -->
        <!-- <HelloWorld msg="You did it!" /> -->

        <!-- <nav> -->
          <!--  -->
          <!-- <RouterLink to="/about">About</RouterLink> -->
        <!-- </nav> -->
      <!-- </div> -->
    </header>

    <RouterView />
  </main>
</template>

<style scoped>

.navbar {
  background-color: #E10075;
  overflow: hidden;
  position: fixed;
  top: 0;
  width: 100%;
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  margin-left: 50px;
  height: 50%;
  
  /* float: left; */
  /* display: block; */
  /* margin: 0 auto 2rem; */
  /* width: 200px; */
  /* height: 100px; */
  /* padding: 0px 0px 0px 0px; */
}

.people {
  margin-right: 50px;
  height: 60%;
  color: white;
  /* float: left; */
  /* display: block; */
  /* margin: 0 auto 2rem; */
  /* width: 200px; */
  /* height: 100px; */
  /* padding: 0px 0px 0px 0px; */
}


/* header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
</style>
