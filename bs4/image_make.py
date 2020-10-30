import requests
from bs4 import BeautifulSoup
import warnings
def image_take(url):
    '''
    원하는 페이지에서 이미지태그를 긁어서 리스트로 모아줌. 해당 리스트를 html doc에 순서대로 
    넣어주는데, 따로 파일을 만들어서 생성해줌. 그 파일열면 페이지에 무슨 이미지가 있는지, 
    전부 확인할 수 있음. 
     
    주의점 -> 
    이 함수는 url 리스트에서 통째로 이미지를 뽑아내는 게 아니라, 하나의 url에서 그 페이지에 걸린
    이미지들만 파일로 모아줌. 여러개의 url이 아님. 

    보완점해야할점 -> 1. 중복되는 이미지가 있음. 2. 이미지의 사이즈 조절이 안되서 html doc에 너무 크게 나옴.  
    '''
    url_use = url
    html_doc = requests.get(url_use).text
    soup = BeautifulSoup(html_doc,'html.parser')

    li = [] # 빈 리스트 생성. img 태그에서 src속성을 갖고 있는 텍스트를 모두 저장한다. 

    for link in soup.find_all('img'):
        li.append(link.get('src'))

    #html 문서 기본 양식 -> 이미지 바둑판으로 보이게 수정하기. 
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
    html_doc_middle = "" # body에 들어갈 내용을 html_doc_middle에 쓴다. 

    html_doc_bottom = '''
    </body>
    </html>'''

    #warnings.filterwarnings(action = 'ignore')
    # open 내에 경로는 항상 백슬래쉬 두개로 써주기. -> \\ 안하면 경고표시뜸. 
    f = open("bs4\\html_file_in\\img_file.html",mode = "wt",encoding="utf-8")

    for i in range(len(li)): #리스트의 길이만큼 반복한다. 즉 페이지에 있는 이미지태그의 개수만큼 반복 
        if li[i] == None:    #가끔 이미지태그에서 긁어온 값인데 값 자체가 None을 반환하는 경우가 있다. 
                             #이 경우에 무조건 에러가 발생함. 
                             #왜 None값이 나오고, 어디서 발생하는 지는 잘 모르겠음. 그런데 가끔 None값을 
                             #반환하는 이미지태그가 있음. --> 
                             #보완점 -> 만약 None 값 반환하는 태그도 실제로는 이미지라면 따로 빼서 처리해주기. 
            continue


        # body에 이미지 태그를 페이지 내의 링크를 걸어서 추가시킨다. 
        html_doc_middle +=('<img src = "'+li[i]+'">'+"<br>"+'\n') 


    #s에 top middle bottom을 더함으로써 하나의 html 문서 완성 
    s = html_doc_top + html_doc_middle + html_doc_bottom

    #파일에 쓰고 닫아준다. 
    f.write(s)
    f.close()

