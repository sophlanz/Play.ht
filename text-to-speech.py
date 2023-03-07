import os,requests,json
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
API_ID = 'CDwIWESGJbhDXmUqO17BnhiJdiE2'
#How the request body looks like

payload = json.dumps({
  "voice": "en-US-AriaNeural",
  "content": [
   "Hi Sophia",
   "woah woah woah woah woah woah woah woah woah woah"
  ],
   "title": "Testing public api convertion",
     "narrationStyle":"angry"
})

url = "https://play.ht/api/v1/convert"

headers =  {
        'Authorization': SECRET_KEY,
        'X-User-ID': API_ID,
        "Content-Type":"application/json"
    }
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
