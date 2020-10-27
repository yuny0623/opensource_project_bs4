import requests
import time 
from random import randint
from bs4 import BeautifulSoup
from create_list_soup import *
from collect_text import *
from create_obj import *
from make_tfile import *


'''
외부 즉 이 클래스를 사용하는 py파일에서 이미 select_text의 to_text를 통해 word list와 
url list를 생성하였다고 가정한다. 그 값 중에서 url list를 이 클래스의 함수가 매개변수로 받았을 때 
기능하는 클래스의 함수를 정의한다. 트리를 생성한다. 
'''
    
word_to_find = 'NULL'       #지정된 단어를 저장할 클래스 전역변수 
word_count = 0              #지정된 단어의 빈도를 저장할 클래스 전역변수
soup_list = []           #soup객체들을 저장할 리스트

def set_word(out_word): #찾을 단어를 지정한다. 
    global word_to_find
    word_to_find = out_word 


#count_word는 정상 작동함. 직접확인해보면 암. 
def count_word(out_word_list): #해당 단어의 노출 빈도를 반환한다. 
    global word_count
    for i in range(len(out_word_list)):
        if word_to_find in out_word_list[i]:
            word_count+=1
    return word_count


'''
해당 함수는 범위를 /10통해 축소시켰다. 이유는 많은 requests요청으로 인해 서버 측에서 
내가 발생시킨 트래픽을 감당하지 못했기 때문...  속도제어 없이 계속 요청했기 때문이다. 그렇기 때문에 
out_url_list를 n등분해서 나누어서 요청을 하던지/ 아니면 sleep을 통해 시간간격을 주고 난 뒤에 요청을 하던지
둘중에 한 방법을 택해야 에러가 발생하지 않는다. 우선은 임시로 10등분을 하였다. 
soup_list에는 각각 해당되는 사이트의 소스코드가 순서대로 담겨있다. sleep이 더 나은 방법인것 같긴한데. .. 

시간정지로 테스트 해봤는데.sleep으로 해결 안됨. 어느 정도 숫자 넘어가면 그냥 요청 자체가 막히는 것같음. 
10분할해서 사용합시다... 

등분으로 테스트해봤는데. 5,7,8,9등분 전부다 안되고, 10등분부터 작동함. 요청이 24.3개 이상 넘어가면
아예 거부됨. 파싱하고 싶은 리스트는 항상 24.3개 이하로 파싱해서 적용하기. 더 작게 자르면 더 빨리 작동하니까 좋고,. 

bot이 아니라 사람이 접속하는 걸로 전달하려고 접속정보제공했는데, 효과 없음. 
다 시도해봤는데, 리스트 분할해서 최대한 작게 슬라이싱해서 http요청하는 것 말고는 방법이 없는 듯하다. 
그런데 이렇게 하면 if문이 너무 많이 발생하고, 객체도 많이 발생한다. 
조금 더 줄일 수 있는 방법은 없을까? ? 
딱봐도 직관적으로 코드가 너무 중첩되어 있다. 근데 방법을 몰겠다.. 
'''
def search_deeper(out_url_list): #일단은 100개 이하인것만 처리 가능.불필요한 반복이 너무 많음. 
    li = out_url_list
    print("search-deeper act in here")
    if(len(li)>400):
        raise Exception("too big list size")

    if (len(li)<400) & (len(li) >300): # 400>x>300
        print("soup act in here")
        j=0
        for i in range(int(len(li)/10)): #int로 나누기연산 감싸야됨. 안하면 float 적용됨. 에러 
            soup_list.append(list_seperate(li[j:(j+10)]))
            j+=10
            time.sleep(1)
            if i == (int(len(li)/10)):
                soup_list.append(list_seperate(li[j:]))

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

    if (len(li)<10) & (len(li)>0): #10>x>0
        soup_list.append(list_seperate(li))

    if len(li) <0:
        raise Exception("잘못된 값이 입력되었습니다.")
    return soup_list

#반드시 search_deeper 호출 다음에 호출되어야함. 아니면 NULL값 리던 .
def show_page_include_word(y_list):
    store_url_location = []#단어가 존재하는 url의 위치를 저장한다. 
    if len(y_list) == 0:
        raise Exception("search_deeper가 호출되지 않았습니다. ")
    for i in range(len(soup_list)):
        for j in range(len(soup_list[i])):
            if word_to_find in soup_list[i][j]:
                store_url_location.append(y_list[i*10+j])
    return store_url_location
        


#작동안됨... requests랑 연결이 끊어짐. 




# html_info = requests.get(out_url_list[i]).text
# soup = BeautifulSoup(html_info,'html.parser')
# soup_text = soup.get_text()
