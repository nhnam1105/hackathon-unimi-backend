import requests
import json

'''from datetime import datetime
timestamp = 1620490775
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object =", dt_object)'''

###FIAT
'''request2 = requests.get('https://api.kucoin.com/api/v1/prices')
json_data2 = json.loads(request2.text)
print(json_data2['data']['ETH'])'''


def data_kucoin(coin1, coin2):
    url = 'https://api.kucoin.com/api/v1/market/histories?symbol=' + coin1 + '-' + coin2
    request = requests.get(url)
    json_data = json.loads(request.text)
    # print(json_data)
    print(json_data['data'][0]['price'])  # tim data > chon position 0 in the list > extract 'price'
    return (json_data['data'][0]['price'])


def data_binance(coin1, coin2):
    crypto_pair = coin1 + coin2
    request = requests.get('https://api2.binance.com/api/v3/ticker/price')
    json_dt = json.loads(request.text)
    print(json_dt)  # prices of all crypto
    for dictionary in json_dt:
        if (dictionary["symbol"] == crypto_pair):
            print(dictionary['price'])
    return (dictionary['price'])


##########
data_kucoin('BTC', 'USDT')
data_binance('BTC', 'USDT')
