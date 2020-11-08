BeautifulSoup4 
==============================
기존 BeautifulSoup4에 새로운 기능이 추가되었습니다. PYTHON으로 작성되었고, 2020.10.25 ~ 2020.10.30까지 작성되었습니다. (아직 진행중...)
------------------------------------------------------------------------------------------------------------------

<img src="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/6.1.jpg" width="40%" height="30%" title="BeautifulSoup4" alt="BeautifulSoup4"></img>

***
# bs4에 추가된 함수 및 클래스 
* collect_text.py  
* create_list_soup.py 
* create_obj.py  
* html_file.py 
* image_make.py  
* make_tfile.py 
* set_of_word.py
* url_to_tree.py  
* z_test.py 
*
* 여기서 
* make_tfile.py 
* create_obj.py 
* set_of_word_act.py
* 는 지금은 쓰이지 않습니다. 
***
# 1. z_text.py
해당 함수들의 사용법에 대해 나와있습니다. 어떻게 호출하고 매개변수를 전달하는 지에 대한 사용법이 나와있습니다.

#2. url_to_tree.py
외부에서 함수를 호출할 때, 이미 collect_text의 to_text함수를 통해 word list와 url list를 생성하였을때에 이 파일 내의 함수들을 사용할 수 있다. 그 값 중에서 url list를 이 파일의 함수가 매개변수로 받는다. 

	set_word 함수: 
	찾을 단어를 지정해주는 함수이다. 전역으로 선언된 변수에 값을 저장한다.

	count_word 함수:
	해당 단어의 노출 빈도를 반환한다. 

	search_deeper 함수 
	메인 페이지로 지정된 URL에서 링크되어있는 모든 링크들에 대한 리스트를 requests 요청을 통해 soup객체로 변환시켜 처리한다. 이때 requests요청 개수가 많아지거나 그 속도가 일정하	     고 빠르게 요청되면 페이지에서 requests요청을 거부당한다. 그래서 리스트를 슬라이싱해서 create_list_soup파일에 있는 list_seperate함수로 전달한다. 

	show_page_include_word 함수 
	반드시 search_deeper 함수 호출 다음에 호출되어야한다. 그렇지 않으면 NULL값을 리턴한다. 찾고싶은 단어를 포함하는 페이지의 url을 리스트로 반환한다.


# 3. image_make.py 

	image_take 함수 
	원하는 페이지에서 이미지태그를 긁어서 리스트로 모아준다. 해당 리스트를 html doc에 순서대로 넣어주는데, 따로 html파일을 만들어서 생성해준다. 그 html파일을 	열면 페이지에 어떤     	   이미지가 링크되어있는지 모아볼 수 있다. 


# 4. html_file.py

	html_link_file 함수 
	메인 페이지에 걸려있는 모든 링크들을 html doc에 넣어서 링크 모음을 만들어준	다. 
	찾고자하는 단어를 포함하는 링크는 SELECTED URL LIST로 분류되어서 하단에 따로 표시된다. 
	동작하는 방식은 image_take 함수와 같다. 동일하게 작동한다. 다만 함수의 매개변수로 selected_list를 하나 더 받는다. 
	show_page_include_word에서 단어를 포함하는 링크의 리스트를 반환하는데, 그 반환한 값이 selected_list 매개변수에 들어오는 것이다. 

# 5. create_list_soup.py
	list_seperate 함수 
	requests 개수 제한을 해결하기 위한 함수. 반복문을 통해 전달받은 리스트의 요소들(url 링크)을 하나씩 soup객체로 만들어준다. 
	만들어진 soup객체를 하나씩 total_list 리스트에 더한다. 즉 soup객체가 요소로 들어있는 리스트를 제공한다. 그리고 만들어진 total_list 리스트를 반환한다. 
	대부분의 requests요청 거부 혹은 연결 끊어짐과 관련된 에러는 전부 다 이 함수	에서 발생한다. 그래서 실행될때마다 “url adding to list is finished” 가 터미널에 출력되는데, 이 문         구가 지속적으로 출력됨을 확인할 수 없으면 제대로 동작하지 않음을 알 수 있다.
	

# 6. collect_text.py

	to_text 함수: 
	url_from_out을 매개변수로 받은 뒤에 soup객체와 함께 페이지의 소스코드를 텍스트로 만든 html_info를 제공받는다. 그후 soup객체를 가공해서 리스트로 만든 뒤 		          	  soup_str_translate을 반환한다. 
	url_list라는 리스트를 생성하는데 페이지에 존재하는 모든 링크를 리스트에 할당한	다. 
	동시에 http를 포함하는 문자열 중에서 exe가 포함되지 않은 문자열을 url_list라는 리스트로 반환한다. (실행파일일 경우에 soup객체로 분석할 수 없음.)

