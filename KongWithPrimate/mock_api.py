from fastapi import FastAPI
import os
app = FastAPI()


@app.get("/api/test")
async def root():
    version_name = os.environ.get('name')
    return {
        "message": "testing ap in kong ",
        "version": f"{version_name}"
    }
