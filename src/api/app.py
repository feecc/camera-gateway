from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI("feecc-camera-gateway")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "DELETE", "PUT"],
    allow_headers=["*"],
)


@app.get("/photo")
def get_photo() -> ...:
    """Get a photo from the camera"""