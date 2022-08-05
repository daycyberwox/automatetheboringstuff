import bs4
import requests

productUrl = ('https://www.amazon.com/gp/product/1593279922/')
res = requests.get(productUrl, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
})
res.raise_for_status()

soup = bs4.BeautifulSoup('features="html.parser"')
soup.select