import requests

TOKEN = "Bot TOKEN"
CHANNEL_ID = "123456789"

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

data = {
    "content": "Hello from Discord API!"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
