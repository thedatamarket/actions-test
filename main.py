import requests
import yfinance as yf
def msg(message):
    print(message)
    news = message.replace("(","").replace(")","").replace(".",",").replace("-","/")
    bot_token = '5041715929:AAFcraPI9-8jZR0bLkquRDNUXg96tEUKje4'
    bot_chatID = '1259144189'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='+ bot_chatID + '&parse_mode=MarkdownV2&text=' + news

    response = requests.get(send_text)
    print(response.json())
    return response.json()

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

ticker = ['HINDUNILVR.NS','RECLTD.NS','JPPOWER.NS']

msg("WatchList")
for i in ticker:
    txt = str(i) + ' ' + str(get_current_price(i))
    msg(txt)

msg("Portfolio")
port = {
    "TCS.NS" : 2,
    "WIPRO.NS" : 2,
    "INFY.NS" : 1,
    "NTPC.NS" : 5,
    "HINDUNILVR.NS":3
}
sum = 0
for i in port:
    sum = int(int(get_current_price(i))*port[i]) + sum 
txt = "Portfolio " + str(sum) + " of 17795"
msg(str(txt))
