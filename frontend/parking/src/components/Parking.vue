<template>
    <div class="vertical-flex-box">
        <div class="horizontal-flex-box">
            <!-- <ParkingSpot v-for="spot in parkingSpots" :key="spot.id" :id="spot.id" :response="spot.response || ''" /> -->
            <ParkingSpot v-if="dataO != null" :id="1" :response="dataO"/>
            <ParkingSpot :id="2"/>
            <ParkingSpot :id="3"/>
            <ParkingSpot :id="4"/>
            <ParkingSpot :id="5"/>
        </div>
        <div class="horizontal-flex-box">
            <div class="parking-div empty top">

            </div>
            <div class="parking-div empty bottom">

            </div>
            <!-- <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/> -->
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot :id="6"/>
            <ParkingSpot :id="7"/>
            <ParkingSpot :id="8"/>
            <ParkingSpot :id="9"/>
            <ParkingSpot :id="10"/>
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot :id="11"/>
            <ParkingSpot :id="12"/>
            <ParkingSpot :id="13"/>
            <ParkingSpot :id="14"/>
            <ParkingSpot :id="15"/>
        </div>
    </div>
</template>

<script setup>
import ParkingSpot from '../components/ParkingSpot.vue'

// fetch reservations
const url = "http://localhost:8000"
let dataO = null

fetch(url + "/parking-spots/list-all", {
    method: 'GET',
    headers: {
    'Content-Type': 'application/json'
    },
    credentials: 'include'
})
.then(response => response.json())
.then(data => {
    console.log(data)
    dataO = data
    // if (data.detail == "Invalid username or password") {
    //     alert("Invalid username or password")
    // }
    // else {
    //     document.cookie = `token=${data.access_token}`
    //     window.location.href = '/'
    // }
    // reload
    
})
</script>

<style scoped>

.empty {
    background-color: white;
    height: 100%;
    border: 2px solid #E10075;
}

.top {
    border-bottom: 0px;
}

.bottom {
    border-top: 0px;
}

.vertical-flex-box {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    height: 100%;
    width: 100%;
    /* border: 2px solid #E10075; */
}

.horizontal-flex-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 0;
    margin: 0;
    /* gap: 5px; */
    column-gap: 0;
    height: 100%;
    width: 100%;
    /* border: 2px solid #E10075; */
}

.parking-div {
    width: 300px;
    height: 70%;
    /* background-color: red; */
    left: 850px;
    top: 18%;
}


</style>