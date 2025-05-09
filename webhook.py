import requests
import random
import time
import os

# Set console title
os.system('title potatoking - Deadhook')

# ASCII Art Banner
print(r'''
██████╗  ██████╗ ████████╗ █████╗ ████████╗ ██████╗     ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗    ██║ ██╔╝██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║   ██║   ███████║   ██║   ██║   ██║    █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║   ██║   ██║   ██╔══██║   ██║   ██║   ██║    ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║     ╚██████╔╝   ██║   ██║  ██║   ██║   ╚██████╔╝    ██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝      ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
''')

# Load messages
try:
    with open('messages.txt') as f:
        messages = f.read().splitlines()
except FileNotFoundError:
    print('\u001b[31m[-] Failed! \u001b[33mCould not find "messages.txt", did you remove it?\u001b[0m')
    os.system('title ERROR - Missing files! && PAUSE >nul')
    os._exit(0)

# Get webhook URL
os.system('title potatoking - Enter webhook URL!')
webhook = input('\u001b[32;1m[?] Enter the webhook URL >>> \u001b[33m')
hookInfo = requests.get(webhook)

if hookInfo.status_code == 401:
    print('\u001b[31m[-] Invalid webhook!\u001b[0m')
    os.system('title ERROR - Invalid webhook! && PAUSE >nul')
    os._exit(0)

hookName = hookInfo.json().get('name', 'Unknown Webhook')

# Get message count
os.system('title potatoking - Message count')
try:
    times = int(input('\u001b[32;1m[?] How many messages to send? >>> \u001b[33m') or 69)
except ValueError:
    print('\u001b[31m[-] Invalid number, defaulting to 69.\u001b[0m')
    times = 69

os.system('title potatoking - Ready')
print(f'\u001b[32;1m[+] Ready! \u001b[33mSending {times} messages to "{hookName}"\u001b[0m\n')
os.system('PAUSE >nul')

# Send messages
for i in range(1, times + 1):
    tempMsg = random.choice(messages)
    res = requests.post(webhook, json={'content': tempMsg})
    if res.status_code == 429:
        wait = res.json().get('retry_after', 1000) / 1000 + 1
        print(f'\u001b[31m[-] Ratelimited! Waiting {wait:.2f} seconds...\u001b[0m')
        time.sleep(wait)
    else:
        print(f'\u001b[32;1m[+] Sent #{i}: \u001b[33m"{tempMsg}"\u001b[0m')
    os.system(f'title potatoking - Spamming... ({i}/{times})')

# Delete webhook
requests.delete(webhook)
print(f'\u001b[32;1m[+] Done! \u001b[33mDeleted webhook "{hookName}" after spamming {times} times.\u001b[0m')
os.system(f'title potatoking - Completed!')
os.system('PAUSE >nul')
