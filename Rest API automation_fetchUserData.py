import requests
import json
import jsonpath
#Api url
URL = 'https://reqres.in/api/users?page=2'

#send GET request
response = requests.get(URL)

#Display response content
# print(response.content)
#Display response header
# print(response.headers)

#Parse the response to json format
json_response = json.loads(response.text)
# print(json_response)

#Fetch value of a field using jsonpath
pages = jsonpath.jsonpath(json_response,'total_pages') # returns a list
print(pages[0])
assert  pages[0]== 3 # for testing