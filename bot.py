import requests
import time

payload = {
    'content': "https://media.tenor.com/bN2IkZ5vzxIAAAAd/byuntear-meme.gif"
}

header = {
    'authorization': ''
}

while True:
    r = requests.post("", data=payload, headers=header)
    time.sleep(5)