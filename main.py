# main.py

# from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional
from random import randint

import json

app = FastAPI()

uri = 'mongodb://root:root/'
client = MongoClient("db", 27017, username="root", password="root", authSource='admin', authMechanism='SCRAM-SHA-256')
db = client.latune

class Device(BaseModel):
    deviceID: int
    deviceName: str
    deviceType: str


@app.post("/devices")
async def add_device(device: Device):
    r = db.devices.insert_one(device.dict())
    return r.inserted_id


@app.delete("/devices/{id}")
async def delete_device(id: int):
    r = db.devices.delete_one({"deviceID": id})
    return 200

@app.get("/devices/")
async def get_devices():
    r = db.devices.find({})
    return r.to_array()

@app.get("/devices/{id}")
async def get_devices(id: int):
    r = db.devices.find({"deviceID": id})
    return list(r)


@app.put("/devices/{id}")
async def update_device(device: Device):
    r = db.devices.update_one({"deviceID": id})
    return id
