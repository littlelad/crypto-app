from django.shortcuts import render
import requests
import json

# Crypto News
api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
api = json.loads(api_request.content)

# Crypto Price
price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,XRP,XMR,DASH,LTC,ZEC,ETC,QTUM&tsyms=USD")
price = json.loads(price_request.content)


def home(request):

    return render(request, 'home.html', {"api": api, "price": price})


def prices(request):

    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter a crypto currency symbol above"
        return render(request, 'prices.html', {'notfound': notfound})
