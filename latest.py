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
  CryptoInfo = []
  pp(data)
  limitNumber = 0
  while(limitNumber<10):

    for i in data[limitNumber]:
      Cryptodict["symbol"] = i["symbol"]
      Cryptodict["name"] = i["name"]
      Cryptodict["price"] = i['quote']['USD']['price']
      Cryptodict["volume24"] = i['quote']['USD']['volume_change_24h']
      #print(i["symbol"])
    CryptoInfo.append(Cryptodict)
    j = j+1
    limitNumber = limitNumber+1
    pp

  pp(CryptoInfo)
  with open('CryptoInfo', 'w') as f:
    json.dump(CryptoInfo,f)
#     for publication in publications:
#     #print(publication.text)
#     list_of_Publication.append(publication.text)
#     #print(publication.get_attribute('href'))
#     list_of_href.append(publication.get_attribute('href'))

# list_of_dict=[]
# dict_of_citation={}
# for href in list_of_href:
#     driver.get(href)
#     driver.implicitly_wait(10)
#     elements = driver.find_elements(By.CSS_SELECTOR, "div.gsc_oci_field")
#     i=0
#     for element in elements:
#         dict_of_citation[element.text] = driver.find_elements(By.CSS_SELECTOR, "div.gsc_oci_value")[i].text
#         i=i+1
#     dict_of_citation.pop('Description',None)
#     dict_of_citation.pop('Total citations',None)
#     dict_of_citation.pop('Scholar articles',None)
#     print(dict_of_citation)
#     print(""".
#     .""")
#     list_of_dict.append(dict_of_citation)


# with open('list_of_dict_cite', 'w') as f:
#     json.dump(list_of_dict,f)

# r = self.session.get(url, params=parameters)
#         data = r.json()['data']

    # Extracting the required data
#   name = data['name']
#   pp(name)
#   symbol = data['symbol']
#   pp(symbol)
#   volume_change_24h = data['quote']['USD']['volume_change_24h']
#   pp(volume_change_24h)
#   price = data['quote']['USD']['price']
#   pp(price)

    # Creating a dictionary
#   bitcoin_info = {
#     "name": name,
#     "symbol": symbol,
#     "volume_change_24h": volume_change_24h,
#     "price": price
#     }

#     # Printing the dictionary
#   print(bitcoin_info)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  pp(e)