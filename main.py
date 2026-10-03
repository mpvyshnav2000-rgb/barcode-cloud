from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

serial_numbers = []


class ScanData(BaseModel):
    serial: str


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Barcode Cloud Server"
    }


@app.post("/scan")
def receive_scan(data: ScanData):

    serial = data.serial.strip()

    if serial:
        serial_numbers.append(serial)

        print("Received:", serial)

        return {
            "success": True,
            "serial": serial
        }

    return {
        "success": False
    }


@app.get("/next")
def get_next():

    if len(serial_numbers) == 0:
        return {
            "available": False
        }

    serial = serial_numbers.pop(0)

    return {
        "available": True,
        "serial": serial
    }
