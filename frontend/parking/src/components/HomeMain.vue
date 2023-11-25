<template>
  <main>
    <div class="side-bar">
        <div class="location-dropdown pink-style">
            <span>BCT-2</span>
        </div>

        <div class="legend-div pink-style">
            <div class="legend-text">
                <span>Legend</span>
            </div>
            
            <div class="availability-div">
                <div class="option-div">
                    <div class="image-div">
                        <img src="/circle-solid-gray.svg" class="circle" alt="">
                    </div>
                    <div class="text-div">
                        <span>Occupied</span>
                    </div>
                </div>
                <div class="option-div">
                    <div class="image-div">
                        <img src="/circle-solid-orange.svg" class="circle" alt="">
                    </div>
                    <div class="text-div">
                        <span>Reserved</span>
                    </div>
                </div>
                <div class="option-div">
                    <div class="image-div">
                        <img src="/circle-solid-purple.svg" class="circle" alt="">
                    </div>
                    <div class="text-div">
                        <span>Free</span>
                    </div>
                </div>
            </div>

        </div>

    </div>

    <Parking class="parking-div"/>

  </main>
</template>

<script setup>
import Parking from '../components/Parking.vue'
</script>

<style scoped>

.location-dropdown span {
    user-select: none;
}

.pink-style {
    width: 80%;
    height: 45px;
    margin:0 auto;
    border: 2px solid #E10075;
    border-radius: 10px;
}
.legend-div {
    margin-top: 50px;
    height: 180px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    /* text-align: center; */
}

.legend-text {
    /* margin-top: 50px; */
    /* height: 45px; */
    /* margin: auto; */
    /* display: flex; */
    /* flex-direction: column; */
    /* align-items: center; */
    /* justify-content: center; */
    margin-top: 10px;
    margin-bottom: 10px;
    user-select: none;
}

.option-div {
    display: flex;
    flex-direction: row;
    /* align-items: center; */
    /* justify-content: center; */
    /* gap: 10px; */
}

.image-div {
    /* margin-right: 25px; */
    /* border: 1px solid black; */
    margin-left: 45px;
    /* display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 10px; */
}

.text-div {
    /* border: 1px solid black; */
    /* margin-left: 25px; */
    text-align: center;
    width: 150px;
    user-select: none;
}

/* .legend-div span { */
    /* font-size: 20px; */
    /* font-weight: bold; */
    /* margin-bottom: 20px; */
    /* margin-top: 20px; */
/* } */

.circle {
    width: 20px;
    height: 20px;
    /* margin-right: 10px; */

}

.availability-div {
    border-top: 2px solid #E10075;
    /* margin-top: 20px; */
    display: flex;
    flex-direction: column;
    /* align-items: center; */
    justify-content: center;
    gap: 20px;
    width: 100%;
    height: 140px;
}

.location-dropdown {
    /* margin-top: 50px; */
    /* height: 45px; */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.side-bar {
    padding-top: 25px;
    background-color: rgba(255, 255, 255, 0.8);
    border-right: 2px solid #E10075;
    width: 300px;
    height: 100vh;
    position: fixed;
}
.parking-div {
    /* height: 100%; */
    position: fixed;
}
</style>