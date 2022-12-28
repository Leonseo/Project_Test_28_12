import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f) #Читает информацию из файла в username
    print(f"Welcome back, {username} !")