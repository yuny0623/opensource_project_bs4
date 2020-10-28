import requests
from bs4 import BeautifulSoup
#아직 사용되지 않음. 
#soup객체를 생성하고, 정렬되고, 텍스트화된 soup객체를 반환한다. 
#리스트와 관련된 클래스가 아님. 그냥 url한개에 매칭되는 한개의 soup객체만 반환함. 
def create_soup(url):
    html_info = requests.get(url).text
    soup = BeautifulSoup(html_info,'html.parser')
    return soup