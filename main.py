from website import create_app
from requests import Request, Session
from pprint import pprint as pp
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'faa372e6-b6d7-40b8-8863-65aba376c307',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = response.json()['data']
  j = 0 
  Cryptodict = {}
  CryptoInfo = {}
  #pp(data)
  for i in data:
    Cryptodict["symbol"] = i["symbol"]
    Cryptodict["name"] = i["name"]
    Cryptodict["price"] = i['quote']['USD']['price']
    Cryptodict["volume24"] = i['quote']['USD']['volume_change_24h']
    #print(i["symbol"])
    CryptoInfo[j] = Cryptodict
    j = j+1

  pp(CryptoInfo)
  with open('CryptoInfo', 'w') as f:
    json.dump(CryptoInfo,f)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  pp(e)
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
