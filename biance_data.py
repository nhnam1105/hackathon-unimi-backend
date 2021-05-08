import requests
import json
import flask
from flask import request, jsonify

#######################
def data_binance(crypto_pair):
    request = requests.get('https://api2.binance.com/api/v3/ticker/price')
    json_dt = json.loads(request.text)
    print(json_dt)  # prices of all crypto
    for dictionary in json_dt:
        if (dictionary["symbol"] == crypto_pair):
            print(dictionary['price'])
    return (dictionary['price'])


def data_kucoin(crypto_pair):
    url = 'https://api.kucoin.com/api/v1/market/histories?symbol=' + crypto_pair
    request = requests.get(url)
    json_data = json.loads(request.text)
    # print(json_data)
    print(json_data['data'][0]['price'])  # tim data > chon position 0 in the list > extract 'price'
    return (json_data['data'][0]['price'])

def get_all_coinpairs():
    url = "https://api.kucoin.com/api/v1/market/allTickers"
    request = requests.get(url)
    json_data = json.loads(request.text)
    coin_pair = []
    for coinpair in json_data['data']['ticker']:
        coin_pair.append(coinpair['symbol'])
    return coin_pair
##########
#data_binance('LTC', 'BTC')
#data_kucoin('LTC', 'BTC')
print(get_all_coinpairs())