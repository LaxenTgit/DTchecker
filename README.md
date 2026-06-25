# DTchecker

Discord token inspector. Fetches account information from a given bot or self token via Discord API.

## Features

- Bot & self token support
- Account details: username, ID, creation date, avatar, email, 2FA, Nitro
- UTC timestamped log file

## Installation

```bash
git clone https://github.com/LaxenTgit/DTchecker.git
cd DTchecker
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

## Structure

```
DTchecker/
├── core/
│   ├── api.py
│   ├── display.py
│   └── logger.py
├── main.py
├── requirements.txt
└── .gitignore
```

## Disclaimer

For educational and personal use only. Only use on tokens you own.
