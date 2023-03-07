import os,requests,json
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
API_ID = 'CDwIWESGJbhDXmUqO17BnhiJdiE2'
headers =  {
        'Authorization': SECRET_KEY,
        'X-User-ID': API_ID,
        "Content-Type":"application/json"
    }
url = 'https://play.ht/api/v1/articleStatus?transcriptionId=-NPxMmUU8cQ4_bMJVgu3'
payload = json.dumps({"status":"CREATED","transcriptionId":"-NPxHE714ljH9II8tTEe","contentLength":2,"wordCount":10})
response = requests.request("GET",url, headers=headers,data=payload)
print(response.text)