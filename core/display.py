from core.api import snowflake_to_date

RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

PREMIUM = {0: "None", 1: "Nitro Classic", 2: "Nitro", 3: "Nitro Basic"}

def print_profile(data: dict, kind: str):
    uid     = data.get("id", "N/A")
    uname   = data.get("username", "N/A")
    disc    = data.get("discriminator", "0")
    dname   = data.get("global_name") or uname
    avatar  = data.get("avatar")
    tag     = f"{uname}#{disc}" if disc != "0" else uname
    created = snowflake_to_date(uid)
    av_url  = f"https://cdn.discordapp.com/avatars/{uid}/{avatar}.png" if avatar else "none"

    sep = "  " + "─" * 52

    print(f"\n{sep}")
    print(f"  {'BOT' if data.get('bot') else 'USER'}  /  {kind.upper()} TOKEN")
    print(sep)
    print(f"  tag           {DIM}{tag}{RESET}")
    print(f"  display name  {DIM}{dname}{RESET}")
    print(f"  id            {DIM}{uid}{RESET}")
    print(f"  created       {DIM}{created}{RESET}")
    print(f"  avatar        {DIM}{av_url}{RESET}")

    if kind == "self":
        print(f"  email         {DIM}{data.get('email', 'N/A')}{RESET}")
        print(f"  phone         {DIM}{data.get('phone', 'N/A')}{RESET}")
        print(f"  verified      {DIM}{'yes' if data.get('verified') else 'no'}{RESET}")
        print(f"  2fa           {DIM}{'enabled' if data.get('mfa_enabled') else 'disabled'}{RESET}")
        print(f"  nitro         {DIM}{PREMIUM.get(data.get('premium_type', 0), 'unknown')}{RESET}")

    print(sep + "\n")

    return tag, uid, created
