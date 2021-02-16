import requests
import json

api_key = 'Please dont scrape my API key
base_url = 'https://www.alphavantage.co/query'
uin = ''
def getStockData(symbol):
    request = f'?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    ticker_data = requests.get(base_url+request)
    #Print the response in json form
    print(ticker_data.json())
    #Save it as a dict
    ticker = ticker_data.json()
    return ticker

data = {}
def main():
    while 1:
        uin = input('Enter a symbol to get stock price. Type quit to quit or save to save output.\n')
        if uin.lower() == 'quit':
            quit()
        elif uin.lower() == 'save':
            with open('japi.out', 'w') as f:
                json.dump(data, f, indent=4)
            print('Saved!')
        else:
            data[uin] = getStockData(uin)
            try:
                print(f"The current price of {uin} is: {data[uin]['Global Quote']['05. price']}")
            except:
                print('Unable to display price for entered symbol.')

if __name__ == '__main__':
    main()