# 7. set_of_word.py 

	make_set_of_word 함수:
	https://relatedwords.io/ 에서는 연관단어에 대해 500개 정도의 단어를 제공한다. 
	requests를 통해 해당 사이트에서 단어를 가져오고 리스트로 변환해서 할당한다. 
	분석을 원하는 사이트가 있으면 make_set_of_word 함수에 매개변수로 링크를 전달한다. 
	전달된 링크는 또다시 requests를 통해 soup객체로 변환된다. (이후에 text로 바뀌고, split()을 통해 사용할 수 있는 형태로 바귄다.)
	최종적으로 카테고리에 있는 분류중에서 가장 많은 빈도 수를 기록한 카테고리가 해당 페이지의 성향으로 판별된다. (예를 들면 opensource 관련 페이지, 혹은 쇼핑 페이지, 블로그와 같     	  은 형식으로 분류된다.)

***
다음은 z_text.py의 내용으로 bs4폴더 내에서 해당 함수를 사용할 수 방법을 알려주는 예제이다. 
```
import requests
from bs4 import BeautifulSoup
from collect_text import to_text
import url_to_tree
import html_file
import image_make

x,y = to_text("https://github.com/") #크롤링하고 싶은 메인 페이지의 url을 넘겨준다. 
# print(x) x에는 word list가 반환된다. 문자열 집합이다. (띄어쓰기로 구분된 문자집합)
# print(y) y에는 메인페이지에 걸린 모든 링크에 대한 집합이 리스트로 반환된다. 
url_to_tree.set_word("python")  #세고 싶은 단어를 입력한다. 
n = url_to_tree.count_word(x)  #단어의 개수가 반환된다.
print(n)                        #단어의 개수를 출력한다.  
print(len(y))                  #url list의 길이 출력 
li = url_to_tree.search_deeper(y)  #search_deeper는 해당페이지에 연결된 모든 링크에 관한 soup객체를 반환한다. 
url_contain_word = url_to_tree.show_page_include_word(y) #show_page_include_word는 해당단어를 포함하는 페이지를 리스트로 반환해준다. 
print(url_contain_word)          #단어를 포함하는 url을 리스트로 출력함. 
html_file.html_link_file(y,url_contain_word) # 모든 url list를 y로 넘기고 선정된 url list를 url_contain_word 로 넘긴다. 
image_make.image_take("https://github.com/") # 해당 페이지의 이미지를 html문서 상에서 모아볼 수 있게 해줍니다. 
```

***
다음은 make_set_of_word에 관한 사용법이 나와있습니다. 
```
import set_of_word
#set_of_word의 작동법에 대해 나와있습니다. 
s = set_of_word.make_set_of_word("https://opensource.com/") #분석을 원하는 사이트의 링크를 전달합니다. 
#s를 반환받습니다. s는 사이트에 대한 짧은 분석입니다. 
print(s)
```
***

# 문제점 또는 개선점 분석
> soup객체로 받아온 객체를 text화하고, split 까지만 하고, 그 이후에는 잘 활용되지 않는다. 즉 parser를 만들기로 했는데 parser가 아직 만들어지지 않았다. 

> set_of_word.py함수가 영어밖에 지원이 안된다. 개선점으로는 한글도 지원할 수 있게 바꾸는 것이다.

> 전반적으로 함수명이나 변수명이 부적절하다. 실제 동작과는 어울리지 않는 함수명도 있고, 어울리지 않는 변수명도 존재한다. 그것들을 잘 어울리게 다시 명칭해야한다. 

image_take 함수 
> 중복되는 이미지가 있다. . 이미지의 사이즈 조절이 안되서 html doc에 너무 크게 나온다. 중복되는 이미지가 없도록 만들고, 이미지를 테이블로 볼 수 있게 처리한다. 

list_seperate 함수
> 보통 import 에러가 아닌 이상 url adding to list is finished가 출력되는 시점에 대부분의 에러가 발생했다. 이 부분에 예외처리가 되지 않았다. 예외처리를 해줄 수 있도록 해야한다.
> requests요청을 한번에 보낼 수 있는 방법을 새로 만들어야 한다. url 리스트의 크기와 상관없이 큰 크기의 리스트를 요청해도 거부당하거나 연결끊어짐 현상이 발생하지 않는 방법을 찾아야함. 

make_set_of_word 함수 
> 지금은 카테고리가 15개밖에 없다. 좀 더 늘려서 더 구체적인 분석을 할 수 있게 만들어야한다. 페이지를 분석해서 카테고리 분류 중 가장 높은 숫자를 기록한 카테고리가 그 페이지의 성향이라> 고 정의하는데, 이런식으로 한가지의 카테고리로 분류하기보다는 백분율로 계산해서 해당 페이지를 성향별로 몇 퍼센트를 차지하는지 보여줄 수 있게 하는 것이 좋을 것 가다.
> 이 함수는 https://relatedwords.io/ 에 종속적이다. 즉 이 사이트의 방식이 바뀌거나 사이트가 운영하지 않게 되면 더 이상 동작할 수 없다. 그렇기 때문에, 카테고리에 따른 연관 단어 집합> > 이 따로 독립적으로 필요하다. 독립적인 데이터셋이 있어야 이 함수가 독립적으로 작동할 수 있다. 




