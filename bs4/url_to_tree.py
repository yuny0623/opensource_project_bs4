import requests
import time 
from random import randint
from bs4 import BeautifulSoup
from create_list_soup import list_seperate
import collect_text
import create_obj
import html_file

'''
외부/ 이 파일 내의 함수를 호출하는 py파일에서 이미 collect_text의 to_text를 통해 word list와 
url list를 생성하였을때 이 파일 내의 함수들을 사용할 수 있다. .
그 값 중에서 url list를 이 클래스의 함수가 매개변수로 받았을 때 
기능하는 클래스의 함수를 정의한다. 트리를 생성한다. -> 1layer 
'''
    
word_to_find = 'NULL'       #지정된 단어를 저장할 클래스 전역변수 
word_count = 1             #지정된 단어의 빈도를 저장할 전역변수
soup_list = []           #soup객체들을 저장할 리스트


def set_word(out_word): 
    '''찾을 단어를 지정해주는 함수.'''
    global word_to_find #함수 내에서 global을 선언해야만 함수 외부의 변수에 접근가능하다. 
    word_to_find = out_word  #매개변수로 전달받은 값을 함수 할당한다. 
 
def count_word(out_word_list): 
    '''해당 단어의 노출 빈도를 반환한다. '''
    w_li = out_word_list
    global word_count          #함수 외부의 word_count에 접근하기 위해 global 사용
    global word_to_find        #함수 외부의 word_to_find 에 접근하기 위해 global 사용
                               #전역으로 선언된 변수가 함수에서 사용되면 무조건 global 사용 
    for i in range(len(w_li)):    
        if word_to_find.find(w_li[i]):  #word_to_find in w_li[i] 라고 코딩하면 제대로 동작하지 않는다. 
                                        #w_li[i]는 리스트 요소이다. 즉 in을 통해 탐색하면, 
                                        #그 요소가 찾고자 하는 단어와 정확히 일치하는 지를 탐색한다. 
                                        #즉 예를 들어 python이라는 단어를 찾고싶다면 정확히 python이라는 
                                        #요소가 존재해야만 word_count+=1을 실행하는 것이다. 
                                        #하지만 find를 통해 탐색하면 그 요소가 정확히 python이라는 단어가 아니라
                                        #himywordpython 와 같은 요소 존재할 때 python이라는 문자열이 후미에 
                                        #존재하므로 word_count+=1을 실행한다. 
            word_count+=1 
    return word_count




