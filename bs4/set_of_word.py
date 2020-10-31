import requests
import time
from bs4 import BeautifulSoup
# https://relatedwords.io/ #연관단어 제공 사이트 
# 2020.10.31 동안 코딩 
def make_set_of_word(single_url): #여기서 single_url은 리스트가 아닌 하나의 url이다. 
    '''
    https://relatedwords.io/ 에서는 연관단어에 대해 500개 정도의 단어를 제공한다. 
    requests를 통해 해당 사이트에서 단어를 가져오고 리스트로 변환해서 할당한다. 
    분석을 원하는 사이트가 있으면 make_set_of_word에 매개변수로 링크를 전달한다. 
    전달된 링크는 또다시 requests를 통해 soup객체로 변환되고, 텍스트화 및 split된다. 
    그리고 최종적으로 카테고리에 있는 분류중에서 가장 많은 빈도 수를 기록한 카테고리가 
    해당 페이지의 분류가 된다.

    보완점: 지금은 카테고리가 15개밖에 없다. 좀 더 늘려서 더 구체적인 분석을 할 수 있게 만들어야함. 
           페이지를 분류해서 카테고리 분류 중에서 가장 높은 숫자를 그 페이지의 분류라고 정의하는데, 
           이런식으로 한가지의 카테고리로 분류하기 보다는 백분율로 계산해서 해당 페이지를 카테고리별로
           퍼센트로 표현할 수 있게 해주는 것이 좋다. 

           이 함수는 https://relatedwords.io/ 에 종속적이다. 즉 이 사이트의 방식이 바뀌거나
           사이트가 운영하지 않게 되면 더 이상 동작할 수 없다. 그렇기 때문에, 카테고리에 따른 연관 단어 집합이
           따로 독립적으로 필요하다. 독립적인 데이터셋이 있어야 이 함수가 독립적으로 작동할 수 있다. 
    '''

    url = single_url                         
    category_list = [                       #카테고리이다. 사이트가 어떤 사이트인지 분류하기 위함. 15개의 카테고리
        "programming","opensource","share","government",
        "shopping","private","blog","album","study","academy",
        "laboratory","archive","portfolio","bank","sell"]

    number_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #카테고리별 연관단어의 출현빈도를 저장할 리스트 

    s = "https://relatedwords.io/"          #연관단어를 긁어올 사이트/ 후미에 카테고리중 하나를 추가할 예정

    html = requests.get(url).text           #분석을 원하는 사이트를 requests를 통해 soup객체로 만든다. 
    soup_url = BeautifulSoup(html,"html.parser")
    soup_url = soup_url.get_text()
    soup_url = soup_url.split()             #사이트에 관한 텍스트 리스트이다. (split은 리스트로 변환된다.)

    soup_for_second = []                    #이중 리스트 생성 예정   
    
    for i in range(len(category_list)):     #15번반복됨. 카테고리가 15개이기 때문에 
        print(str(i)+" --> in catagory for code")
        url_in_here = s+category_list[i]            #카테고리별로 단어를 url에 추가해준다. 
        print(url_in_here)
        html_doc = requests.get(url_in_here).text    
        soup = BeautifulSoup(html_doc,'html.parser') #연관단어 페이지의  soup객체 
        href_list = []                      #값을 전달하기 위해 임시로 사용한 list객체 
                                            #이것을 선언하지 않으면 soup객체에서 태그를 뽑아
                                            #리스트로 전달하는 과정이 복잡해짐. 
        
        for link in soup.find_all('a'):       #a태그 분류 
            #print(type(soup.find_all('a'))) #<class 'bs4.element.ResultSet'>
            #print(type(link.get('href')))   #<class 'str'>
            href_list.append(link.get('href')) #href속성을 찾아서 href_list에 임시로 저장한다. 

        soup_for_second.append(href_list)     #href_list를 통째로 soup_for_second에 할당한다. 이중 리스트 생성

    print()
    print("category cal is finish")
    print()
    print("length of soup_for_second is " + str(len(soup_for_second))) #15 가 출력됨. 즉 15개의 카테고리별로 잘 생성되었다는 뜻. 
    print("factor length of doule list is " + str(len(soup_for_second[0]))) # 502가 출력됨. 카테고리 별로 각 단어들이 잘 생성됨. 
                                   # 이중 리스트로 15개의 각각 502개씩의 요소가 생성됨. (502가 아닌 경우도 존재)
    print() 
    print("appending word is finish")

    print()
    for i in range(len(soup_for_second)): #15번 반복됨. 
        for j in range(len(soup_for_second[i])): #얘는 502인경우도 있고, 그보다 작은 경우도 있음. 
            if soup_for_second[i][j].startswith('/'): #단어이면 실행한다. 단어에는 /가 붙어서 값이 전달되기 때문에 /를 없애줘야 한다. 
                soup_for_second[i][j] = soup_for_second[i][j].replace("/","") #/가 붙은 단어에서 /를 ""로 바꾼다. 즉 삭제 
            else:                         #/로 시작하지 않는 경우는 http가 붙는 경우이다. 이값은 필요가 없다. 
                #원래 여기서 del을 통해 필요없는 http요소를 삭제하려고 했는데, 그렇게 하면 index에러가 발생한다. 
                #즉 del을 하게 되면 아예 요소가 하나 사라지고 for문 내에서 i 와 j의 범위가 아예 바뀐다. 
                #그래서 굳이 삭제하지 않고, 해당카테고리명을 그 자리에 추가해주는 방식을 취했다. 
                soup_for_second[i][j] = soup_for_second[i][j].replace(soup_for_second[i][j],category_list[i])

    print("sorting soup_for_second is finished")
    #print(len(soup_for_second[0]))
    print()

    #페이지를 분석하기 위한 for문 
    #soup_for_second 내의 단어를 soup_url 즉 (사이트에 관한 split된 soup객체)가 포함하고 있다면 
    # number_count의 i번째 요소를 1씩 증가시킨다. 즉 빈도 수를 저장한다. 
    for i in range(len(soup_for_second)):
        for j in range(len(soup_for_second[i])):
            if soup_for_second[i][j] in (soup_url):
                number_count[i]+=1

    #number_count에서 가장 큰 수를 찾아내고, 그 위치 즉 인덱스를 저장한다. 
    for i in range(len(number_count)):
        print(number_count[i])
        if number_count[i] == max(number_count):
            index = i

    #출력문
    print(str(max(number_count))+" is in "+str(index)+" location")

    #반환할 문자열이다. 결론이다. 해당페이지가 카테고리 중 어느 카테고리에 가장 큰 비중을 갖는 지를 할당한다. 
    conclusion_str = "The page is about " + category_list[index] #분석에 대한 결과 (어떤 페이지 인지. )

    return conclusion_str #분석에 대한 결과를 반환한다. 



