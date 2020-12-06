bs4expand -> 구버전입니다. 다른 페이지로 이동해주세요 
==================================================

(여기서 최신버전 확인)[https://github.com/yuny0623/opensw]

뷰티풀수프4를 사용할떄 from bs4 import BeautifulSoup 이라고 선언한 뒤에 
soup객체를 사용자가 원하는 방식으로 사용하는데 이제 저희는 그와  같이 from bs4 import bs4expand 를 선언해서 저희가 만든 기능을 사용할 
수 있게 만들었습니다.  자세한 사용법과 내용은 뒤에 시현을 할때 직접 보여드리도록 하고, 
우선은 기능과 각 함수의 작동방식 그리고 코드에 대해서 말씀드리도록 하겠습니다. 

우선 저희가 추가한 기능은 py 파일로 bs4 폴더안에 위치하고 있습니다. 파일의 이름은 bs4expand.py이고 코드는 
417줄입니다. 

각 함수의 기능에 대해서 설명해드리겠습니다. 
우선 set_word 함수입니다. 사용자가 원하는 단어를 입력받으면, word_to_find라는 변수에 할당해주는 초기화의 역할을
수행합니다. 이후에 정의되는 함수들에서 word_to_find에 할당된 단어를 사용해서 작동한다고 보시면 됩니다. 
***
# count_word 함수
count_word 함수는 말그대로 단어의 개수 빈도수가 얼마나 되는지 soup객체 내의 텍스트에서 탐색해서 그 빈도 수를
알려주는 함수입니다. 

# to_text함수
다음은 to_text함수입니다. 이 함수는 저희가 작성한 bs4expand에서 가장 기본적인 실행을 담당하는 함수입니다. 
우선 분석을 원하는 페이지의 url을 입력받은 뒤에 requests를 통해 soup객체로 바꾸어 줍니다. 그리고 이후에 
연결가능한 링크만 따로 리스트에 할당하는 작업을 진행하고, (exe파일은 걸러내고)
페이지에서 뽑아낸 문자열들에서 특수문자를 제거하는 과정이 진행됩니다. 이를 통해 사용가능한 문자열리스트와 함께, 
페이지 내의 모든 앵커태그의 href(하이퍼텍스트 레퍼런스) 속성이 리스트로 반환됩니다. 그래서 
bs4expand를 사용하고 싶은 사용자는 우선적으로 이 함수를 통해서 두개의 값을 반환받은 뒤에 그 반환받은 값을변수에 할당하는 방식으로 
 사용할 수 있습니다. 



# serch_deeper함수
다음은 serch_deeper함수입니다. 이 함수는 내용이 길어서 두 부분으로 나누어 놓았습니다. 
우선 이함수는 분석하고자 하는 메인 페이지에 연결되어 있는 모든 페이지를 
다시 리스트로 할당해서 각각 모든 페이지에 대한 soup객체를 리스트로 반환받는 함수입니다.  코드를 보시면
여러개의 if문이 보이는데, requests 요청을 한번에 많은 수를 일정한 속도로 보내게 되면, 연결이 끊어진 현상이 발생했기 때문에
리스트를 슬라이싱해서 작업을 진행했습니다. 연결 끊어짐 혹은 요청 거부의 이유는 무작위적인 크롤링을 막기 위해서
웹서버 측에서 설정해두었기 때문인것으로 알고 있습니다. 

# list_seperate 함수
list_seperate 함수는 방금 말씀드린 search_deeper함수에서 받은 url 리스트를 모두 soup객체로 바꾸어주고 반환하는 함수입니다. 

# show_page_include_word 함수
다음은 show_page_include_word 함수입니다. 함수명에서 짐작할 수 있듯이 이 함수는 단어를 포함하는 url을 
리스트로 반환해줍니다. 이 과정에서 단어의 존재여부를 확인하고, 해당 단어가 그 페이지에  존재하면 그 페이지의 
url을 또다시 리스트에 할당하는 과정이 진행된다고 보시면 됩니다. 

# html_link_file함수와 image_take 함수
다음은 html_link_file함수와 image_take 함수입니다. 이 두 함수는 html 문서 양식을 사용하는데, 방금 말씀드린
show_page_include_word 함수에서 얻어낸, 단어를 포함하는 url의 리스트와 그리고 연결되어있는 모든 리스트를 html
문서 양식으로 직접 확인할 수 있습니다. 또한 image_take같은 경우는 해당 페이지에서 사용하고 있는 
모든 이미지를 모아볼 수 있습니다. 따라서 사용자는 image_take 함수 를 통해 직접 모든 이미지의 url에 접근할 수 있기 때문에
이미지를 다운받을 수도 있는 기능을 사용자가 추가로 손쉽게 구현해서 사용할 수 있습니다. 

# make_set_of_word라는 함수
다음은 마지막으로 make_set_of_word라는 함수입니다. 이 함수도 내용이 길어서 두 부분으로 나누어 놓았습니다. 
이 함수는 url을 입력받으면 그 페이지가 어떤 페이지인지
대략적인 분석을 내놓습니다. 15가지의 카테고리가 있는데, 그 카테고리에 해당되는 단어집합에서 빈도수를 측정하게 되는데, 
가장 많은 점수를 얻은 카테고리가 그 페이지의 성향이 된다고 보시면 됩니다. 
예를 들어https://www.oracle.com/index.html 라는 페이지를 분석하게 되면, 
이에 대한 결과로 programming 이라는 결과를 얻게 되는데,  programming카테고리에 존재하는 대략 500개 정도의
단어가 해당 사이트와 비교 되면서 가장 많은 점수를 획득했기 때문입니다. 

#  news_crawler 함수
다음은 news_crawler 입니다. 원하는 키워드 및 기간을 입력하면 그에 맞는 뉴스기사를 크롤링해주는 파일입니다.
첫번째 main 함수는 시작하는 함수로 질문에 따른 값을 입력하면 해당 값들을 crawler 함수로 전달해주는 역할입니다.

# crawler 함수
두 번재는 crawler 함수입니다. 전반적인 크롤링을 하는 함수로 네이버 뉴스기사 페이지에 있는 html 태그를 이용하여 필요한 부분을
크롤링합니다. 이때 정제화 함수를 활용하여 불필요한 내용을 삭제합니다. 노란색 박스는 해당 내용에 따라 어떤 태그에 있는지
확인하면서 넣어주면 값을 불러올 수 있습니다.

# contents_cleansing 함수
세 번째는 contents_cleansing 함수로 태그를 통해 크롤링한 본문 요약분에서 불필요한 부분을 제거해주는 함수입니다.
밑에 예시처럼 처음에 다른 태그가 섞여 더러운 부분을 함수를 통해 깔끔하게 정리된 모습을 확인할 수 있습니다.

사용예시로는 해당 py 파일을 실행시켜 입력 형식에 맞게 입력해주면 실행이 끝나고 코드가 있는 위치에 엑셀파일이 생성됩니다.
해당 엑셀파일로 들어가면 원하는 뉴스기사가 크롤링되어 정리된 것을 확인할 수 있습니다.

저희가 만든 함수들은 대부분이 페이지 분석에 관한 내용입니다. 뷰티풀수프가 html태그와 관련된 강력한 분석기능을 제공하지만, 
실제로 페이지자체를 분석하기 위해서는 soup객체를 활용한 추가적인 구현이 필요합니다. 그래서 이 때문에 
페이지에 대한 구체적인 정보를 얻기에는 사용자가 직접적으로 더 코딩을 진행해야 했기에 번거롭습니다. 그래서 
조금 더 유용한 기능들을 손쉽게 불러다 쓸 수 있게 만들었습니다. 

***
그리고 사용방법에 대해서 말씀드리면 
기본적으로 bs4expand가 파이썬 기본 경로에 있는 폴더에 존재해야 합니다. 원본 bs4같은 경우는 pip istall을 통해 기본 경로 내에 위치시킬 수 있는데, 
저희는 PYPI에 업로드 하지 않아서 우선은 깃허브에서 다운받으신 뒤에 PYTHON의 site_package 폴더 내에 위치시키면 바로 사용할 수 있습니다. 
저희의 깃허브 주소는 https://github.com/yuny0623/opensource_project_bs4 입니다. 여기 들어가시면 
해당 파일을 다운 받으실 수 있습니다. 여기서 알집을 해제하고, 이 해제한 폴더를 본인이 파이썬 을 설치한 위치에 가셔서
Lib에 site-package를 들어가시고 거기에 압축해체한 파일을 위치시키면 됩니다. 
***
우선 먼저 
from bs4 import bs4expand as ex
라고 선언을 하시면 됩니다. 이때 as ex는 쓰셔도 되고, 안쓰셔도 됩니다. 
그리고 다음은 사용하는 짧은 예시입니다. 
대부분의 함수의 반환값이 리스트의 형태이기 때문에 사용자는 이 함수들의 예제를 활용해서 더 나은 웹크롤러를 작성할 수 있습니다. 

```
x,y = ex.to_text("https://github.com/")
ex.set_word("python")
n = ex.count_word(x)
print(n)
print(len(y))
li = ex.search_deeper(y)
url_contain_word =ex.show_page_include_word(y) 
print(url_contain_word)
ex.html_link_file(y,url_contain_word) 
ex.image_take("https://github.com/")
s = ex.make_set_of_word("https://www.oracle.com/index.html")
print(s)
```


우선 to_text에서 결과값인 리스트 두개를 반환받고,. 
set_word에서는 원하는 단어를 초기화시킵니다. count_word로 단어의 빈도수를 반환받을 수 있습니다. 
그리고 serch_deeper함수를 호출하고, 그반환값을 li에 전달받는데, 이 리스트는 사용자가 다양하게 사용할 수 있습니다. 

show_page_include_word함수에서 리턴된 반환값을 받은 url_contain_word라는 변수가 출력된 것을 보실 수 있는데, 
해당 단어가 포함된 모든 url이 할당된것을 확인할 수 있습니다. 

ex.html_link_file(y,url_contain_word) 
ex.image_take("https://github.com/") 함수를 실행함으로써 collected_info_in_here라는 폴더에 파일이 생성되는 것을 확인할 수 있습니다. 
해당 파일을 클릭해보면 다음과 같은 결과를 확인할 수 있습니다.  이미지와 링크를 확인할 수 있습니다. 

마지막으로 make_set_of_word를 통해 간단한 분석이 s에 할당되는 것을 확인할 수 있습니다. 
