import requests
import json
import jsonpath
#Api url
URL = 'https://reqres.in/api/users/2' # 2 is the id of the user whose value needs to be updated

#Read input json file
file = open("C:\\Users\\durve\\PycharmProjects\\RestApi_practice\\UpdateReq.json",'r')
json_input = file.read()
file.close()
request_json = json.loads(json_input)

#Make PUT request with json input body
response = requests.put(URL,request_json)

#Validate response code
#assert response.status_code == 200

#to get 'updatedAt' from response content
json_response = json.loads(response.text) #Parse response to json format
updated_at = jsonpath.jsonpath(json_response,'updatedAt')
print(updated_at[0])
