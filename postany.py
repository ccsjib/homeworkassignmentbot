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

r = requests.post("https://lake0.pythonanywhere.com/foo", data = json.dumps({"bot_id": "steve",
  "text": "Hello from VS Code script testing :)"}))
#assert r.status_code == 200
print(r.text)


#curl -X POST -d "{\"bot_id\": \"81110e5203f6018341de37d901\", \"text\": \"Hello world\"}" -H "Content-Type: application/json" https://api.groupme.com/v3/bots/post

#curl -X POST "https://api.groupme.com/v3/bots/post?bot_id=81110e5203f6018341de37d901&text=Hello+world"

#curl -X POST -d "{
  \"attachments\": [],
  \"avatar_url\": "https://i.groupme.com/123456789",
  \"created_at\": 1302623328,
  \"group_id\": "1234567890",
  \"id\": \"1234567890\",
  \"name\": \"John\",
  \"sender_id\": \"12345\",
  \"sender_type\": \"user\",
  \"source_guid\": \"GUID\",
  \"system\": false,
  \"text\": \"Hello world ☃☃\",
  \"user_id\": \"1234567890\"
}" -H "Content-Type: application/json" lake0.pythonanywhere.com/foo