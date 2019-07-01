from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    response = urlopen(request)
    # 바이트를 뱉어냄
    html = response.read().decode('cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())

    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)

    for index, div in enumerate(divs):
        print(index + 1, div.a.text, sep=' ')

    print('=================================================')


def store_naver_movie_rank(data):
    # output(store)
    for index, div in enumerate(data):
        print(index + 1, div.a.text, sep=' ')



def proc_naver_movie_rank(data):
    # processing
    bs = BeautifulSoup(data, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    return divs


def error():
    pass


def ex02():
    crawler.crawling(
        # 패치작업
        url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949',
        # 프로세싱 작업
        proc1=proc_naver_movie_rank,
        proc2=lambda data: list(map(lambda x: print(x.a), data)))

    # print(bs.prettify())

    # print(divs)

__name__ == '__main__' and not ex02()
