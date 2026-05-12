from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Skeleton API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "FastAPI backend running"}