import requests
import base64
import time
import json

config = json.load(open("config.json", "r+"))

token = config['token']
changed = 0
print("started")
if config['text'] != "":
    arg  = f"/says/{config['text']}"
else: arg = ""
while True:

    image_response = requests.get(f"https://cataas.com/cat/cute/{arg}")
    image_data = image_response.content

    base64_image = base64.b64encode(image_data).decode('utf-8')

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "avatar": "data:image/jpeg;base64," + base64_image
    }
    response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=data)
    if response.status_code == 200:
        changed += 1
        print(f"[{changed}] Changed pfp")
        json = {
            "content":f"Changed pfp [{changed}]"
        }
        r = requests.post(config['webhook_log'], json=json)
        print(r.text)


    time.sleep(config['time']*60)
