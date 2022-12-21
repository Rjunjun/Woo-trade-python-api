import requests
import time
import hmac
import hashlib
from collections import OrderedDict

class Client():
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_api = "https://api.woo.network/v1/"

    def get_signature(self, params, timestamp):
        query_string = '&'.join(["{}={}".format(k, v) for k, v in params.items()]) + f"|{timestamp}"
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature

    def get_header(self, params):
        timestamp = str(int(time.time() * 1000))
        signature = self.get_signature(params, timestamp)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'x-api-key': self.api_key,
            'x-api-signature': signature,
            'x-api-timestamp': timestamp,
            'cache-control': 'no-cache'
        }
        return headers

    def get_orders(self, symbol):
        url = self.base_api + "orders/"
        params = {
            "symbol": symbol
        }
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()

    def get_kline(self, symbol, interval):
        url = self.base_api + "kline/"
        params = {
            "symbol": symbol,
            "type": interval,
            "limit": 10
        }
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()
    
    def get_kline_hist(self, symbol, interval, start_time):
        url = "https://api-pub.woo.org/v1/hist/kline"
        params = {
            "symbol": symbol,
            "type": interval,
            "start_time": start_time
        }
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()

    def get_all_symble(self):
        url = self.base_api + "public/info/"
        params = OrderedDict(sorted({}.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()

    def send_order(self, symbol, order_type, order_price, order_quantity, side, reduce_only):
        url = self.base_api + "order/"
        params = {
            "symbol": symbol,
            "order_type": order_type,
            "order_price": order_price,
            "order_quantity": order_quantity,
            "side": side,
            "reduce_only":reduce_only
        }
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.post(url=url, params=params,  headers=headers).json()

    def get_positions(self):
        url = self.base_api + "positions/"
        params = {}
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()

    def get_client_info(self):
        url = self.base_api + "client/info/"
        params = {}
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()
    
    def cancel_orders(self, symbol):
        url = self.base_api + "orders/"
        params = {
            "symbol": symbol
        }
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.delete(url=url, params=params,  headers=headers).json()

    def cancel_order(self, symbol, order_id):
        url = self.base_api + "order/"
        params = {
            "symbol": symbol,
            "order_id": order_id
        }
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.delete(url=url, params=params,  headers=headers).json()

    def get_info(self, symbol):
        url = self.base_api + "public/info/" + symbol
        params = {}
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()

    def get_orderbook(self, symbol):
        url = self.base_api + "orderbook/" + symbol
        params = {}
        params = OrderedDict(sorted(params.items()))
        headers = self.get_header(params)
        return requests.get(url=url, params=params,  headers=headers).json()
