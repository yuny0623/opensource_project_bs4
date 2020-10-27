import requests
from bs4 import BeautifulSoup

class select_text:
    '''
    url_from_out을 매개변수로 받은 뒤에 soup객체와 함께 페이지의 소스를 텍스트화 시킨 html_info를 제공받는다. 
    url_list라는 리스트를 생성하는데 페이지에 존재하는 모든 링크를 리스트에 삽입한다. 
    그후 soup객체를 가공시켜 리스트로 만든 뒤 soup_str_translate과 을 반환한다. 
    '''
    
    def to_text(self,url_from_out):       #성공적으로 잘 출력됨을 확인할 수 있음. 
        url = url_from_out     
        html_info = requests.get(url).text    #텍스트로 변환해주기. request사용하기. 
        soup = BeautifulSoup(html_info,'html.parser')   # soup객체 만들어주기. 뷰티풀수프의 메소드 적용가능. 

        soup_text = soup.get_text()           #soup객체를 순수한 텍스트로 만들어서 soup_text에 할당하기. 
        soup_str_translate = soup_text.split()#soup_text객체를 리스트로 만들어서 soup_str_translate에 할당. 

        url_list = []                    #soup객체 내의 모든 링크는 url_list의 리스트를 통해 접근 가능하다. 
        for link in soup.find_all('a'):  #soup객체 내에 존재하는 모든 링크를 list로 만들어준다. 
            url_list.append(link.get('href'))
        

        new_url_list = []               #새로운 리스트를 생성해서 가공된 데이터를 할당한다.                 
        for i in range(len(url_list)):
            try:
                if ((url_list[i][0:4] == "http") & (url_list[i] != None)):   #http가 있는 문자열 즉 링크만 따로 모아서 new_url_list에 할당한다. 
                    if "exe" not in url_list[i]:   #실행파일이 아닌 link들만 리스트에 저장한다. 
                        new_url_list.append(url_list[i])
            except TypeError:
                continue

        #해당되는 기호들이 있으면 제거한다. word_list에 정리된 단어들을 할당한다. 
        word_list = []
        for word in soup_str_translate:
            symbols = """▶↑~!@#$%^&*()_-+={[}]|\;:"‘'·<>?/.,ⓒ """
            for i in range(len((symbols))):
                word = word.replace(symbols[i], '')  
            if len(word) > 0:
                word_list.append(word)
        
        return word_list,new_url_list #가공된 word에 관한 리스트와 url에 관한 리스트를 반환시켜 준다. 2개 반환.. 



# 사용방법
# x에는 정렬된 word list가 반환되고, y에는 정렬된 url list가 반환된다. 다음과 같이 호출한다. 
# x,y = select_text().to_text("https://www.naver.com/")

    