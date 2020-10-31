import requests
from bs4 import BeautifulSoup


'''
url_from_out을 매개변수로 받은 뒤에 soup객체와 함께 페이지의 소스코드를 텍스트화시킨 html_info를 제공받는다. 
그후 soup객체를 가공해서 리스트로 만든 뒤 soup_str_translate을 반환한다. 
url_list라는 리스트를 생성하는데 페이지에 존재하는 모든 링크를 리스트에 할당한다. 
동시에 http를 포함하는 문자열 중에서 exe가 포함되지 않은 문자열을 url_list라는 리스트로 반환한다. 

for link in soup.find_all('a'):
    print(link.get('href'))    

--> 을 사용하면 쉽게 하이퍼링크만 뽑아낼 수 있다. 근데 이 기능만 사용하면 exe파일과 같이 다른 페이지로 
넘어가는 link가 아닌 다른 link들도 함께 sorting된다. 그러므로 따로 조건을 더 달아줘야함. 
'''

def to_text(url_from_out):
    url = url_from_out     
    html_info = requests.get(url).text   
    soup = BeautifulSoup(html_info,'html.parser') 

    soup_text = soup.get_text()            #soup객체를 텍스트로 만들어서 soup_text에 할당하기. 
    soup_str_translate = soup_text.split() #soup_text객체를 공백 구분해서 soup_str_translate에 할당. 

    url_list = []                    #모든 링크는 url_list의 리스트를 통해 접근 가능하다. 
    for link in soup.find_all('a'):  #soup객체 내에 존재하는 모든 링크를 list로 만들어준다. 
        url_list.append(link.get('href'))
    

    new_url_list = []               #새로운 리스트를 생성해서 가공된 url list를 할당한다.                 
    for i in range(len(url_list)):  
        try:
            #http가 있는 문자열 즉 연결 가능한 링크만 따로 모아서 new_url_list에 할당한다.
            #가끔 None을 반환하는 링크가 있다. 그럴 경우는 제외시킨다. 
            #exe 파일도 제외시킨다. 
            if ((url_list[i][0:4] == "http") & (url_list[i] != None)):    
                if "exe" not in url_list[i]:   #실행파일이 아닌 경우에만
                    new_url_list.append(url_list[i]) 
        except TypeError:                      #TypeError가 발생하는 경우가 있음. 그럴 경우에는 무시하고 진행
            continue

    #해당되는 기호들이 있으면 제거한다. word_list에 정리된 단어들을 할당한다. 
    word_list = []
    for word in soup_str_translate:
        symbols = """▶↑~!@#$%^&*()_-+={[}]|\\;:"‘'·<>?/.,ⓒ """ 
        for i in range(len((symbols))):

            #해당 symbols내의 기호가 있으면 '' 내부의 것으로 바꾼다. 
            #근데 '' 안에 아무것도 없으니 제거하는것과 마찬가지 기능을 함. 
            word = word.replace(symbols[i], '')  

        if len(word) > 0:
            word_list.append(word)
    
    return word_list,new_url_list #가공된 word에 관한 리스트와 url에 관한 리스트를 반환시켜 준다. 2개 반환..
