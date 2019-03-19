import requests
import json

symbol = 'AAPL'

url = 'https://uk.finance.yahoo.com/quote/{}?p={}'.format(symbol, symbol)
r = requests.get(url)

content = ''
page_content_lines = r.text.split('\n')
for line in page_content_lines:
	if line.startswith('root.App.main'):
		content = line.split('root.App.main = ')[1]
		
		with open('/home/nikeah/yahooFinanceResponse.txt', 'w') as file:
			file.write(content)
			
		break


with open('/home/nikeah/yahooFinanceResponse.txt', 'r') as file:
	content = file.read()
	
json_content = json.loads(content[:-1])
dataStore = json_content['context']['dispatcher']['stores']['StreamDataStore']['quoteData'][symbol]

#print(dataStore)

opening_value = dataStore['regularMarketOpen']['raw']
high_value = dataStore['regularMarketDayHigh']['raw']
low_value = dataStore['regularMarketDayLow']['raw']
volume_value = dataStore['regularMarketVolume']['raw']

change_percentage_value = dataStore['regularMarketChangePercent']['raw']
change_value = dataStore['regularMarketChange']['raw']
current_price = dataStore['regularMarketPrice']['raw']
symbol_value = dataStore['symbol']
timestamp = dataStore['regularMarketTime']['fmt']

print(symbol)
print('Price:', current_price)
print('Change:', change_value)
print('Change %:', change_percentage_value)
print('Timestamp:', timestamp)