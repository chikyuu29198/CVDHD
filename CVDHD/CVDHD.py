import urllib.request, json
import pyCompare

url = "https://cvdhd-ef484.firebaseio.com/.json"
data = urllib.request.urlopen(url).read().decode()
obj = json.loads(data)
print(obj)
bmp = []
dht = []

for key in obj:
    bmp.append(obj[key]["bmp"]["temp"])
    dht.append(obj[key]["dht"]["temp"])
print(bmp)
print(dht)
pyCompare.blandAltman(bmp,dht)