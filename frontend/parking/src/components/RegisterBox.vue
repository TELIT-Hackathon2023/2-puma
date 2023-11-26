<template>
  <div class="main">
    <div class="login-box">
        <img src="/square-parking-solid.svg" class="icon" alt="">
        <h1 class="header-text">Sign Up</h1>
        <div class="login-inputs">
            <p class="input-text">First Name:</p>
            <input type="text" v-model="first_name" id="first_name" placeholder="" name="" value="" class="textbox">
            <p class="input-text">Last Name:</p>
            <input type="text" v-model="last_name" id="last_name" placeholder="" name="" value="" class="textbox">
            <p class="input-text">Phone:</p>
            <input type="text" v-model="phone" id="phone" placeholder="" name="" value="" class="textbox">
            <p class="input-text">E-mail:</p>
            <input type="text" v-model="email" id="email" placeholder="" name="" value="" class="textbox">
            <p class="input-text">Company ID:</p>
            <input type="text" v-model="company_id" id="company_id" placeholder="" name="" value="" class="textbox">
            <p class="input-text">Password:</p>
            <input type="password" v_model="password" id="password" placeholder="" name="" value="" class="textbox">
            <p class="input-text">Confirm Password:</p>
            <input type="password" v_model="password2" id="password2" placeholder="" name="" value="" class="textbox">
            <input class="btn" type="button" name="" value="Sign up" @click="signUp"> 
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
            first_name: '',
            last_name: '',
            phone: '',
            email: '',
            company_id: '',
            password: '',
            password2: ''
        };
    },
    methods: {
        signUp() {
           const url = 'http://localhost:8000/register'
              const data = {
                first_name: this.first_name,
                last_name: this.last_name,
                phone: this.phone,
                email: this.email,
                company_id: this.company_id,
                password: this.password,
                license_plates: ["ECV-4562", "GHE-4325"],
                status: "admin",
              }
              if (this.password == this.password2) {
                console.log("yes")
                fetch(url, {
                    method: 'POST',
                    headers: {
                    'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    if (data.detail == "Email already registered") {
                        alert("Email already registered")
                    }
                    else {
                      {
                        // window.location.href = '/'
                      }
                    }
                    // reload
                    
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
              }
        }
    }

}
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