# Potato Hook - Webhook Spam Tool

Potato Hook is a Python-based tool designed for spamming a webhook multiple times with random messages from a text file. The tool allows you to configure the number of messages to send and uses a specified webhook URL for the spam operation. **This tool is intended for educational purposes only** and should **not** be used in any malicious way, as it can violate the terms of service of platforms like Discord.

## Features
- Read messages from a `messages.txt` file.
- Send a specified number of random messages to the provided webhook.
- Handles rate limiting by waiting before retrying if rate-limited.
- Delete the webhook after spamming.

## Requirements
- Python 3.x
- `requests` library (can be installed via `pip`)

## Setup
1. Clone or download the repository to your local machine.
2. Install the required dependencies using `pip`:
   `'pip install requests'`

3. Ensure you have a `messages.txt` file in the same directory as the script. This file should contain the messages you want to spam, each on a new line.

4. Run the script:
   `'python potato_hook.py'`

   The script will prompt you to:
   - Enter the webhook URL.
   - Enter how many times you want to spam the webhook.

   After the spam operation, the script will delete the webhook and display a summary.

## Usage
1. Make sure to place your `messages.txt` in the same directory as the script.
2. Ensure that the webhook URL you provide is valid and has the necessary permissions.
3. Execute the script by running it in a terminal or command prompt:
   `'python potato_hook.py'`

4. Follow the on-screen prompts to:
   - Enter the webhook URL.
   - Enter the number of messages to send (defaults to 69 if you enter an invalid number).

5. The script will spam the webhook with random messages from your `messages.txt` and will automatically delete the webhook after completing the task.

## Important Notes
- **Do not** use this tool to spam others or perform any malicious activities.
- Using this script to spam a webhook may violate the terms of service of platforms like Discord or others.
- This tool is intended for educational and personal use only.
