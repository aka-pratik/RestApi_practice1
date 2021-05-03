import requests
#Api url
URL = 'https://reqres.in/api/users/2'
response = requests.delete(URL)

#Fetch delete request code
print(response.status_code)
assert response.status_code == 205
