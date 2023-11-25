from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
import fastapi
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timezone

import pymongo


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
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
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
    user_dict.update({"created_at": datetime.utcnow()})
    user_dict.update({"_id": user_dict["email"]})
    app.database["accounts"].insert_one(user_dict)
    return {"message": "success"}


class UserDeleteAccount(BaseModel):
    email: str

@app.post("/account/delete")
async def delete_account(
    user: UserDeleteAccount
):
    a = app.database["accounts"].delete_one({"email": user.email})
    if a.deleted_count == 0:
        raise HTTPException(status_code=400, detail="Email not found")
    return {"message": "success"}

class ReservationCreate(BaseModel):
    access_token: str
    license_plate: str
    spot_id: int
    start_time: str
    end_time: str


@app.post("/reservation/create")
async def create_reservation(
    reservation: ReservationCreate
):
    #TODO
    #Check reservations only one day ahead and if use already has reservation
    user = await get_current_user(reservation.access_token)
    #Check if user already exists
    print(user["email"])
    if not get_user(user["email"]):
        raise HTTPException(status_code=400, detail="Email not registered", status="failed")
    if app.database["reservations"].find_one({"email": user["email"]}):
        raise HTTPException(status_code=400, detail="User already has reservation", status="failed")
    if app.database["reservations"].find_one({"license_plate": reservation.license_plate}):
        raise HTTPException(status_code=400, detail="License plate already has reservation", status="failed")
    if app.database["spots"].find_one({"_id": reservation.spot_id})["occupied"]:
        raise HTTPException(status_code=400, detail="Spot is already occupied", status="failed", reason="occupied")
    if app.database["spots"].find_one({"_id": reservation.spot_id})["reserved"]:
        raise HTTPException(status_code=400, detail="Spot is already reserved", status="failed", reason="reserved")
    #Convert start_time, end_time to datetime
    reservation.start_time = datetime.strptime(reservation.start_time, "%Y-%m-%d")
    reservation.end_time = datetime.strptime(reservation.end_time, "%Y-%m-%d")
    if reservation.start_time < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Start time is in the past")
    
    # if reservation is 2 days before
    if user["status"] == "employee":
        if reservation.start_time - timedelta(days=2) < datetime.utcnow():
            raise HTTPException(status_code=400, detail="You can only reserve a spot 2 days ahead")
    elif user["status"] == "manager":
        if reservation.start_time - timedelta(days=7) < datetime.utcnow():
            raise HTTPException(status_code=400, detail="You can only reserve a spot 7 days ahead")
    reservation_dict = reservation.model_dump()
    del reservation_dict["access_token"]
    reservation_dict.update({"created_at": datetime.utcnow()})
    reservation_dict.update({"email": user["email"]})
    reservation_dict.update({"_id": reservation_dict["license_plate"]})
    app.database["reservations"].insert_one(reservation_dict)
    return {"message": "success", "status": "success"}

class ReservationGet(BaseModel):
    access_token: str

#Get user reservation
@app.get("/reservation/get")
async def get_reservation(
    reservation: ReservationGet
):
    user = await get_current_user(reservation.access_token)
    reservation = app.database["reservations"].find_one({"email": user["email"]})
    if not reservation:
        raise HTTPException(status_code=400, detail="No reservation found")
    return reservation

# class ReservationDelete(BaseModel):
    # access_token: str
@app.post("/reservation/delete")
async def delete_reservation(
    reservation: ReservationGet
):
    user = await get_current_user(reservation.access_token)
    reservation = app.database["reservations"].delete_one({"email": user["email"]})
    if reservation.deleted_count == 0:
        raise HTTPException(status_code=400, detail="No reservation found")
    return {"message": "success"}

@app.get("/reservation/list-all")
async def list_all_reservations():
    reservations = app.database["reservations"].find({})
    filtered_reservations = []
    for reservation in list(reservations):
        filtered_reservations.append({
            "spot_id": reservation["spot_id"],
            "start_time": reservation["start_time"],
            "end_time": reservation["end_time"]
        })
    return filtered_reservations


@app.get("/generate-spots")
async def generate_spots():
    for i in range(1, 16):
        app.database["spots"].insert_one({
            "_id": i,
            "location": "BCT East",
            "occupied": False,
            "occupied_by": None,
            "reserved": False,
            "reserved_by": None,
            "reserved_until": None
        })
    return {"message": "success"}
# async def get_parking_spots():
    # return app.database["parking_spots"].find()