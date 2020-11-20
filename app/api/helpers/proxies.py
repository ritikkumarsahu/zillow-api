import requests
from bs4 import BeautifulSoup
from random import choice
import time

headers = {
        'authority': 'www.zillow.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
}

session = requests.Session()
session.headers.update(headers)

def get_proxy():
    url = "https://www.sslproxies.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    return {'https': choice(list(map(lambda x:x[0]+':'+x[1] ,zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8])))))}

def proxy_request(req_type, url, **kwargs):
    flag = True
    r = None
    timeout = time.time() + 60*5   # 5 minutes from now
    while 1:
        if time.time() > timeout:
            break
        try:
            # first try without proxy
            if flag:
                try:
                    session.get("https://www.zillow.com", timeout=6)
                    r = session.request(req_type, url, timeout=6, **kwargs)
                    break
                except:
                    flags = False

            proxy = get_proxy()
            session.get("https://www.zillow.com", proxies = proxy, timeout=6)
            r = session.request(req_type, url, proxies = proxy, timeout=6, **kwargs)
            break
        except:
            pass
    return r