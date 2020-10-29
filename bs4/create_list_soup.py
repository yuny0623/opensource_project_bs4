import requests
from bs4 import BeautifulSoup


def list_seperate(url_list): 
    '''
전달받은 url list를 하나씩 soup객체로 만들어준다. 

이 클래스에 문제 있음. dls soup 딱 하나만 반환해줌. 내일 일어나서 고치기 !! 
클래스 전역 으로 하나 만들어서 그 리스트에 다 넣어주고 그 리스트를 반환하셈. 
'''
    li = url_list
    total_list = []
    for i in range(len(li)): 
        html_info = requests.get(li[i]).text
        soup = BeautifulSoup(html_info,'html.parser')
        #soup = soup.text # <- 나중에 지워줘도 됨. 순수 soup객체만 받고 싶으면 이거지우셈.
                            #일단은 비교연산때문에 text로 str로 바꿔놨음. 
        #.split()을 통해 더 깔끔하게 만들고 싶은데 .split()은 전달받은 객체를 
        #리스트로 만들어버린다. 그렇기 때문에 비교를 진행할 수가 없다. ㅇㅋ? 3중리스트가 되어버리는거.. 
        #그래서 밖에 for문이 너무 지저분해질 거임 그냥 get_text()만 쓰자. 
        #그리고 get_text()는 오직 soup객체에만 적용가능
        #이미 text화시킨 soup객체에는 적용불가임. 
        soup_text = soup.get_text()          
        total_list.append(soup_text)


    #type of soup is str
    #type of total_list is list
    print("url adding to list is finished")
    
    return total_list









