# import requests
# from bs4 import BeautifulSoup
from bs4 import bs4expand as ex

'''해당 함수들의 사용방법에 대해 나와있습니다. 
2020.10.25 ~ 2020.10.30. 추후에 추가사항있으면 py추가해주기. 
'''
x,y = ex.to_text("https://github.com/") #크롤링하고 싶은 메인 페이지의 url을 넘겨준다. 

# print(x) x에는 word list가 반환된다. 문자열 집합이다. (띄어쓰기로 구분된 문자집합)
# print(y) y에는 메인페이지에 걸린 모든 링크에 대한 집합이 리스트로 반환된다. 
ex.set_word("python")  #세고 싶은 단어를 입력한다. 
n = ex.count_word(x)  #단어의 개수가 반환된다.

print(n)                        #단어의 개수를 출력한다.  
print(len(y))                  #url list의 길이 출력 

li = ex.search_deeper(y)  #search_deeper는 해당페이지에 연결된 모든 링크에 관한 soup객체를 반환한다. 

url_contain_word =ex.show_page_include_word(y) #show_page_include_word는 해당단어를 포함하는 페이지를 리스트로 반환해준다. 
print(url_contain_word)          #단어를 포함하는 url을 리스트로 출력함. 

ex.html_link_file(y,url_contain_word) # 모든 url list를 y로 넘기고 선정된 url list를 url_contain_word 로 넘긴다. 

ex.image_take("https://github.com/") # 해당 페이지의 이미지를 html문서 상에서 모아볼 수 있게 해줍니다. 
#set_of_word의 작동법에 대해 나와있습니다. 
#다른 조건이 필요없이 이 함수만 바로 사용가능합니다. 
s = ex.make_set_of_word("https://opensource.com/") #분석을 원하는 사이트의 링크를 전달합니다. 
#s를 반환받습니다. s는 사이트에 대한 짧은 분석입니다. 
print(s)