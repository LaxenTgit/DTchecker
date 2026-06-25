import requests
from datetime import datetime, timezone

BASE = "https://discord.com/api/v10"

def snowflake_to_date(sid: str) -> str:
    try:
        ms = (int(sid) >> 22) + 1420070400000
        return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        return "unknown"

def fetch_bot(token: str) -> tuple[int, dict]:
    headers = {"Authorization": f"Bot {token}"}
    r = requests.get(f"{BASE}/users/@me", headers=headers, timeout=8)
    return r.status_code, r.json()

def fetch_self(token: str) -> tuple[int, dict]:
    headers = {"Authorization": token}
    r = requests.get(f"{BASE}/users/@me", headers=headers, timeout=8)
    return r.status_code, r.json()
