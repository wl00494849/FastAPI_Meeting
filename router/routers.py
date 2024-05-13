from fastapi import APIRouter
from router.api_v1.update_file import router as update_file

routers = APIRouter()
routers.include_router(update_file)