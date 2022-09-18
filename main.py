import base64
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

DURATION_URL = "https://wakatime.com/api/v1/users/current/summaries"


def get_creds(env_path: Path) -> str:
    """Get API Key"""
    load_dotenv(env_path)
    api_key = os.environ.get("API_KEY", "")
    return api_key


def get_day_stats(api_key: str, url: str, date: datetime) -> List:
    """Get the day stats"""
    url = f"{url}?api_key={api_key}&start={date}&end={date}"
    with requests.session() as s:
        response = s.get(url).json()
    return response


def main():
    env_path = Path.cwd() / ".env"
    api_key = get_creds(env_path=env_path)
    today = datetime.today().strftime("%Y-%m-%d")
    stats = get_day_stats(api_key=api_key, url=DURATION_URL, date=today)
    stats_json = json.dumps(stats, indent=4)
    print(stats_json)


if __name__ == "__main__":
    main()
