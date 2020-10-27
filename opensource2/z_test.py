import requests
from bs4 import BeautifulSoup
from collect_text import *
from create_list_soup import *
from create_obj import * 
from make_tfile import *
from url_to_tree import *
from html_file import *
'''https://www.naver.com/'''
'''해당 클래스들의 사용방법에 대해 나와있습니다. '''
x,y = to_text("https://github.com/") #크롤링하고 싶은 메인 페이지의 url을 넘겨준다. 
# print(x) x에는 word list가 반환된다. 문자열 집합이다. (띄어쓰기로 구분된 문자집합)
# print(y) y에는 메인페이지에 걸린 모든 링크에 대한 집합이 리스트로 반환된다. 
set_word("python")  #세고 싶은 단어를 입력한다. 
n = count_word(x)  #단어의 개수가 반한된다.
print(n)           #단어의 개수를 출력한다.  
#print(y)                #url list의 길이 출력 
li = search_deeper(y)  #search_deeper는 해당페이지에 연결된 모든 링크에 관한 soup객체를 반환한다. 
url_contain_word = show_page_include_word(y) #show_page_include_word는 해당단어를 포함하는 페이지를 리스트로 반환해준다. 
#print(url_contain_word) #리스트 형식으로 모든 url 출력하기. 

html_link_file(y,url_contain_word) # 모든 url list를 y로 넘기고 선정된 url list를 url_contain_word 로 넘긴다. 