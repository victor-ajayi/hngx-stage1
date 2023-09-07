from datetime import datetime, timezone, tzinfo

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


@app.get("/api")
async def main(slack_name: str, track: str):
    return {
        "slack_name": slack_name,
        "current_day": datetime.now().strftime("%A"),
        "utc_time": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "track": track,
        "github_file_url": "https://github.com/victor-ajayi/hngx-stage1/blob/main/main.py",
        "github_repo_url": "https://github.com/victor-ajayi/hngx-stage1",
        "status_code": 200,
    }
