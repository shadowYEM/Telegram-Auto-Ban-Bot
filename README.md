# Telegram Auto-Ban Bot


A simple yet effective Telegram bot built using the `telethon` library. This bot automatically bans users who leave a specified channel and ensures that users who left before the bot became an admin are also banned.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)



## Features

- **Automatic Banning**: Automatically bans users who leave the channel.
- **Retroactive Banning**: Bans users who left before the bot became an admin.
- **Real-time Monitoring**: Continuously monitors the channel for user actions.
- **Easy Setup**: Simple configuration and setup process.

## Requirements

- Python 3.7 or higher
- `telethon` library

## Installation

### Step-by-Step Guide

1. **Clone the Repository**:

   Open your terminal or command prompt and run the following commands to clone the repository to your local machine:

   ```bash
   git clone https://github.com/shadowYEM/telegram-auto-ban-bot.git
   cd telegram-auto-ban-bot
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:

   It's a good practice to use a virtual environment to manage dependencies. You can create one using `venv`:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   Install the required Python packages using `pip`:

   ```bash
   pip install telethon
   ```

4. **Set Up API Credentials**:

   - Obtain your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).
   - Create a bot using [BotFather](https://t.me/BotFather) and get the bot token.

## Configuration

- **API Credentials**: Replace the placeholders in the script with your `api_id` and `api_hash`.
- **Bot Token**: Replace the placeholder with your bot token.
- **Channel ID**: Set the `channel_id` variable to the ID of the channel where the bot will operate.

```python
# Example configuration in the script
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'
channel_id = -1001234567890  # Replace with your channel ID
```

## Usage

1. **Run the Bot**:

   Execute the bot script using Python:

   ```bash
   python app.py
   ```

2. **Monitoring**: The bot will start monitoring the channel and ban users who leave. It will also check for users who left before it became an admin and ban them.




---
