import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

ccy_1 = "USD"
ccy_2 = "PHP"
amt = "100"

querystring = {"from":ccy_1,"to":ccy_2,"amount":amt}

headers = {
	"X-RapidAPI-Key": "d9c9a9ce8cmsh36e8be071e6516cp13e109jsn80510aaec594",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amt = data['result']['convertedAmount']
formatted_amt = "{:,.2f}".format(converted_amt)

print(converted_amt, formatted_amt)