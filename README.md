BeautifulSoup4 
==============================
기존 BeautifulSoup4에 새로운 기능이 추가되었습니다. PYTHON으로 작성되었고, 2020.10.25 ~ 2020.10.30까지 작성되었습니다. (아직 진행중...)
------------------------------------------------------------------------------------------------------------------

<img src="https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/6.1.jpg" width="40%" height="30%" title="BeautifulSoup4" alt="BeautifulSoup4"></img>

***
* collect_text.py  
* create_list_soup.py 
* create_obj.py  
* html_file.py 
* image_make.py  
* make_tfile.py 
* set_of_word.py
* url_to_tree.py  
* z_test.py 

가 추가되었습니다. 
***
# z_text.py
해당 함수들의 사용법에 대해 나와있습니다. 
***
# url_to_tree.py
외부/ 이 파일 내의 함수를 호출하는 py파일에서 이미 collect_text의 to_text를 통해 word list와 url list를 생성하였을때 이 파일 내의 함수들을 사용할 수 있다. .
그 값 중에서 url list를 이 클래스의 함수가 매개변수로 받았을 때 기능하는 클래스의 함수를 정의한다. 트리를 생성한다. -> 1layer 

## set_word 함수 
찾을 단어를 지정해주는 함수

## count_word 함수 
해당 단어의 노출 빈도를 반환한다.

## search_deeper 함수 
2020.10.27
> 개선해야할점 많음. -> (문제점 많음. )
> 해당 함수는 처음에 범위를 /10통해 축소시켰다. 이유는 많은 requests요청을 걸면 서버 측에서 
> (내가 발생시킨 트래픽을 감당하지 못했기 때문...? -> 이라고 생각했는데, 사이트마다 요청할 수 있는 
> 개수가 다르다. 어떤 곳에서는 아무리 잘게 쪼개도 요청되지 않는 경우도 있었음. 음... 봇으로 크롤링
> 하는 걸 방지하려고 서버 측에서 그런 설정을 해놓은 것 같다. 이부분은 자세히 알지 못해서 추측 뿐... )  

2020.10.27
> 속도제한 없이 계속 요청했기 때문에 그럴 수도 있다는 얘기가 있어서 
> sleep을 통해 시간간격을 주고 난 뒤에 요청을 했는데,( sleep은 다양한 값을 사용해봤음. ) 이건 썼을때랑
> 안썻을 때랑 차이가 없다. 이게 문제가 아닌 듯? 

> soup_list에는 각각 해당되는 사이트의 소스코드가 순서대로 담겨있다.
> .sleep으로 해결 안됨. 어느 정도 숫자 넘어가면 그냥 요청 자체가 막히는 것같음. 

2020.10.27
> naver.com의 경우에는 --> 
> 등분으로 테스트해봤는데. 5,7,8,9등분 전부다 안되고, 10등분부터 작동함. 요청이 24.3개 이상 넘어가면
> 아예 거부됨. 파싱하고 싶은 리스트는 항상 24.3개 이하로 파싱해서 적용하기. 
> 더 작게 자르면 더 빨리 작동하니까 좋고. 

2020.10.27
> bot이 아니라 사람이 접속하는 걸로 전달하려고 접속정보제공했는데, 효과 없음. 
> 다 시도해봤는데, 리스트 분할해서 최대한 작게 슬라이싱해서 http요청하는 것 말고는 방법이 없는 듯하다. 
> 그런데 이렇게 하면 if문이 너무 많이 발생하고, 일단 객체가 너무 많이 발생한다. 
> 조금 더 줄일 수 있는 방법은 없을까? ? 

2020.10.28
> 리스트를 처리하는 함수를 새로 만들어서 코드수를 줄였다. 음... 저번보다는 많이 줄었긴 했는데, 
> 그래도 언뜻 보면 반복되는 량이 눈에 확 띈다. 이건 좀 더 좋은 방안있는지 살펴보기. 

## show_page_include_word 함수 
반드시 search_deeper 호출 다음에 호출되어야함. 아니면 NULL값 리턴 .단어를 포함하는 페이지의 url을 리스트로 반환한다.
***

# image_make.py 

## image_take 함수 
원하는 페이지에서 이미지태그를 긁어서 리스트로 모아줌. 해당 리스트를 html doc에 순서대로 넣어주는데, 따로 파일을 만들어서 생성해줌. 그 파일열면 페이지에 무슨 이미지가 있는지, 전부 확인할 수 있음. 
> 주의점 -> 
>> 이 함수는 url 리스트에서 통째로 이미지를 뽑아내는 게 아니라, 하나의 url에서 그 페이지에 걸린
>> 이미지들만 파일로 모아줌. 여러개의 url이 아님. 
>> 보완점해야할점 -> 1. 중복되는 이미지가 있음. 2. 이미지의 사이즈 조절이 안되서 html doc에 너무 크게 나옴.

***
# html_file.py

## html_link_file 함수 
메인 페이지에 걸려있는 모든 링크들을 html doc에 넣어서 링크집합을 만들어준다. 
찾고자하는 단어를 포함하는 링크는 SELECTED URL LIST 로 분류되어 하단에 따로 표시된다. 
내용은 image_make와 같다. 동일하게 동작한다. 다만 함수의 매개변수로 selected_list를 하나 더 받는다. 
show_page_include_word에서 단어를 포함하는 링크의 리스트를 반환했는데, 그 반환한 값이 
selected_list 매개변수에 들어오는 것이다. 
***

