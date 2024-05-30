# discord-scripts

A collection of scripts for Discord.

> [!WARNING]
> Selfbotting is against Discord's Terms of Service. Use at your own risk.

## Setup

1. Populate `.env` file.
2. Setup virtual environment and install dependencies.

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## Selfbot

> self.py

- `/nerd <mention>`: Toggles whether a user is a nerd or not. Every message from any nerds (including in DMs, group DMs, and servers), will be replied to, quoting the message with a nerd emoji.