def search_deeper(out_url_list): 
    '''
search-deeper 함수 

2020.10.27
개선해야할점 많음. -> (문제점 많음. )
해당 함수는 처음에 범위를 /10통해 축소시켰다. 이유는 많은 requests요청을 걸면 서버 측에서 
(내가 발생시킨 트래픽을 감당하지 못했기 때문...? -> 이라고 생각했는데, 사이트마다 요청할 수 있는 
개수가 다르다. 어떤 곳에서는 아무리 잘게 쪼개도 요청되지 않는 경우도 있었음. 음... 봇으로 크롤링
하는 걸 방지하려고 서버 측에서 그런 설정을 해놓은 것 같다. 이부분은 자세히 알지 못해서 추측 뿐... )  

2020.10.27
속도제한 없이 계속 요청했기 때문에 그럴 수도 있다는 얘기가 있어서 
sleep을 통해 시간간격을 주고 난 뒤에 요청을 했는데,( sleep은 다양한 값을 사용해봤음. ) 이건 썼을때랑
안썻을 때랑 차이가 없다. 이게 문제가 아닌 듯? 

soup_list에는 각각 해당되는 사이트의 소스코드가 순서대로 담겨있다.

.sleep으로 해결 안됨. 어느 정도 숫자 넘어가면 그냥 요청 자체가 막히는 것같음. 

2020.10.27
naver.com의 경우에는 --> 
등분으로 테스트해봤는데. 5,7,8,9등분 전부다 안되고, 10등분부터 작동함. 요청이 24.3개 이상 넘어가면
아예 거부됨. 파싱하고 싶은 리스트는 항상 24.3개 이하로 파싱해서 적용하기. 
더 작게 자르면 더 빨리 작동하니까 좋고. 

2020.10.27
bot이 아니라 사람이 접속하는 걸로 전달하려고 접속정보제공했는데, 효과 없음. 
다 시도해봤는데, 리스트 분할해서 최대한 작게 슬라이싱해서 http요청하는 것 말고는 방법이 없는 듯하다. 
그런데 이렇게 하면 if문이 너무 많이 발생하고, 일단 객체가 너무 많이 발생한다. 
조금 더 줄일 수 있는 방법은 없을까? ? 

2020.10.28
리스트를 처리하는 함수를 새로 만들어서 코드수를 줄였다. 음... 저번보다는 많이 줄었긴 했는데, 
그래도 언뜻 보면 반복되는 량이 눈에 확 띈다. 이건 좀 더 좋은 방안 있는 지 살펴보기. 
'''
    li = out_url_list
    print("search-deeper act in here")

    if(len(li)>400):                    #400개 이상이면 예외를 발생시킨다. 사실 400개 넘는 경우가 별로 없다. 
        raise Exception("too big list size")

    if (len(li)<400) & (len(li) >300):  # 400>x>300
        print("soup act in here")
        j=0
        for i in range(int(len(li)/10)): #int로 나누기연산 감싸야됨. 안하면 float 적용됨. 에러 발생함. 
            soup_list.append(list_seperate(li[j:(j+10)])) 
            #리스트인 전역 변수인 soup_list에 list_seperate에서 반환받은 객체를 리스트에 더한다. 
            j+=10                
            '''
            리스트를 쪼개면 [0:10] -> [10:20] -> [20:30] -> [n:n+10]이와 같은 순서를 따른다. 
            그렇기 때문에 j+=10에서 10씩 증가시켜주고, list_seperate에 li[j:j+10]을 전달하면 
            자동으로 [0:10] -> [10:20] -> [20:30] -> [n:n+10] 순으로 반복해서 전달된다. 
            '''
            time.sleep(1)        #일단 sleep 써놓긴 했는데, 사실 이거 효과는 없는듯 

            '''만약 슬라이싱하고 즉 10등분을 했는데, 그 끝에 남은 수가 있다면 꼬리에 더해서 
            list_seperate에 전달한다. 즉 95라고 치면 90은 위에서 이미 처리하고 5가 남는데, 
            이 5만큼을 리스트 끝에다가 더해주는거. 
            '''
        if i == (int(len(li)/10)):
            soup_list.append(list_seperate(li[j:]))
        #이하로는 범위만 변경되고 나머지는 똑같은 내용입니다. 


    if (len(li)<300) & (len(li) >200): # 300>x>200
        print("soup act in here")
        j=0
        for i in range(int(len(li)/10)):
            soup_list.append(list_seperate(li[j:(j+10)]))
            j+=10
            time.sleep(1)
        if i == (int(len(li)/10)):
            soup_list.append(list_seperate(li[j:]))

    if (len(li)<200) & (len(li) >100): # 200>x>100
        print("soup act in here")
        j=0
        for i in range(int(len(li)/10)): 
            soup_list.append(list_seperate(li[j:(j+10)]))
            j+=10
            time.sleep(1)
        if i == (int(len(li)/10)):
            soup_list.append(list_seperate(li[j:]))

    if (len(li)<100) & (len(li) >0): # 100> x> 0
        print("soup act in here")
        j=0
        for i in range(int(len(li)/10)): 
            soup_list.append(list_seperate(li[j:(j+10)]))
            j+=10
            time.sleep(1)
        if i == (int(len(li)/10)):
            soup_list.append(list_seperate(li[j:]))

    #어차피 리스트의 크기가 0<x<10이라면 굳이 슬라이싱 해줄 필요는 없다. 
    #10개정도의 요청은 거부된 적이 없음. 
    if (len(li)<10) & (len(li)>0): #10>x>0
        soup_list.append(list_seperate(li))

    #0보다 작은값이 전달되면 예외가 발생한다. 
    if len(li) <0:
        raise Exception("잘못된 값이 입력되었습니다.")
    return soup_list



def show_page_include_word(y_list): #전체 리스트인 y_list 
    '''반드시 search_deeper 호출 다음에 호출되어야함. 아니면 NULL값 리던 .
       단어를 포함하는 페이지의 url을 리스트로 반환한다. '''

    global soup_list
    store_url_location = [] #단어가 존재하는 url의 위치를 저장한다. 
    if len(y_list) == 0:    #리스트의 크기가 0이면 애초에 #search_deepter에서 반환한 값에
                            #문제가 있는 것이다. 그럴 경우에 예외 호출발생시킨다. 
        raise Exception("search_deeper가 호출되지 않았습니다. ")

    #전달 받은 모든 리스드에서 탐색한다. 
    for i in range(len(soup_list)):
        #soup_list 리스트는 리스트를 요소로 가지고 있는데, 이유는 list_seperate에서 리스트를 반환해줬기 때문에.. 
        #그 리스트의 요소들은 soup객체의 텍스트를 가지고 있는데, 즉 페이지에 있는 문자열들! 
        #거기서 단어의 존재여부를 확인하고, 만약 해당 단어가 그 페이지(그 리스트의 리스트 요소)에 존재한다면
        #그 위치 즉 페이지의 링크 url을 store_url_location에 저장한다. 그리고 그걸 반환한다. 
        
        for j in range(len(soup_list[i])):
            # 2020.10.30 -> word_to_find in soup_list[i][j]: 에서 find로 바꿔줬음.
            # 애초에 요소는 text로 정렬된 str형태이므로 find를 통해 탐색하는 게 더 정확함.  
            if word_to_find.find(soup_list[i][j]):  
                store_url_location.append(y_list[i*10+j])
    return store_url_location
        