# create_list_soup.py

## list_seperate 함수 

requests 개수 제한을 해결하기 위한 함수. 
반복문을 통해 전달받은 리스트의 요소들(url 링크)을 하나씩 soup객체로 만들어준다. 
만들어진 soup객체를 하나씩 total_list 리스트에 더한다. 즉 soup객체가 요소로 들어있는 리스트를 제공한다. 
그리고 만들어진 total_list 리스트를 반환한다. 
대부분의 requests요청 거부 혹은 연결 끊어짐과 관련있는 에러는 전부 다 이 함수에서 발생한다. 
실행될때마다 url adding to list is finished 가 터미널에 출력되는데, 이 문구를 확인할 수 없으면 
에러가 발생한거임. 


> 보완해야할 점. -> 
>> 보통 import 에러가 아닌 이상 url adding to list is finished가 출력되는 시점에 대부분의 에러가 발생했음. 
>> -> requests요청을 한번에 보낼 수 있는 방법 (url 리스트 통째로 전달해도 거부당하지 않는 방법) 있으면 
>> 수정하기 

***

# collect_text.py
## to_text 함수 

url_from_out을 매개변수로 받은 뒤에 soup객체와 함께 페이지의 소스코드를 텍스트화시킨 html_info를 제공받는다. 
그후 soup객체를 가공해서 리스트로 만든 뒤 soup_str_translate을 반환한다. 
url_list라는 리스트를 생성하는데 페이지에 존재하는 모든 링크를 리스트에 할당한다. 
동시에 http를 포함하는 문자열 중에서 exe가 포함되지 않은 문자열을 url_list라는 리스트로 반환한다. 

for link in soup.find_all('a'):
    print(link.get('href'))    

--> 을 사용하면 쉽게 하이퍼링크만 뽑아낼 수 있다. 근데 이 기능만 사용하면 exe파일과 같이 다른 페이지로 
넘어가는 link가 아닌 다른 link들도 함께 sorting된다. 그러므로 따로 조건을 더 달아줘야함.

***

# set_of_word.py (추가)(독립)

## make_set_of_word 함수
https://relatedwords.io/ 에서는 연관단어에 대해 500개 정도의 단어를 제공한다. 
requests를 통해 해당 사이트에서 단어를 가져오고 리스트로 변환해서 할당한다. 
분석을 원하는 사이트가 있으면 make_set_of_word에 매개변수로 링크를 전달한다. 
전달된 링크는 또다시 requests를 통해 soup객체로 변환되고, 텍스트화 및 split된다. 
그리고 최종적으로 카테고리에 있는 분류중에서 가장 많은 빈도 수를 기록한 카테고리가 
해당 페이지의 분류가 된다.

보완점: 
> 지금은 카테고리가 15개밖에 없다. 좀 더 늘려서 더 구체적인 분석을 할 수 있게 만들어야함. 
> 페이지를 분류해서 카테고리 분류 중에서 가장 높은 숫자를 그 페이지의 분류라고 정의하는데, 
> 이런식으로 한가지의 카테고리로 분류하기 보다는 백분율로 계산해서 해당 페이지를 카테고리별로
> 퍼센트로 표현할 수 있게 해주는 것이 좋다. 

데이터셋 꼭 필요함. 
> 이 함수는 https://relatedwords.io/ 에 종속적이다. 즉 이 사이트의 방식이 바뀌거나
> 사이트가 운영하지 않게 되면 더 이상 동작할 수 없다. 그렇기 때문에, 카테고리에 따른 연관 단어 집합이
> 따로 독립적으로 필요하다. 독립적인 데이터셋이 있어야 이 함수가 독립적으로 작동할 수 있다. 
***

# 간단한 사용방법입니다. 예시처럼 작성하면 해당 함수를 사용할 수 있습니다. (set_of_word.py 아직 안썼음. )
<pre>
<code>
import requests
from bs4 import BeautifulSoup
from collect_text import to_text
import url_to_tree
import html_file
import image_make


'''해당 함수들의 사용방법에 대해 나와있습니다. 
2020.10.25 ~ 2020.10.30. 추후에 추가사항있으면 py추가해주기. 
'''
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

</code>
</pre>





***
make_tfile.py , create_obj.py지금 쓰이지 않습니다. / set_of_word_act.py도 쓰이지 않습니다. 
***
BeautifulSoup4의 원문 문서를 보고 싶으면 아래 링크를 클릭
<https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/>


***

# 보완점. 다시 만들어야되는 부분 
2020.11.03
그리고 전반적으로 보완해야 할거....
soup객체로 받아온거 text화하고, split하는데, parser를 만들기로 했는데 parser가 아직 안만들어짐. (soup객체 받아온게 활용이 안되는 느낌?)
그리고 set_of_word.py는 영어밖에 지원이 안됨. 

# bs4 폴더에 있는거 보시면 됩니당 opensource 는 그냥 예전꺼 .. 
