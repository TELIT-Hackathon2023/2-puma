<template>
    <div class="main">
    <div class="login-box">
        <img src="/square-parking-solid.svg" class="icon" alt="">
        <h1>Login</h1>
        <!-- <i class="fas fa-user"></i> -->
        <input type="text" placeholder="" name="" value="" class="textbox">
<!--     
        <div class="textbox">
        <i class="fas fa-lock"></i>
        <input type="password" placeholder="Password" name="" value="">
        </div>
    
        <input class="btn" type="button" name="" value="Sign in"> -->
    </div>
    </div>
</template>

<script>
export default {
    


}
const url = "http://localhost:8000"

function login() {
    console.log('login')
    // get username and password
    // const email = document.getElementById('email').value
    // const password = document.getElementById('password').value
    let email = "GG2@telekom.sk"
    let password = "heslo123"
    console.log(email)
    console.log(password)
    // send request to backend
    fetch(url + '/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email: email, password: password})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        // save token in cookie
        document.cookie = 'token=' + data.token
        // redirect to home
        window.location.href = '/'
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

</script>

<style scoped>

.main {
    /* center */
    display: flex;
    justify-content: center;
    padding-top: 150px;
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
    height: 500px;
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
}

.icon {
    width: 150px;
    padding-top: 40px;
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

.textbox {
    
    background: none;
    color: white;
    font-size: 18px;
    width: 80%;
    height: 60px;
    border: 2px solid #E10075;
    border-radius: 15px;
    margin-top: 100px;
}

.btn {
    width: 100%;
    background: none;
    border: 2px solid #4caf50;
    color: white;
    padding: 5px;
    font-size: 18px;
    cursor: pointer;
    margin: 12px 0;
}



</style>