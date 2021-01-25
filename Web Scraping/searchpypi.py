#! python3
# searchpypi.py - Open several search results in multiple tabs
import requests, webbrowser, bs4, sys

print('Searching....')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Search top result links
soup = bs4.BeautifulSoup(res.text,'lxml')
# Open a browser tab for each result
linkElems = soup.select('.package-snippet')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org'+linkElems[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)