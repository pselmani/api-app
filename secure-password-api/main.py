from fastapi import FastAPI, Query, HTTPException
from password_generator import generate_password

app = FastAPI()

@app.get("/generate-passwords")
def generate_passwords(
    count: int = Query(1, ge=1, le=100),
    length: int = Query(12, ge=6, le=128),
    special: int = Query(2, ge=0),
    digits: int = Query(2, ge=0)
):
    try:
        passwords = [generate_password(length, special, digits) for _ in range(count)]
        return {"passwords": passwords}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def liveness_probe():
    return {"status": "alive"}

@app.get("/ready")
def readiness_probe():
    return {"status": "ready"}