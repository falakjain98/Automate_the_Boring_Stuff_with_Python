#! python3
# downloadXkcd.py - Download every single Xkcd comic

import requests,os,bs4

url = 'http://xkcd.com'     #starting url
os.makedirs('xkcd',exist_ok = True)     #storing comics in ./xkcd
for i in range(5):
    # Download the page
    print(f'Donwload page {url}')
    resp = requests.get(url)
    resp.raise_for_status()
    soup = bs4.BeautifulSoup(resp.text,'lxml')
    # Find URL of comic image
    comicElem = soup.select('#comic img')   #id = 'comic' and image within img tag
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image
        print(f'Downloading image {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        directory = os.path.join('xkcd',os.path.basename(comicUrl))
        if not os.path.exists(directory):
            imageFile = open(directory,'xb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        else:
            print('Image file already exists')
    # Get the Prev button's url
    prevLink = soup.select('a[rel = "prev"]')[0]
    url = 'https://xkcd.com'+prevLink.get('href')
print('Done!')