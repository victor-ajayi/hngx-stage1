from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main(slack_name: str, track: str):
    now = datetime.now()

    return {
        "slack_name": slack_name,
        "current_day": now.day,
        "utc_time": now.time(),
        "track": track,
        "github_file_url": "",
        "github_repo_url": "",
        "status_code": 200,
    }
