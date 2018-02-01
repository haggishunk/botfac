import requests

url = r'http://localhost:8000/bots/'

r = requests.get(url)

if r.text == 'Welcome to the BotFac':
    pass
else:
    raise Exception
