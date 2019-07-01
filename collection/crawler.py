import ssl
import sys
from urllib.request import Request, urlopen
from datetime import datetime

# encoding deafault 는 utf-8
def crawling(
        url='',
        encoding='utf-8',
        # proc을 none 으로 하게되면 생기는일
        # 코드가 조금은 복잡해질 수 있다.
        # lambda 로 같은 값을 뱉어주는 함수를 default 로 지정해주는것이 깔끔하다.
        proc1=lambda data: data,
        proc2=lambda data: data):

    try:
        request = Request(url)
        context = ssl._create_unverified_context()
        response = urlopen(request, context=context)

        receive_data = response.read()

        result = proc2(proc1(receive_data.decode(encoding, errors='replace')))

        print(f'{datetime.now()} : success for request [{url}]')
        return result

    except Exception as e:
        print(f'{e} : %{datetime.now()}', file=sys.stderr)

