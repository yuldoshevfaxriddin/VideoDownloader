import requests
import time
chuck_size = 1024*1024#  1kb =1024 

url = "https://www.w3schools.com/html/mov_bbb.mp4"

print("requests")
r = requests.get(url,stream=True)
print("start")
start = time.time()
i = 0
with open("test.mp4","wb") as f:
    for chuck in r.iter_content(chuck_size):
        f.write(chuck)
        i+=1
        print(i)

print("end")
end = time.time()
print(end-start)
