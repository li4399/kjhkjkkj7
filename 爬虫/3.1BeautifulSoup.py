# 安装
# pip3 install BeautifulSoup4
# pip3 install lxml

# 基础用法
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html,'lxml')
# print(soup.title)

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(attrs={'id':'list-1'}))
li = soup.find_all(attrs={'class': 'element'})
print(type(li))
for i in li:
    print(i.string)

print(soup.find_all('ul', {'class', 'list-small'}))