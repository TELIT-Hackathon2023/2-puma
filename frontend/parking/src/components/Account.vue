<template>
    <div class="main">
      <div class="login-box">
          <img src="/square-parking-solid.svg" class="icon" alt="">
          <h1 class="header-text">Account Details</h1>
          <div class="login-inputs">
              <p class="input-text">License Plates:</p>
              <input type="text" v-model="licenses" id="licenses" placeholder="" name="" value="AA111AA, AA222AA" class="textbox">
              <input class="btn" type="button" name="" value="Back" @click="goBack"> 
              <input class="btn" type="button" name="" value="Apply" @click="getData"> 
              <input class="btn" type="button" name="" value="Logout" @click="logout"> 
          </div>
    <!--     
          <div class="textbox">
          <i class="fas fa-lock"></i>
          <input type="password" placeholder="Password" name="" value="">
          </div>
          <>
          <input class="btn" type="button" name="" value="Sign in"> -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
  data() {
    return {
      licenses: '',
    };
  },
  methods: {
    goBack() {
      window.location.href = '/';
    },
    getData() {
      const url = 'http://localhost:8000/get-user-info';
      //set license plate shit here
    },
    logout() {

      const cookies = document.cookie.split(";");

      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i];
          const eqPos = cookie.indexOf("=");
          const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
          document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
          window.location.href = '/'
      }
    }
  },
  mounted() {
    // Set the value of the input element when the component is mounted
    document.getElementById("licenses").value = "get licenses here";
  },
};
</script>
  
  <style scoped>
  
  
  
  
  .main {
    /* center */
    display: flex;
    justify-content: center;
    /* height: 100%; */
    width: 100%;
    /* height: 100vh; */
    /* width: 100vw; */
  
  }
  
  
  .login-box {
    width: 80%; /* Set a percentage width for better responsiveness */
    max-width: 480px; /* Set a maximum width to avoid it becoming too wide on larger screens */
    height: 80%;
    margin-top: 75px;
    color: white;
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 30px;
    border: 3px solid #E10075;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 50px;
    padding-bottom: 50px;
    padding-top: 20px;
  }
  
  .login-inputs {
    /* background: black */
    /* border: 1px solid black; */
    display: flex;
    flex-direction: column;
    margin-top: 0;
    width: 80%;
    height: 55%;
    display: flex;
    justify-content: center; 
  }
  
  .icon {
    width: 100px;
    padding-top: 10px;
    /* top: 100px; */
    /* height: 100px; */
    fill: #E10075;
    /* border-radius: 50%; */
    /* position: absolute; */
    /* margin: auto; */
    /* top: -50px; */
    /* left: calc(50% - 50px); */
  
  }
  
  .login-box h1 {
    /* float: left; */
    font-size: 40px;
    /* border-bottom: 6px solid #4caf50; */
    /* margin-bottom: 50px; */
    padding: 13px 0;
  }
  /* .textbox {
    width: 100%;
    overflow: hidden;
    font-size: 20px;
    padding: 8px 0;
    margin: 8px 0;
    border-bottom: 1px solid #4caf50;
  } */
  
  
  .header-text {
    display: inline-block;
    color: black;
  
    margin-top: 0px;
    margin-bottom: 0;
    font-weight: bold;
  }
  
  .input-text {
    display: inline-block;
    color: black;
    align-self: left;
    margin-bottom: 0;
  }
  
  .textbox {
    
    background: none;
    color: black;
    font-size: 20px;
    width: 100%;
    height: 50px;
    border: 2px solid #E10075;
    border-radius: 10px;
    align-self: center;
    padding-left: 10px;
    /* margin-top: 30px; */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .btn {
    align-self: center;
    height: 50px;
    width: 60%;
    background: #E10075;
    border: 2px solid #E10075;
    border-radius: 10px;
    color: white;
    padding: 5px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 30px;
    /* margin-bottom: 30px; */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: background-color 0.25s ease; /* Add a smooth transition effect */
  }
  
  .btn:hover {
  background-color: #b3045e; /* Change the background color on hover */
  }
  
  .btn:active {
  background-color: #860246; /* Change the background color when pressed */
  box-shadow: none; /* Remove the box shadow when pressed */
  }
  
  </style>