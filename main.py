import uvicorn
from fastapi import FastAPI
from api.user import router as user_router

app = FastAPI()
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
