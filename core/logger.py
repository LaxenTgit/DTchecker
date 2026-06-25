from datetime import datetime, timezone

RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

LOG_FILE = "dtc_log.txt"

def log(level: str, message: str):
    now  = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] [{level.upper():7}] {message}"

    styled = f"  {BOLD}{line}{RESET}" if level == "ERROR" else f"  {line}"
    print(styled)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
