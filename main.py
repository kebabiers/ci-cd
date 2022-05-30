# main.py

# from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Device(BaseModel):
    deviceID: int
    deviceName: str
    deviceType: str


@app.post("/add")
async def add_device(device: Device):
    return device


@app.delete("/delete/{id}")
async def delete_device(id: int):
    return id


@app.get("/devices/{id}")
async def get_devices(id: int):
    return id


@app.put("/update/{id}")
async def update_device(device: Device):
    return device
