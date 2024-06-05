import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBaA6Gnz5Z8_dI3Xx7PEN2cnTrEsbNZlw8"
)

data = {
    "contents": [
        {
            "parts":[
                {"text":"Write a story about a magic backpack"}
                ]
        }
    ]
}


res = requests.post(
    URL,
    headers={
        "content-type": "application/json",
    },
    json=data,
    params={"key": os.getenv("GOOGLE_API_KEY")}
)

json_res = res.json()
pprint(json_res)

joke = json_res["candidates"][0]['content']['parts'][0]['text']

print(res.json())