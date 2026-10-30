from fastapi import FastAPI

from routes.stu_routers import router


app = FastAPI(
    title="Student CRUD Application"
)


app.include_router(router)