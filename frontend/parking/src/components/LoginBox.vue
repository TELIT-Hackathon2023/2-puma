<template>
    <div class="main">
    <div class="login-box">
        <img src="/square-parking-solid.svg" class="icon" alt="">
        <h1 class="header-text">Sign In</h1>
        <div class="login-inputs">
            <p class="input-text">Email:</p>
            <input type="text" v-model="email" id="email" placeholder="" name="" value="" class="textbox">
            <p class="input-text">Password:</p>
<<<<<<< Updated upstream
            <input type="password" v-model="password" id="password" placeholder="" name="" value="" class="textbox">
            <input class="btn" type="button" name="" value="Sign-in" @click="signIn"> 
        </div>
        <router-link to="/register" style="color: #E10075;">Don't have an account?</router-link>
=======
            <input type="password" id="password" placeholder="" name="" value="" class="textbox">
            <input class="btn" type="button" name="" value="Login"> 
        </div>
        <router-link to="/register">Don't have an account?</router-link>
>>>>>>> Stashed changes
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
            email: '',
            password: ''
        };
    },
    methods: {
        signIn() {
           const url = 'http://localhost:8000/login'
              const data = {
                email: this.email,
                password: this.password
              }
                fetch(url, {
                    method: 'POST',
                    headers: {
                    'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    if (data.detail == "Invalid username or password") {
                        alert("Invalid username or password")
                    }
                    else {
                        document.cookie = `access_token=${data.access_token}`
                        window.location.href = '/'
                    }
                    // reload
                    
                })
                .catch((error) => {
                    alert("Server is probably not runnning")
                    console.error('Error:', error);
                });

        }
    }

}
</script>

<style scoped>

.main {
    /* center */
    display: flex;
    justify-content: center;
    /* padding-top: 75px; */
    /* align-items: center; */
    /* margin-top: 100px; */
    /* background-color: #E10075; */
    /* height: 100vh; */
    /* width: 100vw; */

}


.login-box {
    /* width: 280px; */
    /* position: absolute; */
    /* padding-top: 250px; */
    width: 480px;
    height: 550px;
    margin-top: 75px;
    /* padding-top: 200px; */
    /* top: 55%; */
    /* left: 50%; */
    /* transform: translate(-50%,-50%); */
    color: white;
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 30px;
    border: 3px solid #E10075;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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
    position: absolute;
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

    margin-top: 130px;
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
    height: 60px;
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

@media screen and (max-width: 768px) {
  .main {
    padding: 20px; /* Add padding to the main container for better spacing on smaller screens */
  }

  .login-box {
    width: 100%; /* Make the login box full width on smaller screens */
    margin-top: 0; /* Remove top margin */
  }

  .login-inputs {
    margin-top: 20px; /* Adjust the top margin for the input container */
  }

  .icon {
    width: 100px; /* Adjust the width of the icon for smaller screens */
    padding-top: 20px; /* Adjust the top padding of the icon */
  }

  .textbox {
    font-size: 16px; /* Adjust the font size of the textboxes for smaller screens */
    height: 50px; /* Adjust the height of the textboxes */
  }

  .btn {
    height: 40px; /* Adjust the height of the button for smaller screens */
    margin-top: 20px; /* Adjust the top margin of the button */
  }
}

</style>