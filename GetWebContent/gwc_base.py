import requests
import re
url = "https://item.jd.com/6957643.html"
previous = 'class="sku-name"'
before = 'class="news"'
save = "F:\\github\\Tool\\GetWebContent\\test.txt"

if __name__ == "__main__":
    try:
        f = open(save,"w",encoding="utf-8")
        find = previous + ".*?" + before
        html = requests.get(url)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        result = re.search('div class="item hid.*?e"></div', html.text)
        f.write(result.group())
    except:
        print("Fail to get content.")