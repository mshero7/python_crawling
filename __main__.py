import ssl
import sys
import time
import os

import pandas as pandas

from selenium import webdriver
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from collection import crawler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def crawling_kyochon():
    results =[]

    for sido1 in range(1, 2):
        for sido2 in count(start=1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1={}&sido2={}&txtsearch='.format(sido1, sido2)
            html = crawler.crawling(url)

            # 끝 검출
            if html is None:
                break

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})
            tags_span = tag_ul.findAll('span', attrs={'class' : 'store_item'})

            for tag_span in tags_span:
                # print(tag_span)
                strings = list(tag_span.strings)
                name = strings[1]
                address = strings[3].strip('\r\n\t')
                sidogu = address.split()[:2]

                results.append((name, address) + tuple(sidogu))

    for t in results:
        print(t)


def crawling_pelicana():
    results = []

    for page in range(1, 5):
        try:
            url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
            request = Request(url)
            context = ssl._create_unverified_context()
            response = urlopen(request, context=context)

            receive_data = response.read()
            html = receive_data.decode('utf-8', errors='replace')
            print(f'{datetime.now()} : success for request [{url}]')
        except Exception as e:
            print(f'{e} : %{datetime.now()}', file=sys.stderr)
            continue

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            # print(list(tag_tr))
            strings = list(tag_tr.strings)
            # print(strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)

    # store
    table = pandas.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)
    print(table)

    for result in results:
        print(result)


def crawling_nene():
    result_set = set()
    page_count = 1
    flag = True

    while flag:
        try:
            url = 'https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A' % page_count
            request = Request(url)
            response = urlopen(request)

            receive_data = response.read()
            html = receive_data.decode('utf-8', errors='replace')
            print(f'{datetime.now()} : success for request [{url}]')
        except Exception as e:
            print(f'{e} : %{datetime.now()}', file=sys.stderr)
            continue

        page_count += 1

        bs = BeautifulSoup(html, 'html.parser')
        shop_infos = bs.findAll('div', attrs={'class': 'shopInfo'})
        # print(shop_infos)

        for shop in shop_infos:
            shop_strings = list(shop.strings)
            shop_name = shop_strings[4]
            shop_loc = shop_strings[6]
            t = (shop_name, shop_loc)
            # print(t)

            # 중복될때 종료.
            if t in result_set:
                flag = False

            result_set.add(t)

    # store
    table = pandas.DataFrame(result_set, columns=['name', 'address'])
    table.to_csv('/crawling-results/nene.csv', encoding='utf-8', mode='w', index=True)
    print(table)

    # for result in result_set:
    #     print(result)


def crawling_goobne():
    results = []

    # 첫 페이지 로딩
    wd = webdriver.Chrome('E:\cafe24\chromedriver_win32\chromedriver.exe')
    wd.get('http://goobne.co.kr/store/search_store.jsp')
    time.sleep(5)

    for page in range(103, 105):
        # 자바스크립트 실행
        script = 'store.getList(%d)' % page
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request [{script}]')
        time.sleep(3)

        # 실행결과 HTML (동적으로 렌더링 된 HTML) 가져오기
        html = wd.page_source

        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')
        next_text = wd.find

        print(next_text)
        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]
            results.append((name, address)+tuple(sidogu))

            print(strings)
    wd.quit()

if __name__ == '__main__':
    # print(os.path.abspath(__file__))
    # print(os.path.relpath(__file__))
    # print(os.getcwd())

    # 교촌
    # crawling_kyochon()

    # nene 과제
    crawling_nene()

    # 굽네치킨
    # crawling_goobne()
