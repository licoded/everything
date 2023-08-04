from pcloud import PyCloud
import requests
import json
import datetime

# Define a function to extract and convert the date value
def get_date(d):
    return datetime.datetime.strptime(d['created'], '%a, %d %b %Y %H:%M:%S %z')

pc = PyCloud('lykangforever@gmail.com', 'lykang.0804', endpoint="eapi")

token_str = pc.get_auth_token()

# print(token)
# print(pc.uploadtransfer())

tokenList = pc.listtokens()['tokens']
sorted_tokenList = sorted(tokenList, key=get_date)
print(len(tokenList))

def manual_delete_token(tokenid):
    import requests
    url = f'https://eapi.pcloud.com/deletetoken?tokenid={tokenid}&auth={token_str}'
    response = requests.request("GET", url)
    return json.loads(response.text)

for tokenItem in sorted_tokenList[:-1]:
    print(tokenItem)
    device = tokenItem['device']
    tokenid = tokenItem['tokenid']
    # print(device, tokenid)
    if 'python-request' in device:
        # print('TODO: delete', tokenid)
        resp_json = manual_delete_token(tokenid)
        print('delete token', tokenid, ', resp: ', resp_json)

pc.logout()
