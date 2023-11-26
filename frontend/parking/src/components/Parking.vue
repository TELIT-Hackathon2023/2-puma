<template>
    <div class="vertical-flex-box">
        <div class="horizontal-flex-box">
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
            <ParkingSpot/>
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
            <ParkingSpot/>
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
            <ParkingSpot/>
        </div>
    </div>
</template>

<script setup>
import ParkingSpot from '../components/ParkingSpot.vue'
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