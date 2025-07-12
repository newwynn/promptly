from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routes import auth

app = FastAPI()

# Include routers
app.include_router(auth.router)

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "welcome"
 