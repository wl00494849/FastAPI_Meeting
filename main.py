from fastapi import FastAPI
from router.routers import routers
import uvicorn

app = FastAPI()
app.include_router(routers,prefix="/api_v1")

@app.get("/")
async def root():
    return {"message":"test"}

uvicorn.run(app,port=8080)