from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

html = '''
<td class="title black">
    <div class="tit3" id="kickscar">
        <a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
    </div>
</td>
'''


# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(type(bs))
    # print(bs)

    # tag = bs.td

    tag = bs.a
    print(tag)


# 2. attributes 조회
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])

    tag = bs.div
    print(tag['id'])

    print(tag.attrs)


# 3. attribute로 태그 조회
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    print(tag)

    tag = bs.find(attrs={'class': 'tit3'})
    print(tag)


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()

