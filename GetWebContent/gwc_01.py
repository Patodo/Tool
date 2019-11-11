import requests
import re
url = '***'
previous = 'http://d'
before = 'zip'
save = "test.txt"

if __name__ == "__main__":
    try:
        f = open(save,"w",encoding="utf-8")
        ff = open('test2.txt',"w",encoding="utf-8")
        for i in range(10000, 88201):
            print("----------Reading "+(str)(i),end='')
            find = previous + '.*?' + before
            html = requests.get(url+(str)(i)+'.html')
            html.raise_for_status()
            html.encoding = html.apparent_encoding
            result = re.search('_filename">.*?</p>', html.text)
            ff.write((str)(i)+result.group()+' ')
            print("__Name: success", eof='')
            result2 = re.search(find, html.text)
            f.write(result2.group()+'\n')
            print("link: success -----------")
    except:
        print("\nFail to get content．Check code.")
