<template>
    <div class="parking-div">
        <div class="flex">
            <div class="image-div">
                <img :src="image_path" alt="" class="image">
                <span class="text-center">A{{ id }} </span>
                
            </div>
            <button @click="showCalendar" class="reserver-button">Reserve</button>
            
            <!-- <span>Parking</span> -->
        </div>

        <div v-if="showPopup" class="calendar-popup">
            <h1>Calendar</h1>
                <VDatePicker v-model="selectedDate" color="pink" />
                <input type="text" class="license-plate">
            <span @click="reserveSpot">Confirm Reservation</span>
            <span @click="closeCalendar">Cancel</span>
        </div>
    </div>
</template>

<script>
import { onMounted, ref } from 'vue'
// import { watch } from 'vue'

// let showPopup = ref(false);



export default {
    props: {
        id: Number,
        color: String,
        data: Object
    },
    data() {
        return {
            image_path: "/circle-solid-gray2.svg",
            showPopup: false,
            selectedDate: null,
            // showPopup

        }
    },
    methods: {
        updateImagePath() {
        // console.log(this.data)
        // Update the image_path based on the color prop
        if (this.data) {
            // console.log(this.data[this.id-1])
            if (this.data[this.id-1]["occupied"]) {
                this.image_path = "/circle-solid-gray2.svg"
            } else if (this.data[this.id-1]["reserved"]) {
                this.image_path = "/circle-solid-orange.svg"
            } else if (!this.data[this.id-1]["occupied"] && !this.data[this.id-1]["reserved"]) {
                this.image_path = "/circle-solid-purple.svg"
            }
        };
        },
        showCalendar() {
            console.log('showing calendar');
            this.showPopup = true;
        },

        closeCalendar () {
            console.log('closing calendar');
            this.showPopup = false;
        },

        reserveSpot() {
      if (this.selectedDate) {
        // Perform the reservation logic here
        // Send a request with selected date and time
        // const reservationDateTime = `${this.selectedDate}`;
        const licensePlate = document.querySelector('.license-plate').value;
        console.log(`Spot reserved for: ${this.selectedDate} with license plate: ${licensePlate}`);
        const formattedStartTime =
        this.selectedDate.getFullYear() +
        '-' +
        (this.selectedDate.getMonth() + 1).toString().padStart(2, '0') +
        '-' +
        this.selectedDate.getDate().toString().padStart(2, '0');

        console.log(formattedStartTime)
        let url = 'http://localhost:8000'
        // TODO: Send a request to your server with the reservationDateTime
        // Example using fetch:
        fetch(url + '/reservation/create', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            spot_id: this.id,
            license_plate: licensePlate,
            start_time: formattedStartTime
          }),
          credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
        //   console.log('Reservation successful:', data);
            alert(data['detail'])
          // Update your data or perform any additional actions
        })
        .catch(error => {
          console.error('Error making reservation:', error);
        });

        this.closeCalendar();
      } else {
        // Show an error or prompt the user to select a date and time
        console.error('Please select a date and time for the reservation.');
      }
    },
        // if (color === "occupied") {
            // this.image_path = "/circle-solid-gray2.svg"
        // } else if (color === "reserved") {
            // this.image_path = "/circle-solid-orange.svg"
        // } else if (color === "free") {
            // this.image_path = "/circle-solid-purple.svg"
        // }
        // }
    },
    mounted() {
        this.updateImagePath(this.color)
        setInterval(this.updateImagePath, 500);
        // let showPopup = ref(false);
        // setInterval(console.log(this.data), 1000);
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
        position: relative
    }

    .reserver-button {
        position: absolute;
        bottom: 5px;
        right: 5px;
        width: 30%;
        height: 30%;
        background-color: #E10075;
        color: white;
        border: none;
        border-radius:10px;
        font-size: 15px;
        font-weight: bold;
        cursor: pointer;
    }

    .reserver-button:hover {
        background-color: #db0473c7;
    }
    .image-div {
        position: relative;
    
    }
    .text-center {
        position: absolute;
        top: 50%;
        left: 50%;
        color: white;
        transform: translate(-50%, -57%);
    }

    .calendar-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        z-index: 1000;
        display:flex;
        width: 350px;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }

    .calendar-popup h1 {
        font-size: 1.5em;
        margin-bottom: 15px;
    }

    .calendar-popup span {
        display: inline-block;
        padding: 8px 16px;
        background-color: #E10075;
        color: white;
        margin-right: 10px;
        cursor: pointer;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
    }

    .calendar-popup span:hover {
        background-color: #db0473c7;
    }

    .license-plate {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
  }

</style>