# FastAPI Parking Application

This is a simple FastAPI application for managing user authentication, registration, and parking spot reservations. The application uses MongoDB as its database.

## Features

- User Authentication: Login and token generation using OAuth2PasswordBearer.
- User Registration: Register users with email, password, and additional details.
- Parking Spot Reservations: Create, retrieve, and delete parking spot reservations.
- MongoDB Integration: Data is stored in a MongoDB database.

## Prerequisites

- Python 3
- MongoDB installed and running locally
- Vue.js

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/TELIT-Hackathon2023/2-puma.git
   cd fastapi-parking-app
   ```
2. Install the Dependencies
    ```bash
    pip install -r requirements.txt
    ```
    Download [MongoDB Community Server](https://www.mongodb.com/try/download/community).
3. Run the application
    ```bash
    cd ./backend
    python -m uvicorn --host=0.0.0.0 --reload
    ```
    
