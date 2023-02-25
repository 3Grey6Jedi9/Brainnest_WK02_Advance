import json

with open('/Users/danielmulatarancon/Desktop/Documents/HACKING TIME/Brainnest /Week 02/Advance Tasks/OAuth/client_secret_google.json') as f:
    secret_data = json.load(f)


useful_data = secret_data['installed']
print(useful_data)

