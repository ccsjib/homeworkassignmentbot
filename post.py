import requests
import json

#URL = 

#https://stackoverflow.com/questions/49721695/python-requests-get-gets-stuck
#https://www.w3schools.com/python/ref_requests_post.asp

#https://www.geeksforgeeks.org/get-post-requests-using-python/



PARAMS = {
  "bot_id"  : "81110e5203f6018341de37d901",
  "text"    : "Hello from VS Code script testing :)"
}

r = requests.post("https://api.groupme.com/v3/bots/post", data = json.dumps({"bot_id": "81110e5203f6018341de37d901",
  "text": "Hello from VS Code script testing :)"}))

print(r.text)


#curl -X POST -d "{\"bot_id\": \"81110e5203f6018341de37d901\", \"text\": \"Hello world\"}" -H "Content-Type: application/json" https://api.groupme.com/v3/bots/post

#curl -X POST "https://api.groupme.com/v3/bots/post?bot_id=81110e5203f6018341de37d901&text=Hello+world"