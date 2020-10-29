import requests
from bs4 import BeautifulSoup
import warnings
def image_take(url):
    url_use = url
    html_doc = requests.get(url_use).text
    soup = BeautifulSoup(html_doc,'html.parser')

    li = []

    for link in soup.find_all('img'):
        li.append(link.get('src'))

    html_doc_top = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <h1>ALL IMAGE COLLECTED</h1>
    '''
    html_doc_middle = ""

    html_doc_bottom = '''   
    </body>
    </html>'''

    warnings.filterwarnings(action = 'ignore')
    #저번부터 자꾸 경고메시지가 떠서 윗줄에 경고메시지 끄기를 만들어주었다. 근데 이걸로 해결될 게 아니라
    #애초에 밑에 open안에 경로를 써줫는데, 경로를 쓸때 \를 쓰는데, 그걸 하나를 쓰게 되면 \t \i \a 뭐 이런식으로
    #쓰는 요소들이랑 구분이 안간다? 뭐이런뜻이라고 나와있다. 그래서 \를 두개 \\ 써주면 경고가 안나온다. 
    #즉 백슬래쉬를 명시적으로 쓰기 위해 두개를 쓴다는 것 \\ 이게 백슬래쉬입니다. 라고 알려주기 위해서 
    #기초적인거였는데, 까먹었네.. 
    f = open("bs4\\html_file_in\\img_file.html",mode = "wt",encoding="utf-8")
    for i in range(len(li)):
        if li[i] == None:
            continue
        html_doc_middle +=('<img src = "'+li[i]+'">'+"<br>"+'\n')

    s = html_doc_top + html_doc_middle + html_doc_bottom
    f.write(s)
    f.close()



    '''
버전이 자주 업그레이드 되는(특히 Pandas..) 라이브러리나, 파이썬 IDE(주피터, 스파이더 등)을 사용하다보면 버전이 상향됨에 따라 변경될 수 있음을 알려주는 경고메세지를 출력해준다.
하지만 지금 상황에서 의미없고 깔끔하게 log를 출력하고 있는데, 이런 경고메세지가 뜨면 굉장히 거슬린다.
이럴때 warnings이란 라이브러리를 활용할 수 있다.

경고메세지 생성
예시 제공을 위해 경고메세지를 발생시키기 위해 이리저리 찾아봤지만 안나온다. 잘만 나오던 경고메시지가 찾으려 하니 안나오네
그래서 직접 경고메세지를 만들어본다.

def warn_func():
    warn_message = 'warn_func() is deprecated, use new_function() instead' 
    warnings.warn(warn_message)

warn_func()
__main__:3: UserWarning: warn_func() is deprecated, use new_function() instead
warn이라는 메소드로 경고메세지를 출력시킬 수 있다.

경고메세지 off & on
이 경고메세지를 키고 끄는 방법은 아래와 같이 간단하다.

# 경고메세지 끄기
warnings.filterwarnings(action='ignore')

# 다시 출력하게 하기
warnings.filterwarnings(action='default')
확인해보면.

warnings.filterwarnings(action='ignore')
warn_func()
안나오고!

warnings.filterwarnings(action='default')
warn_func()
__main__:3: UserWarning: warn_func() is deprecated, use new_function() instead
다시 나온다!
    '''
