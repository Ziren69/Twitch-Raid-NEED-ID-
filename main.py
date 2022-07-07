import requests
import random

def useraid(raidid):
    token1 = open('tokens.txt').read().splitlines()
    token = random.choice(token1)

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Authorization': f'OAuth {token}',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Client-Session-Id': '0e6bff1844174f35',
        'Client-Version': 'babfaee6-9f6f-4bcf-b3c6-265823943d65',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.twitch.tv',
        'Referer': 'https://www.twitch.tv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Device-Id': 'NZ8fPKkncCSh5AixdM7C4wO1rPtoysk9',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '[{"operationName":"JoinRaid","variables":{"input":{"raidID":"'+raidid+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"c6a332a86d1087fbbb1a8623aa01bd1313d2386e7c63be60fdb2d1901f01a4ae"}}}]'

    response = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)

fdsf = input('Enter raid id: ')
for i in range(10):
    useraid(fdsf)
    