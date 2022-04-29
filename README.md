# Woo-trade-python-api

## Example used
init
```
API = "*******************************"
SECRET = "********************************"
client = Client(API, SECRET)
```
get available symbol
```
client.get_all_symble()
```
get Kline
```
data = client.get_kline("SPOT_BTC_USDT", "1m")
df = pd.DataFrame(data["rows"])[::-1]
df['date'] = [str(datetime.fromtimestamp(i/1000)) for i in df["start_timestamp"]]
df.set_index('date', inplace=True)
df["SMA20"]=df["close"].rolling(20).mean()
```
send order
```
# sell: use market price
client.send_order("PERP_ETH_USDT", "MARKET", 100, 0.02, "SELL")
# buy : use limit price 
client.send_order("PERP_ETH_USDT", "LIMIT", 5000, 0.02, "BUY")
```
