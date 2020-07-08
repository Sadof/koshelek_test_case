from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys



url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'sort':'volume_24h',
  'sort_dir': 'desc',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '14031ef2-d0d5-43f2-a442-96d137384fcf',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print([item['name'] for item in data['data']])
  print(response.elapsed.total_seconds())
  print(sys.getsizeof(response))
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)