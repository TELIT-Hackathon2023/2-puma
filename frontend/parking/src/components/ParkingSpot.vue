<template>
    <div class="parking-div">
        <div class="flex">
            <div class="image-div">
                <img :src="image_path" alt="" class="image">
                <span class="text-center">A{{ id }}</span>
            </div>

            
            <!-- <span>Parking</span> -->
        </div>
    </div>
</template>

<script>
import { onMounted } from 'vue'
export default {
    props: {
        id: Number,
        color: String
    },
    data() {
        return {
            image_path: "/circle-solid-gray2.svg",

        }
    },
    mounted() {
        console.log(this.color)
        if (this.color == "occupied") {
            this.image_path = "/circle-solid-gray2.svg"
            
        }
        else if (this.color == "reserved") {
            this.image_path = "/circle-solid-orange.svg"
            // set parking div background color class


        }
        else if (this.color == "free") {
            this.image_path = "/circle-solid-purple.svg"
        }
    }

}

// on mount

// console.log(this.color)
// if (this.color == "occupied") {
//     let image_path = "/circle-solid-gray2.svg"
// }
// else if (this.color == "reserved") {
//     let image_path = "/circle-solid-orange.svg"
// }
// else if (this.color == "free") {
//     let image_path = "/circle-solid-purple.svg"
// }

// console.log(this.response[this.id-1])
// console.log(this.response)
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
    .occupied {
        background-color: rgb(217, 217, 217);
    }

    .free {
        background-color: rgb(217, 217, 217);
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