#! python3
# threadedDownloadXkcd.py - Download Xkcd comics using multiple threads

import requests,os,bs4,threading

url = 'https://xkcd.com/'  #starting url
os.makedirs('xkcd',exist_ok = True)     #storing comics in ./xkcd
def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        # Download the page
        print(f'Donwload page {url}{urlNumber}')
        resp = requests.get(url+str(urlNumber))
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

# Create and start the Thread Project
downloadThreads = [] #list of all thread objects
for i in range(0,140,10):
    start = i
    end = i + 9
    if start == 0:
        start = 1 #since there is no comic 0, therefore setting to 1
    downloadThread = threading.Thread(target = downloadXkcd, args = (start,end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')