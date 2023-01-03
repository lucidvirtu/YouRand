import requests, json, datetime

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

headers = {
    'User-Agent': 'PyXBT'
}

try:
    response = (requests.get(url, headers=headers)).content
    result = json.loads(response.decode('utf-8'))
    timestamp = datetime.datetime.now()
    usdprice = result['bpi']['USD']['rate_float']
    eurprice = result['bpi']['EUR']['rate_float']
    gbpprice = result['bpi']['GBP']['rate_float']

    records = [(usdprice, timestamp, 'USD'), (eurprice, timestamp, 'EUR'), (gbpprice, timestamp, 'GBP')]

    print("USD: ", usdprice)
    print("EUR: ", eurprice)
    print("GBP: ", gbpprice)
except:
    print("Error updating latest price")
