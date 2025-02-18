from scrapy import Selector

html = '''
<html>
    <body>
        <div class="hello" id="hello">
            <p>Hello World!</p>
        </div>
        <p>Hope you are Enjoying Zindua So far</p>
        <p class='hello'>My Classmates at Zindua are fun</p>
    </body>
</html>
'''

sel = Selector(text = html)

print("----------------------------------------")

print(sel.xpath('/html/body/p'))

print("----------------------------------------")

print(sel.xpath('/html/body/p').extract())

print("----------------------------------------")

print(sel.xpath('/html/body/p[@class="hello"]').extract())

print("----------------------------------------")

print(sel.xpath('/html/*').extract())


print("----------------------------------------")

import requests

url = 'https://en.wikipedia.org/wiki/Donald_Trump'
html = requests.get(url).content

sel = Selector(text=html)

zindua_text = sel
print(zindua_text)
