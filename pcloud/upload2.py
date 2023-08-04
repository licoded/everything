import requests

url = "https://api.pcloud.com/uploadtransfer"

payload = {'language': 'en',
'ppaccepted': 'yes',
'sendermail': 'lykangforever@gmail.com',
'getlink': '1',
'auth': '7BGUJ7ZhyNQZKFd7jpVhL47ItkgKgTc0i4clocPy',
'locationid': '2',
'ts': '1691115114',
'debug': 'String languageenppacceptedyests1691115114; Browser Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
'sig': '69210255c78f45bf5fe295aa41a4fb258182349c'}
files=[
  ('files',('file',open('/root/nerd-fonts/glyphnames.json','rb'),'application/octet-stream'))
]
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Origin': 'https://transfer.pcloud.com',
  'Pragma': 'no-cache',
  'Referer': 'https://transfer.pcloud.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

