import requests
import json
import os
import datetime

def removeOutdatedPics():
    path = os.getcwd() + '/Display'
    now = datetime.datetime.now()
    for filename in os.listdir(path):    
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(path, filename)
            filemtime = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            if (now - filemtime).total_seconds() > 24 * 3600: # > 1 day
                print(filename, "was downloaded more than 24 hours ago.")
                os.remove(filepath)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Connection": "close",
}

def dumpBingWallpaper():
    n = 1
    idx = 1
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx={}&n={}".format(idx, n)
    res = requests.get(url, headers=headers)
    res.encoding = 'utf8'
    jsonData = json.loads(res.text)
    uri = jsonData['images'][0]['url']
    
    img = requests.get("https://s.cn.bing.net/" + uri, headers=headers).content
    desc = str(jsonData['images'][0]['copyright']).split(',')[0]
    dt = jsonData['images'][0]['startdate']
    desc = desc.replace(" ", "").replace('/', '')
    output = os.getcwd() + '/Display/{}.jpg'.format(desc + "_" + dt)
    with open(os.path.abspath(output), 'wb') as f:
        f.write(img)
    print(f'Downloaded {desc} to {output}')

def dumpHistoryBingWallpaper():
    img = requests.get("https://bing.img.run/rand_uhd.php", headers=headers).content
    output = os.getcwd() + '/Display/{}.jpg'.format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
    with open(os.path.abspath(output), 'wb') as f:
        f.write(img)

if __name__ == "__main__":
    removeOutdatedPics()
    # dumpBingWallpaper()
    dumpHistoryBingWallpaper()