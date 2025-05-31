from fastapi import FastAPI, Request, Query, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from prometheus_fastapi_instrumentator import Instrumentator
from password_generator import generate_password  # adjust if under `app.`

app = FastAPI()

# Setup limiter (e.g., 5 requests per minute per IP)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Metrics Monitoring
Instrumentator().instrument(app).expose(app)

@app.get("/generate-passwords")
@limiter.limit("5/minute")
def generate_passwords(
    request: Request,
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
