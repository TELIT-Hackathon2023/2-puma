<template>
    <div class="vertical-flex-box">
        <div class="horizontal-flex-box">
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
        </div>
        <div class="horizontal-flex-box">
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
        </div>
    </div>
</template>

<script setup>
import ParkingSpot from '../components/ParkingSpot.vue'
</script>

<style>

.vertical-flex-box {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    height: 100%;
    width: 100%;
}

.horizontal-flex-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;;
    height: 100%;
    width: 100%;
}

.parking-div {
    width: 75%;
    height: 70%;
    /* background-color: red; */
    left: 360px;
    top: 18%;
}


</style>