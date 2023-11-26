<template>
    <div class="vertical-flex-box" v-if="data !== null">
        <div class="horizontal-flex-box">
            <!-- <ParkingSpot v-for="spot in data" :key="spot.id" :id="spot.id"/> -->
            <!-- ParkingSp -->
            <ParkingSpot :id="1" :data="data" :licences="licences"/>
            <ParkingSpot :id="2" :data="data" :licences="licences"/>
            <ParkingSpot :id="3" :data="data" :licences="licences"/>
            <ParkingSpot :id="4" :data="data" :licences="licences"/>
            <ParkingSpot :id="5" :data="data" :licences="licences"/>
        </div>
        <div class="horizontal-flex-box">
            <div class="parking-div empty top">

            </div>
            <div class="parking-div empty bottom">

            </div>
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot :id="6" :data="data" :licences="licences"/>
            <ParkingSpot :id="7" :data="data" :licences="licences"/>
            <ParkingSpot :id="8" :data="data" :licences="licences"/>
            <ParkingSpot :id="9" :data="data" :licences="licences"/>
            <ParkingSpot :id="10" :data="data" :licences="licences"/>
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot :id="11" :data="data" :licences="licences"/>
            <ParkingSpot :id="12" :data="data" :licences="licences"/>
            <ParkingSpot :id="13" :data="data" :licences="licences"/>
            <ParkingSpot :id="14" :data="data" :licences="licences"/>
            <ParkingSpot :id="15" :data="data" :licences="licences"/>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref} from 'vue'
import ParkingSpot from '../components/ParkingSpot.vue'

let data = ref(null);
let licences = ref(null);
const fetchData = () => {
  const url = 'http://localhost:8000';

  fetch(url + '/parking-spots/list-all', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  })
    .then((response) => response.json())
    .then((rdata) => {
      console.log(rdata);
      // Update the reactive data
      data.value = rdata;
    });

};

onMounted(() =>{
    fetchData();
  setInterval(fetchData, 3000); // Adjust the interval as needed
  fetch('http://localhost:8000' + '/get-user-info', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      })
        .then((response) => response.json())
        .then((rdata) => {

          // Update the reactive data
          licences.value = rdata["license_plates"];
          console.log("Llll", licences.value);
        });
});

// fetch reservations
</script>

<style scoped>

.empty {
    /* background-color: white; */
    height: 100%;
    /* border: 2px solid #E10075; */
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