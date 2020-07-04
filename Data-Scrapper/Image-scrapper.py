import urllib.request
import pandas as pd

def dl_jpg(url,file_path,file_name):
  full_path = file_path + file_name + '.jpg'
  urllib.request.urlretrieve(url,full_path)

img = pd.read_csv('data/images.csv') 
for i in range(328,len(img)):
    print(i)
    try:
        url = str(img['images'][i])
        file_name = str(img['TweetId'][i])
        dl_jpg(url,'Images/',file_name)
    except:
        pass