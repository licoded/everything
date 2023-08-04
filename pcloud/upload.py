from pcloud import PyCloud
import requests
import json

pc = PyCloud('lykangforever@gmail.com', 'lykang.0804', endpoint="eapi")

res = pc.listfolder(folderid=0)

token = pc.get_auth_token()

print(token)
print(pc.listtokens())
print(pc.uploadtransfer())


url = 'https://api.pcloud.com/uploadtransfer'
params = {
    'language': 'en',
    'ppaccepted': 'yes',
    'sendermail': 'lykangforever@gmail.com',
    'getlink': '1',
    'locationid': '2',
    'ts': '1691115114',
    # 'debug': 'String languageenppacceptedyests1691115114; Browser Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'sig': '69210255c78f45bf5fe295aa41a4fb258182349c',
    'auth': token
}

# Open the file to be uploaded
file_path = '/root/nerd-fonts/glyphnames.json'
files=[
  ('files',('file',open(file_path,'rb'),'application/octet-stream'))
]
# Create the form-data request
response = requests.post(url, data=params, files=files)

# Parse the JSON response
data = json.loads(response.text)
print(data)

# Extract the code field from the response
code = data['code']
print(data['link'])

# Print the code value
print(code)
