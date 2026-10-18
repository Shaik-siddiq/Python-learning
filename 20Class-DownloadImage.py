import requests
import threading
import time


urlss = ["https://httpbin.org/image/svg", "https://httpbin.org/image/jpeg", "https://httpbin.org/image/webp"]

def downloadImage(url):
    print("start downloading")
    request = requests.get(url)
    print(f"finshed image downloading from {url} in {len(request.content)} size in bytes")

threds = []
start = time.time()
for url in urlss:
    t = threading.Thread(target=downloadImage, args=(url, ))
    t.start()
    threds.append(t)

for t in threds:
    t.join()

end = time.time()

print(f"finished all downloads in {end-start:2f} seconds")

'''
start downloading
start downloading
start downloading
finshed image downloading from https://httpbin.org/image/svg in 8984 size in bytes
finshed image downloading from https://httpbin.org/image/webp in 10568 size in bytes
finshed image downloading from https://httpbin.org/image/jpeg in 35588 size in bytes
finished all downloads in 1.369127 seconds
'''

"""
When to use threads?
Threads manily use at I/O bounds, disk read/write/edit/delete, web requests
"""