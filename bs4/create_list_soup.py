import requests
from bs4 import BeautifulSoup


def list_seperate(url_list): 
    '''
    requests 개수 제한을 해결하기 위한 함수. 
    반복문을 통해 전달받은 리스트의 요소들(url 링크)을 하나씩 soup객체로 만들어준다. 
    만들어진 soup객체를 하나씩 total_list 리스트에 더한다. 즉 soup객체가 요소로 들어있는 리스트를 제공한다. 
    그리고 만들어진 total_list 리스트를 반환한다. 
    대부분의 requests요청 거부 혹은 연결 끊어짐과 관련있는 에러는 전부 다 이 함수에서 발생한다. 
    실행될때마다 url adding to list is finished 가 터미널에 출력되는데, 이 문구를 확인할 수 없으면 
    에러가 발생한거임. 


    보완해야할 점. -> 
    보통 import 에러가 아닌 이상 url adding to list is finished가 출력되는 시점에 대부분의 에러가 발생했음. 
    -> requests요청을 한번에 보낼 수 있는 방법 (url 리스트 통째로 전달해도 거부당하지 않는 방법) 있으면 
    수정하기 
    '''
    li = url_list
    total_list = []
    for i in range(len(li)): 
        html_info = requests.get(li[i]).text
        soup = BeautifulSoup(html_info,'html.parser')
        #soup = soup.text # <- 나중에 지워줘도 됨. 순수 soup객체만 받고 싶으면 주석처리 
        #일단은 비교연산 때문에 str로 바꿔놨음. 
        #.split()을 통해 더 깔끔하게 만들 수 있는데, .split()은 전달받은 객체를 
        #리스트로 만들어버린다. 그렇기 때문에 비교연산을 진행할 수가 없다. 즉 3중리스트가 되어버려서 
        #요소 비교하는 방식을 새로 바꿔야함. 그래서 그래서 밖에 for문이 너무 지저분해짐. 
        #그리고 get_text()는 오직 soup객체에만 적용가능
        #이미 text화시킨 soup객체에는 적용불가

        soup_text = soup.get_text()          
        total_list.append(soup_text)


    #type of soup is str
    #type of total_list is list
    print("url adding to list is finished")
    
    return total_list









