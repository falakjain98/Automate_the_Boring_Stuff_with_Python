#! python3
# downloadImgur.py - Download top 10 images from Imgur

import requests,os,bs4
search_term = str(input('Enter Search Term: '))
url = 'https://imgur.com/search/score?q=' + search_term    #starting url
os.makedirs('imgur - ' + search_term,exist_ok = True)     #storing comics in ./imgur - search term
print(f'Donwload page {url}')
resp = requests.get(url)
resp.raise_for_status()
soup = bs4.BeautifulSoup(resp.text,'lxml')
# Find URL of comic image
for img in soup.find_all('div',class_='post')[:5]:
    if img == '':
        print('Could not find image')
    else:
        imageUrl = 'https:' + img.find('img').get('src')
        # Download the image
        print(f'Downloading image {imageUrl}')
        res = requests.get(imageUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        directory = os.path.join('imgur - '+search_term,os.path.basename(imageUrl))
        if not os.path.exists(directory):
            imageFile = open(directory,'xb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        else:
            print('Image file already exists')
    # Get the Prev button's url
    #prevLink = soup.select('a[rel = "prev"]')[0]
    #url = 'https://xkcd.com'+prevLink.get('href')
print('Done!')