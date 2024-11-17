import uvicorn
from fastapi import FastAPI
from api.user import router as user_router
from api.theme import router as theme_router
from api.surveillance import router as surveillance_router

app = FastAPI()
app.include_router(user_router)
app.include_router(theme_router)
app.include_router(surveillance_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
