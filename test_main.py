# from fastapi import FastAPI
import main
from fastapi.testclient import TestClient

# app = FastAPI()

client = TestClient(main.app)


def test_add():
    r = client.post(
        "/devices", json={"deviceID": 0, "deviceName": "Thomas", "deviceType": "Nuleuh"}
    )

    print(r.json())
    assert r.status_code == 200
    assert r.json() == {"deviceID": 0, "deviceName": "Thomas", "deviceType": "Nuleuh"}


def test_delete():
    r = client.delete("/devices/10")
    print(r.json())
    assert r.status_code == 200
    assert r.json() == 10


def test_get():
    r = client.get("/devices/10")
    print(r.json())
    assert r.status_code == 200
    assert r.json() == 10


def test_update():
    r = client.put(
        "/devices/10",
        json={"deviceID": 10, "deviceName": "Thomas", "deviceType": "Nule"},
    )
    print(r.json())
    assert r.status_code == 200
    assert r.json() == {"deviceID": 10, "deviceName": "Thomas", "deviceType": "Nule"}
