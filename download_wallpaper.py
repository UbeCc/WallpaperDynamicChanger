import requests
import json

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
    desc = desc.replace(" ", "")
    output = '~/Pictures/Wallpapers/Display/{}.jpg'.format(desc + "_" + dt)
    with open(output, 'wb') as f:
        f.write(img)
    print('Downloaded', output)

if __name__ == "__main__":
    dumpBingWallpaper()