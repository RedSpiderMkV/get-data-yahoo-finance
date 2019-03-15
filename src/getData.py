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

print(dataStore)


