import requests
import json
import jsonpath
#Api url
URL = 'https://reqres.in/api/users'

#Read input json file
file = open("C:\\Users\\durve\\PycharmProjects\\RestApi_practice\\CreateReq.json",'r')
json_input = file.read()
file.close()
request_json = json.loads(json_input)

#Make POST request with json input body
response = requests.post(URL,request_json)
print(response.content)
print(response.status_code)
#Validate response code
#assert response.status_code == 201

#fetch resonse header
print(response.headers)

# to get specific header
print(response.headers.get('Content-Length'))

#to get 'id' from response content
json_response = json.loads(response.text) #Parse response to json format
id = jsonpath.jsonpath(json_response,'id')
print(id[0])
