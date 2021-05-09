import flask
from flask import request, jsonify
import biance_data

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# A route to return all of the available entries in our catalog.
@app.route('/api/get_price', methods=['GET'])
def get_price():
    if 'coinpair' in request.args:
        coinpair = request.args['coinpair']
        print(coinpair)
    else:
        return "Error: No id field provided. Please specify an id."
    price_dict = {}
    kc = biance_data.data_kucoin(coinpair)
    print(kc)
    price_dict['kucoin'] = kc
    coinpair = coinpair.replace("-", "")
    bn = biance_data.data_binance(coinpair)
    if bn == None:
        bn = 0
    price_dict['binance'] = bn
    return jsonify(price_dict)


@app.route('/api/get_all_coinpairs', methods=['GET'])
def get_all():
    cp = biance_data.get_all_coinpairs()
    return jsonify(cp)
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)