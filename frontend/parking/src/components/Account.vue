<template>
    <div class="main">
      <div class="login-box">
          <img src="/square-parking-solid.svg" class="icon" alt="">
          <h1 class="header-text">Account Details</h1>
          <div class="login-inputs">  
              <p class="header-text">License Plates:</p>
              <div v-for="(license, index) in licenses" :key="index">
              <div class="license-entry">
                <p class="input-text">{{ license }}</p>
                <input class="btn2" type="button" name="" value="Remove" @click="removeLicense(license, index)">
              </div>
              <div class="separator"></div>
              </div>
              <!-- <input type="text" v-model="licenses" id="licenses" placeholder="" name="" :value="licences" class="textbox"> -->
              <input class="btn" type="button" name="" value="Add License" @click="addLicense"> 
              <input class="btn" type="button" name="" value="Back" @click="goBack"> 
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
      licenses: [],
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
    },
    removeLicense(license, index) {
           const url = 'http://localhost:8000/remove-license-plate'
              const data = {
                license_plate: license
                }
                fetch(url, {
                    method: 'POST',
                    headers: {
                    'Content-Type': 'application/json'
                    },
                    credentials: 'include',
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                  if (data["message"] == "success") {
                    console.log(data)
                    this.licenses.pop(index)  
                  }
                  else {
                    alert(data["detail"])
                  }
                  // window.location.href = '/'                  
      
                })
                .catch((error) => {
                    alert("Server is probably not runnning")
                    console.error('Error:', error);
                });

        },
        addLicense() {
          let plate = window.prompt("Enter License Plate", "xxx...")
          const url = 'http://localhost:8000/add-license-plate'
              const data = {
                license_plate: plate
                }
                fetch(url, {
                    method: 'POST',
                    headers: {
                    'Content-Type': 'application/json'
                    },
                    credentials: 'include',
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                  if (data["message"] == "success") {
                    console.log(data)
                    this.licenses.push(plate)  
                  }
                  else {
                    alert(data["detail"])
                  }
                  // window.location.href = '/'                  
      
                })
                .catch((error) => {
                    alert("Server is probably not runnning")
                    console.error('Error:', error);
                });
        }
  },
  mounted() {
    console.log("mounted")
    const url = "http://localhost:8000/get-user-info"
    let _data = null
    fetch(url, {
        method: 'GET',
        headers: {
        'Content-Type': 'application/json'
        },
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        _data = data
        // console.log(data["license_plates"])        
        this.licenses = data["license_plates"]
        console.log(this.licenses)
        // document.getElementById("licenses").value = data["license_plates"];
    })

    // document.getElementById("licenses").value = data[0];
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
  .license-entry {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0px;
  }
  

  .separator {
    width: 100%;
    height: 3px;
    background-color: #E10075;
    margin-top: 10px;
    margin-bottom: 10px;
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

  .btn2 {
    align-self: right;
    height: 50px;
    width: 30%;
    background: #E10075;
    border: 2px solid #E10075;
    border-radius: 10px;
    color: white;
    padding: 5px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 10px;
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