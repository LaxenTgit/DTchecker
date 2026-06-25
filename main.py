import requests
from core.api     import fetch_bot, fetch_self
from core.display import print_profile
from core.logger  import log

RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

BANNER = """
  ██████╗ ████████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
  ██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
  ██║  ██║   ██║   ██║     ███████║█████╗  ██║     █████╔╝ 
  ██║  ██║   ██║   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
  ██████╔╝   ██║   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝

               Discord Token Inspector  -  by LaxenT
  ================================================================
"""

def handle(kind: str):
    is_bot = kind == "bot"
    token  = input(f"  {kind} token: ").strip()
    print()

    if not token:
        log("ERROR", "empty token")
        return

    log("INFO", f"checking {kind} token  ({token[:10]}...)")

    try:
        status, data = fetch_bot(token) if is_bot else fetch_self(token)

        if status == 200:
            tag, uid, created = print_profile(data, kind)
            log("INFO", f"profile fetched  —  {tag}  ({uid})  created: {created}")
        elif status == 401:
            log("ERROR", "invalid token  (401)")
        elif status == 429:
            log("WARN",  "rate limited  (429)  —  retry later")
        else:
            log("ERROR", f"unexpected response  —  status {status}")

    except requests.exceptions.ConnectionError:
        log("ERROR", "no internet connection")
    except requests.exceptions.Timeout:
        log("ERROR", "request timed out")
    except Exception as e:
        log("ERROR", f"unhandled exception: {e}")

def main():
    print(BANNER)
    log("INFO", "session started")

    while True:
        print()
        print(f"  {BOLD}[1]{RESET} Bot token")
        print(f"  {BOLD}[2]{RESET} Self token")
        print(f"  {BOLD}[0]{RESET} Exit")
        print()

        choice = input("  > ").strip()
        print()

        if choice == "0":
            log("INFO", "session ended")
            break
        elif choice == "1":
            handle("bot")
        elif choice == "2":
            handle("self")
        else:
            log("WARN", f"invalid choice: {repr(choice)}")

if __name__ == "__main__":
    main()
