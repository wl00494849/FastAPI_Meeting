from fastapi import FastAPI
import uvicorn
from routers.api import router

app = FastAPI()
app.include_router(router,prefix="/api")

@app.get("/")
async def root():
    return {"message":"test"}

uvicorn.run(app,port=8080)