from datetime import datetime, timedelta
# from typing import Annotated

from fastapi import FastAPI, HTTPException, status
# import fastapi
# from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Cookie
import pymongo

import time
import hashlib
import hmac
import struct


def generate_totp(secret_key, time_step=60*60*12, digits=6):
    current_time = int(time.time()) // time_step
    time_bytes = struct.pack('>Q', current_time)
    
    hash_value = hmac.new(secret_key.encode('utf-8'), time_bytes, hashlib.sha1).digest()
    offset = hash_value[-1] & 0x0F
    dynamic_code = hash_value[offset:offset + 4]
    totp = struct.unpack('>I', dynamic_code)[0] & 0x7FFFFFFF
    totp %= 10 ** digits
    totp = f"{totp:0{digits}d}"

    return totp


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None


# class UserInDB(User):
#     hashed_password: str

SECRET_KEY = "226f7594bfca294ac2ec689a63ff01268d59ef94fba92d449d40eb32168e5c21"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*30






pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_db_client():
    app.client = pymongo.MongoClient("mongodb://localhost:27017/")
    app.database = app.client["parking"]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.client.close()






def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(email: str):
    user_dict = app.database["accounts"].find_one({"email": email})
    if user_dict:
        return user_dict


def authenticate_user(email: str, password: str):
    user = get_user(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.today() + expires_delta
    else:
        expire = datetime.today() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



async def get_current_user(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
    
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        # token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(email)
    if user is None:
        raise credentials_exception
    return user

async def get_role_info(role: str):
    role_info = app.database["roles"].find_one({"name": role})
    if role_info is None:
        raise HTTPException(status_code=400, detail="Role not found")
    return role_info


@app.get("/")
async def root():
    return {"message": "Hello World"}

class UserLogin(BaseModel):
    email: str
    password: str


@app.post("/login")
async def login(
    user: UserLogin
):



    user = authenticate_user(user.email, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

class UserRegister(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    phone: str
    company_id: int
    license_plates: list[str]
    status: str

@app.post("/register")
async def register(
    user: UserRegister
):
    user_dict = user.model_dump()
    #Check if user already exists
    print("gg", get_user(user_dict["email"]))
    if get_user(user_dict["email"]):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict["hashed_password"] = get_password_hash(user_dict["password"])
    del user_dict["password"]
    # print(user_dict)
    user_dict.update({"created_at": datetime.today()})
    user_dict.update({"_id": user_dict["email"]})
    app.database["accounts"].insert_one(user_dict)
    return {"message": "success"}


@app.post("/logout")
async def logout(
    access_token: str = Cookie()
):
    return {"message": "success"}

class UserDeleteAccount(BaseModel):
    email: str

@app.post("/account/delete")
async def delete_account(
    user: UserDeleteAccount,
    access_token: str = Cookie()
):
    authed_user = await get_current_user(access_token)
    #Check if user already exists
    # print("gg", get_user(user["email"]))
    if authed_user["email"] != user.email:
        raise HTTPException(status_code=400, detail="Cannot authorize user to this email")
    
    a = app.database["accounts"].delete_one({"email": user.email})
    if a.deleted_count == 0:
        raise HTTPException(status_code=400, detail="Email not found")
    return {"message": "success"}

class ReservationCreate(BaseModel):
    license_plate: str
    spot_id: int
    start_time: str
    # end_time: str


def get_today():
    return datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

def get_higest_id(collection: str):
    max_id = 0
    for document in app.database[collection].find({}):
        if document["_id"] > max_id:
            max_id = document["_id"]
    return max_id

@app.post("/reservation/create")
async def create_reservation(
    reservation: ReservationCreate,
    access_token: str = Cookie()
):
    # return 1
    #TODO
    #Check reservations only one day ahead and if use already has reservation
    user = await get_current_user(access_token)
    role_info = await get_role_info(user["status"])
    #Check if user already exists
    # print(user["email"])
    if not get_user(user["email"]):
        raise HTTPException(status_code=400, detail="Email not registered")
    spot_dict = app.database["spots"].find_one({"_id": reservation.spot_id})

    #Check if user has license plate
    if reservation.license_plate not in user["license_plates"]:
        raise HTTPException(status_code=400, detail="License plate not registered")
    # if app.database["reservations"].find_one({"email": user["email"]}):
        # raise HTTPException(status_code=400, detail="User already has reservation", status="failed")
    # if app.database["reservations"].find_one({"license_plate": reservation.license_plate}):
        # raise HTTPException(status_code=400, detail="License plate already has reservation", status="failed")
    #Check if spot is already reserved in time
    
    reservation.start_time = datetime.strptime(reservation.start_time, "%Y-%m-%d")
    # reservation.end_time = datetime.strptime(reservation.end_time, "%Y-%m-%d")

    # if spot_dict != None:
    for time in spot_dict["reserved_time"]:
        # print(time, "tt", reservation.start_time)
        if time == reservation.start_time:
            raise HTTPException(status_code=400, detail="Spot is already reserved")
    # if reservation.start_time in spot_dict["reserved_until"]:
        # raise HTTPException(status_code=400, detail="Spot is already reserved")
    #Check if spot is already occupied in time
    if reservation.start_time == get_today() and spot_dict["occupied"]:
        raise HTTPException(status_code=400, detail="Spot is already occupied")
    # if app.database["spots"].find_one({"_id": reservation.spot_id})["occupied"]:
        # raise HTTPException(status_code=400, detail="Spot is already occupied")
    
    # if app.database["spots"].find_one({"_id": reservation.spot_id})["reserved"]:
        # raise HTTPException(status_code=400, detail="Spot is already reserved")
    
    #Already have reservation for this day
    if app.database["reservations"].find_one({"email": user["email"], "start_time": reservation.start_time}):
        raise HTTPException(status_code=400, detail="You already have a reservation for this day")
    #Convert start_time, end_time to datetime
    print(reservation.start_time, get_today(), timedelta(days=1))
    if reservation.start_time < get_today():
        raise HTTPException(status_code=400, detail="Start time is in the past")
    
    # can only reverse cetain days in future
    if reservation.start_time - timedelta(days=role_info["days_ahead"]) > get_today():
        raise HTTPException(status_code=400, detail=f"You can only reserve a spot {role_info['days_ahead']} days ahead")
    
    #Check if user has already reserved too many spots
    if app.database["reservations"].count_documents({"email": user["email"]}) >= role_info["reservation_limit"]:
        raise HTTPException(status_code=400, detail=f"You can only reserve {role_info['reservation_limit']} spots")
    reservation_dict = reservation.model_dump()
    # del reservation_dict["access_token"]
    reservation_dict.update({"created_at": datetime.today()})
    reservation_dict.update({"email": user["email"]})
    # generate reservation id based on already existing reservations
    # reservation_dict.update({"_id": app.database["reservations"].count_documents({}) + 1})
    reservation_dict.update({"_id": get_higest_id("reservations") + 1})
    app.database["reservations"].insert_one(reservation_dict)
    #Update spot, make reserver_by and until list
    app.database["spots"].update_one({"_id": reservation.spot_id}, {"$set": {"reserved": True,
    "reserved_by": spot_dict["reserved_by"] + [user["email"]],
    "reserved_time": spot_dict["reserved_time"] + [reservation.start_time]}})
    # app.database["spots"].update_one({"_id": reservation.spot_id}, {"$set": {"reserved": True, "reserved_by": user["email"], "reserved_until": reservation.end_time}})
    return {"message": "success", "status": "success"}

# class ReservationGet(BaseModel):
    # access_token: str

#Get user reservation
@app.get("/reservation/get")
async def get_reservation(
    access_token: str = Cookie()
):
    user = await get_current_user(access_token)
    reservations = app.database["reservations"].find({"email": user["email"]})
    # reservation = app.database["reservations"].find_one({"email": user["email"]})
    # if not reservations:
        # raise HTTPException(status_code=400, detail="No reservation found")
    return list(reservations)

# class ReservationDelete(BaseModel):
    # access_token: str

class ReservationDelete(BaseModel):
    # access_token: str
    spot_id: int


@app.post("/reservation/delete")
async def delete_reservation(
    reservation: ReservationDelete,
    access_token: str = Cookie()
):
    user = await get_current_user(access_token)
    #if reservation id exists and belongs to user
    # reservation = app.database["reservations"].find_one({"email": user["email"], "_id": reservation.id})
    # if not reservation:
        # raise HTTPException(status_code=400, detail="No reservation found")
    #Update spot, make reserver_by and until list
    # app.database["spots"].update_one({"_id": reservation["spot_id"]}, {"$set": {"reserved": False,
    # "reserved_by": spot_dict["reserved_by"] + [user["email"]],
    # "reserved_time": spot_dict["reserved_time"] + [reservation.start_time]}})
    # app.database["spots"].update_one({"_id": reservation["spot_id"]}, {"$set": {"reserved": False, "reserved_by": [], "reserved_time": []}})
    # print("reservation id", reservation.spot_id, "user email", user["email"])
    reservation_info = app.database["reservations"].find_one({"email": user["email"], "spot_id": reservation.spot_id})
    if not reservation_info:
        raise HTTPException(status_code=400, detail="No reservation found")
    rr = app.database["reservations"].delete_one({"email": user["email"], "spot_id": reservation.spot_id})
    # if rr.deleted_count == 0:
        # raise HTTPException(status_code=400, detail="No reservation found")
    
    #delete reservation from spot
    reservation_spot = app.database["spots"].find_one({"_id": reservation.spot_id})
    print(reservation_spot)
    for res_spot_i, res_spot in enumerate(reservation_spot["reserved_by"]):
        if res_spot == user["email"] and reservation_spot["reserved_time"][res_spot_i] == reservation_info["start_time"]:
            #get current reserver_by and reserver_time array
            # print("popping index,",res_spot_i)
            reservation_spot["reserved_by"].pop(res_spot_i)
            reservation_spot["reserved_time"].pop(res_spot_i)
            if len(reservation_spot["reserved_by"]) == 0:
                app.database["spots"].update_one({"_id": reservation.spot_id}, {"$set": {"reserved": False, "reserved_by": reservation_spot["reserved_by"], "reserved_time": reservation_spot["reserved_time"]}})
            else:
                app.database["spots"].update_one({"_id": reservation.spot_id}, {"$set": {"reserved_by": reservation_spot["reserved_by"], "reserved_time": reservation_spot["reserved_time"]}})
    return {"message": "success"}

@app.get("/reservation/list-all")
async def list_all_reservations(access_token: str = Cookie()):

    # access_token = access_token.access_token
    await get_current_user(access_token)
    reservations = app.database["reservations"].find({})
    filtered_reservations = []
    for reservation in list(reservations):
        filtered_reservations.append({
            "spot_id": reservation["spot_id"],
            "start_time": reservation["start_time"],
            # "end_time": reservation["end_time"]
        })
    return filtered_reservations

class AccessTokenReq(BaseModel):
    access_token: str

@app.get("/generate-spots")
async def generate_spots(access_token: str = Cookie()):
    #if valid token
    # access_token = access_token.access_token
    user = await get_current_user(access_token)
    if user["status"] != "admin":
        raise HTTPException(status_code=400, detail="Not authorized")
    for i in range(1, 16):
        app.database["spots"].insert_one({
            "_id": i,
            "location": "BCT East",
            "occupied": False,
            "reserved": False,
            "occupied_by": None,
            "reserved_by": [],
            "reserved_time": []
        })
    return {"message": "success"}

@app.get("/delete-spots")
async def delete_spots(access_token: str = Cookie()):
    
    # access_token = access_token.access_token
    user = await get_current_user(access_token)
    if user["status"] != "admin":
        raise HTTPException(status_code=400, detail="Not authorized")
    app.database["spots"].delete_many({})
    return {"message": "success"}

@app.get("/generate-roles")
async def generate_roles(access_token: str = Cookie()):

    # access_token = access_token.access_token
    user = await get_current_user(access_token)
    if user["status"] != "admin":
        raise HTTPException(status_code=400, detail="Not authorized")
    
    app.database["roles"].insert_one({
        "_id": 1,
        "name": "visitor",
        "description": "visitor",
        "days_ahead": 1,
        "reservation_limit": 1

    })
    app.database["roles"].insert_one({
        "_id": 2,
        "name": "employee",
        "description": "Employee",
        "can_reserve": True,
        "days_ahead": 2,
        "reservation_limit": 2
    })
    app.database["roles"].insert_one({
        "_id": 3,
        "name": "manager",
        "description": "Manager",
        "can_reserve": True,
        "days_ahead": 7,
        "reservation_limit": 5
    })
    app.database["roles"].insert_one({
        "_id": 4,
        "name": "admin",
        "description": "Admin",
        "can_reserve": True,
        "days_ahead": 7,
        "reservation_limit": 5
    })
    return {"message": "success"}
# async def get_parking_spots():
    # return app.database["parking_spots"].find()

@app.get("/parking-spots/list-all")
async def list_all_parking_spots(access_token: str = Cookie()):
    # print(access_token)
    # access_token = access_token.access_token
    user = await get_current_user(access_token)
    #just to check if logged in ^
    parking_spots = app.database["spots"].find({})
    filtered_parking_spots = []
    for parking_spot in list(parking_spots):
        filtered_parking_spots.append({
            "id": parking_spot["_id"],
            "location": parking_spot["location"],
            "occupied": parking_spot["occupied"],
            "reserved": parking_spot["reserved"],
        })
    return filtered_parking_spots

class CheckIn(BaseModel):
    # access_token: str
    licence_plate: str

# @app.post("/verify-totp")
# async def verify_totp(access_token: str = Cookie(), totp: str = None):
    
#     user = await get_current_user(access_token)

#     #Check if user is admin
#     if user["status"] != "admin":
#         raise HTTPException(status_code=400, detail="Not authorized")
    
#     server_totp = generate_totp(SECRET_KEY)

@app.post("/check-in")
async def check_in(check_in: CheckIn, access_token: str = Cookie()):

    user = await get_current_user(access_token)
    #Check if user is admin
    if user["status"] != "admin":
        raise HTTPException(status_code=400, detail="Not authorized")
    #Check if license plate is reserved
    license_plate = check_in.licence_plate

    reservations = app.database["reservations"].find({"license_plate": license_plate})
    if not reservations:
        raise HTTPException(status_code=400, detail="No reservation found")
    #if reservation is today
    reservation_found = False
    for reservation in reservations:
        if reservation["start_time"] == get_today():
            reservation_found = True
            #delete reservation
            #find reservation with license plate
            reservation = app.database["reservations"].find_one_and_delete({"license_plate": license_plate})
            # app.database["reservations"].delete_many({"license_plate": license_plate})

            reservation_spot = app.database["spots"].find_one({"_id": reservation["spot_id"]})
            for res_spot_i, res_spot in enumerate(reservation_spot["reserved_by"]):
                if reservation_spot["reserved_time"][res_spot_i] == reservation["start_time"]:
                    #get current reserver_by and reserver_time array
                    print("popping index,",res_spot_i)
                    reservation_spot["reserved_by"].pop(res_spot_i)
                    reservation_spot["reserved_time"].pop(res_spot_i)

                    app.database["spots"].update_one({"_id": reservation["spot_id"]}, {"$set": {"reserved_by": reservation_spot["reserved_by"], "reserved_time": reservation_spot["reserved_time"]}})
            #Update spot, make reserver_by and until list
            app.database["spots"].update_one({"_id": reservation["spot_id"]}, {"$set": {"occupied": True, "occupied_by": license_plate}})

            return {"message": "success"}
    if not reservation_found:
        raise HTTPException(status_code=400, detail="No reservation found for today")
    #Check if license plate is already checked in
    # for reservation in reservations:
        # if reservation["checked_in"]:
            # raise HTTPException(status_code=400, detail="License plate already checked in")
    

class LicensePlate(BaseModel):
    # access_token: str
    license_plate: str

@app.get("/get-user-info")
async def get_user_info(access_token: str = Cookie()):
    
        # access_token = access_token.access_token
        user = await get_current_user(access_token)
        #Check if user is admin
        # if user["status"] != "admin":
            # raise HTTPException(status_code=400, detail="Not authorized")
        #Check if license plate is reserved

        return {
            "email": user["email"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "phone": user["phone"],
            "company_id": user["company_id"],
            "license_plates": user["license_plates"],
        }


@app.post("/add-license-plate")
async def add_license_plate(license_plate: LicensePlate, access_token: str = Cookie()):
    
        # access_token = license_plate.access_token
        user = await get_current_user(access_token)

        license_plate = license_plate.license_plate
        
        #Check if license plate is already checked in
        app.database["accounts"].find_one({"email": user["email"]})
        for lic in user["license_plates"]:
            if lic == license_plate:
                raise HTTPException(status_code=400, detail="License plate already registered")
        #Add license plate to user
        app.database["accounts"].update_one({"email": user["email"]}, {"$set": {"license_plates": user["license_plates"] + [license_plate]}})
        return {"message": "success"}

@app.post("/remove-license-plate")
async def remove_license_plate(license_plate: LicensePlate, access_token: str = Cookie()):
    
        # access_token = license_plate.access_token
        user = await get_current_user(access_token)

        license_plate = license_plate.license_plate
        
        found_license = False
        #Check if license plate is already checked in
        app.database["accounts"].find_one({"email": user["email"]})
        for lic in user["license_plates"]:
            if lic == license_plate:
                found_license = True
                #check if license plate is reserved
                if app.database["reservations"].find_one({"license_plate": license_plate}):
                    raise HTTPException(status_code=400, detail="Cannot remove license plate, if it's reserved")
                #check if it is used in spot rn
                if app.database["spots"].find_one({"occupied_by": license_plate}):
                    raise HTTPException(status_code=400, detail="Cannot remove license plate, if it's used in spot")
                user["license_plates"].remove(lic)

        if not found_license:
            raise HTTPException(status_code=400, detail="License plate not found")
        #Add license plate to user
        app.database["accounts"].update_one({"email": user["email"]}, {"$set": {"license_plates": user["license_plates"]}})
        return {"message": "success"}