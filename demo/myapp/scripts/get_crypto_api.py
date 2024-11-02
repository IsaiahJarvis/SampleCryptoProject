from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from collections import defaultdict
from myapp.models import Crypto
import json

def call_api():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '100470ef-7bad-4b31-adc9-dae9cbacf3f3',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        store_wanted_data = []

        if 'data' in data:
            coindata = data['data']

            for x in coindata:
                curr = x

                store_wanted_data.append({'name': curr['name'], 'market_cap': curr['quote']['USD']['market_cap']})
        else:
            print("No data found in the response")
        return store_wanted_data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None
    
def run():
    coin_data = call_api()
    
    if coin_data:
        Crypto.objects.all().delete()
        for item in coin_data:
            cat_name = item['name']
            cat_market_cap = item['market_cap']

            print(cat_name, cat_market_cap)

            c = Crypto(name = cat_name, market_cap = cat_market_cap)

            c.save()
