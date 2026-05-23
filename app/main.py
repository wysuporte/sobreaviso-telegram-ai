from fastapi import FastAPI
from app.routes.telegram_webhook import router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

app.include_router(router)


@app.get("/")
def health_check():
    return {
        "status": "online"
    }


