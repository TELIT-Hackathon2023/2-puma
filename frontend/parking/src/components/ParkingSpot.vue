<template>
    <div class="parking-div">
        <div class="flex">
            <div class="image-div">
                <img src="/circle-solid-gray2.svg" alt="" class="image">
                <span class="text-center">A1</span>
            </div>

            
            <!-- <span>Parking</span> -->
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .parking-div {
        border: 2px solid #E10075;
        height: 1%;
        width: 80px;
        background-color: #d9d9d9;
        /* height: 250px; */
        /* width: 100px; */
        /* width: 50px; */
    }
    .image {
        width: 50px;
    }

    .flex {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
    .image-div {
        position: relative;
    
    }
    .text-center {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
</style>