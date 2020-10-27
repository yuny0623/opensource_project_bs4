
















'''
def search_deeper(self,out_url_list): #일단은 100개 이하인것만 처리 가능.불필요한 반복이 너무 많음. 
        li = out_url_list
        print("search-deeper act in here")
        if (len(li)<100) & (len(li) >0): # 100> x> 0
            print("soup act in here")
            if len(li)>90 :
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:10]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[10:20]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[20:30]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[30:40]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[40:50]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[50:60]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[60:70]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[70:80]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[80:90]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[90:]))
                #95라 가정하자. 
                j=0
                for i in range(len(li)/10): # 9가 나오겠지? i는 0~9까지 돌거고...
                    url_parse.soup_list.append(make_small_list().list_seperate(li[j:(j+10)]))
                    j+=10
                    if i == (len(li)/10):
                        url_parse.soup_list.append(make_small_list().list_seperate(li[j:]))
            if (len(li)<90) & (len(li)>80):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[21:31]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[31:41]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[41:51]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[51:61]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[61:71]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[71:81]))
            if (len(li)<80) & (len(li)>70):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[21:31]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[31:41]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[41:51]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[51:61]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[61:71]))
            if (len(li)<70) &(len(li)>60):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[21:31]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[31:41]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[41:51]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[51:61]))
            if (len(li)<60) &(len(li)>50):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[21:31]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[31:41]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[41:51]))
            if (len(li)<50) &(len(li)>40):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[21:31]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[31:41]))
            if (len(li)<40) &(len(li)>30):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[21:31]))
            if (len(li)<30) &(len(li)>20):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
                url_parse.soup_list.append(make_small_list().list_seperate(li[11:21]))
            if (len(li)<20) &(len(li)>10):
                url_parse.soup_list.append(make_small_list().list_seperate(li[0:11]))
            if len(li)<10 &len(li)>0:
                url_parse.soup_list.append(make_small_list().list_seperate(li))
        if len(li) <0:
            raise Exception("잘못된 값이 입력되었습니다.")
        return url_parse.soup_list
'''



































# for i in range(len(soup_str_translate)): #soup_str_translate내부의 요소들을 모두 출력해줌.
#     print(soup_str_translate[i])


        # for i in range(len(in_list)):
        #     print(in_list[i])

        # print(in_list[1])


        # soup_str_translate리스트를 다시 한번 가공한다. 불필요한 기호는 삭제시킨다. 
    # 그리고 바뀐 리스트를 반환한다. 


    # def clean_soup_str_translate(self,out_list): #필요없는 기호는 삭제시킨다. soup_str_translate가 매개변수가 되어야함. 
    #     in_list = []
    #     for word in out_list:
    #         symbols = """!@#$%^&*()_-+={[}]|\;:"‘'·<>?/.,ⓒ """
    #         for i in range(len((symbols))):
    #             word = word.replace(symbols[i], '')      
    #         if len(word) > 0:
    #             in_list.append(word)
    #     return in_list    








# new_list = []
# for i in range(len(s_list_obj)):
#     if s_list_obj[i][0:4] == "http":
#         new_list.append(s_list_obj[i])

# for i in range(len(new_list)):
#     print(new_list[i])



# s_str_obj,s_list_obj = new_html_parse().make_url_to("https://www.naver.com/")
# for i in range(len(s_list_obj)):
#     print(s_list_obj[i])
# s_obj_transe = new_html_parse().clean_soup_str_translate(s_obj)
# print(s_obj)

'''
from new_html_parse1 import new_html_parse
#이 파일은 new_html_parse1 파일에서 받아온 url_list를 가공하는 파일입니다. 
s_str_obj,s_list_obj = new_html_parse().make_url_to("https://www.naver.com/")


# for i in range(len(s_list_obj)):
#     print(s_list_obj[i])

# print(s_list_obj[5][0:4])
new_list = []
for i in range(len(s_list_obj)):
    if s_list_obj[i][0:4] == "http":
        new_list.append(s_list_obj[i])

for i in range(len(new_list)):
    print(new_list[i])
'''




# import requests
# from bs4 import BeautifulSoup

# url = "https://www.naver.com/"       #테스트용 url링크  
# html_info = requests.get(url).text   #requests 사용해서 url경로의 페이지 str로 변경해줌.   
# soup = BeautifulSoup(html_info,'html.parser')      #beautifulsoup4로 새로 파싱하기 위해 soup객체 생성. 

# print(type(html_info))
# soup_text = soup.get_text()

# # print(soup_text)
# soup_str_translate = soup_text.split()
# # print(soup_text)

# def clean_wordlist(input_list):
#     output_list = []
#     for word in input_list:
#         symbols = """!@#$%^&*()_-+={[}]|\;:"‘'·<>?/.,ⓒ """
#         for i in range(len((symbols))):
#             word = word.replace(symbols[i], '')      
#         if len(word) > 0:
#             output_list.append(word)
#     return output_list    
# str_list = clean_wordlist(soup_str_translate)
# # print(str_list)
# # print(html_info.get_text())

# def counter(input_list):
#     word_count = {}
#     for word in str_list:
#         if word in  word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count


# word_count = counter(str_list)
# word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
# print(word_count)


#todo list
#soup 객체 내의 텍스트 데이터 파싱하거나, 분석하는 메소드 생성하기. 
#문자열 길이에 따라서 정렬하기. 단어 정렬하기 단어 길이 순 정렬하기. 단어 빈도 순 정렬하기 
# 단어 속성 순으로 정렬하기. 어디에 포함된 단어인지 판단하기. 

s = """

<!doctype html>                <html lang="ko" data-dark="true"> <head> <meta charset="utf-8"> <title>NAVER</title> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=1190"> <meta name="apple-mobile-web-app-title" content="NAVER"/> <meta name="robots" content="index,nofollow"/> <meta name="description" content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요"/> <meta property="og:title" content="네이버"> <meta property="og:url" content="https://www.naver.com/"> <meta property="og:image" content="https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png"> <meta property="og:description" content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요"/> <meta name="twitter:card" content="summary"> <meta name="twitter:title" content=""> <meta name="twitter:url" content="https://www.naver.com/"> <meta name="twitter:image" content="https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png"> <meta name="twitter:description" content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요"/>  <link rel="stylesheet" href="https://pm.pstatic.net/dist/css/nmain.20201020.css"> <link rel="stylesheet" href="https://ssl.pstatic.net/sstatic/search/pc/css/api_atcmp_200709.css"> <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico?1"/>   <script>document.domain="naver.com",window.nmain=window.nmain||{},window.nmain.supportFlicking=!1;var nsc="navertop.v4",ua=navigator.userAgent;window.nmain.isIE=navigator.appName&&navigator.appName.indexOf("Explorer")>0&&ua.toLocaleLowerCase().indexOf("msie 10.0")<0,document.getElementsByTagName("html")[0].setAttribute("data-useragent",ua),window.nmain.isIE&&(Object.create=function(n){function a(){}return a.prototype=n,new a})</script> <script>var darkmode= true;window.naver_corp_da=window.naver_corp_da||{main:{}},window.naver_corp_da.main=window.naver_corp_da.main||{},window.naver_corp_da.main.darkmode=darkmode</script> <script> window.nmain.gv = {  isLogin: "dkapqk450",
userId: "dkapqk450",
old: "22",   daInfo: {"ANIMAL":{"menu":"ANIMAL","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000161","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_animal_1","tb":"ANIMAL_1","unit":"SU10567","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000162","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_animal_2","tb":"ANIMAL_1","unit":"SU10568","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"BEAUTY":{"menu":"BEAUTY","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000163","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_beauty_1","tb":"BEAUTY_1","unit":"SU10595","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000164","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_beauty_2","tb":"BEAUTY_1","unit":"SU10596","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"BUSINESS":{"menu":"BUSINESS","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000165","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_business_1","tb":"BUSINESS_1","unit":"SU10577","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000166","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_business_2","tb":"BUSINESS_1","unit":"SU10578","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"CARGAME":{"menu":"CARGAME","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000167","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_cargame_1","tb":"CARGAME_1","unit":"SU10587","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000168","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_cargame_2","tb":"CARGAME_1","unit":"SU10588","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"CHINA":{"menu":"CHINA","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000169","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_china_1","tb":"CHINA_1","unit":"SU10591","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000170","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_china_2","tb":"CHINA_1","unit":"SU10592","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"DESIGN":{"menu":"DESIGN","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000171","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_design_1","tb":"DESIGN_1","unit":"SU10569","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000172","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_design_2","tb":"DESIGN_1","unit":"SU10570","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"FARM":{"menu":"FARM","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000173","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_farm_1","tb":"FARM_1","unit":"SU10561","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000174","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_farm_2","tb":"FARM_1","unit":"SU10562","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"FINANCE":{"menu":"FINANCE","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000175","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_finance_1","tb":"FINANCE_1","unit":"SU10563","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000176","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_finance_2","tb":"FINANCE_1","unit":"SU10564","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"ITTECH":{"menu":"ITTECH","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000177","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_ittech_1","tb":"ITTECH_1","unit":"SU10593","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000178","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_ittech_2","tb":"ITTECH_1","unit":"SU10594","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"JOB":{"menu":"JOB","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000179","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_job_1","tb":"JOB_1","unit":"SU10589","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000180","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_job_2","tb":"JOB_1","unit":"SU10590","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"LAW":{"menu":"LAW","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000181","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_law_1","tb":"LAW_1","unit":"SU10573","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000182","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_law_2","tb":"LAW_1","unit":"SU10574","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"LIVING":{"menu":"LIVING","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000183","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_living_1","tb":"LIVING_1","unit":"SU10597","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000184","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_living_2","tb":"LIVING_1","unit":"SU10606","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"LIVINGHOME":{"menu":"LIVINGHOME","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000185","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_livinghome_1","tb":"LIVINGHOME_1","unit":"SU10571","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000186","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_livinghome_2","tb":"LIVINGHOME_1","unit":"SU10572","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"MOMKIDS":{"menu":"MOMKIDS","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000187","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_momkids_1","tb":"MOMKIDS_1","unit":"SU10575","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000188","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_momkids_2","tb":"MOMKIDS_1","unit":"SU10576","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"MOVIE":{"menu":"MOVIE","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000189","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_movie_1","tb":"MOVIE_1","unit":"SU10585","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000190","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_movie_2","tb":"MOVIE_1","unit":"SU10586","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"SCHOOL":{"menu":"SCHOOL","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000191","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_school_1","tb":"SCHOOL_1","unit":"SU10579","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000192","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_school_2","tb":"SCHOOL_1","unit":"SU10580","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"SHOW":{"menu":"SHOW","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000193","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_show_1","tb":"SHOW_1","unit":"SU10565","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000194","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_show_2","tb":"SHOW_1","unit":"SU10566","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"TRAVEL":{"menu":"TRAVEL","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000195","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_travel_1","tb":"TRAVEL_1","unit":"SU10581","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000196","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_travel_2","tb":"TRAVEL_1","unit":"SU10582","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]},"WEDDING":{"menu":"WEDDING","childMenu":"","adType":"singleDom","multiDomAdUrl":"","multiDomUnit":"","infoList":[{"adposId":"1000197","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_wedding_1","tb":"WEDDING_1","unit":"SU10583","calp":"-"},"type":{"position":"abs","positionIndex":4,"subject":"contents"},"dom":null},{"adposId":"1000198","singleDomAdUrl":"https://siape.veta.naver.com/fxshow","param":{"da_dom_id":"p_main_wedding_2","tb":"WEDDING_1","unit":"SU10584","calp":"-"},"type":{"position":"abs","positionIndex":8,"subject":"contents"},"dom":null}]}},
svt: 20201025182233,
}; </script> <script> window.nmain.newsstand = {
rcode: '09290139',
newsCastSubsInfo: '',
newsStandSubsInfo: ''
};
window.etc = {  };
window.svr = "<!--aweb102-->"; </script> <script src="https://ssl.pstatic.net/tveta/libs/assets/js/pc/main/min/pc.veta.core.min.js" defer="defer"></script> <script src="https://ssl.pstatic.net/tveta/libs/assets/js/common/min/probe.min.js" defer="defer"></script>   <script src="https://pm.pstatic.net/dist/js/external.57da6acd.js?o=www" type="text/javascript" crossorigin="anonymous" defer="defer"></script> <script src="https://pm.pstatic.net/dist/js/preload.c93a5604.js?o=www" type="text/javascript" crossorigin="anonymous" defer="defer"></script> <script src="https://pm.pstatic.net/dist/js/polyfill_async.2029d342.js?o=www" type="text/javascript" crossorigin="anonymous" async></script> <script src="https://pm.pstatic.net/dist/js/vendors~more~nmain~sidebar_notice.6ccea782.js?o=www" type="text/javascript" crossorigin="anonymous" defer="defer"></script> <script src="https://pm.pstatic.net/dist/js/vendors~nmain.4109dec4.js?o=www" type="text/javascript" crossorigin="anonymous" defer="defer"></script> <script src="https://pm.pstatic.net/dist/js/nmain.a24ade21.js?o=www" type="text/javascript" crossorigin="anonymous" defer="defer"></script> <script type="text/javascript" src="https://pm.pstatic.net/dist/lib/search.jindo.20200326.js?o=www" crossorigin="anonymous" defer="defer"></script> <style>:root{color-scheme:light}#_nx_kbd .setkorhelp a{display:none}</style> </head> <body> <div id="u_skip"> <a href="#newsstand"><span>뉴스스탠드 바로가기</span></a> <a href="#themecast"><span>주제별캐스트 바로가기</span></a> <a href="#timesquare"><span>타임스퀘어 바로가기</span></a> <a href="#shopcast"><span>쇼핑캐스트 바로가기</span></a> <a href="#account"><span>로그인 바로가기</span></a> </div> <div id="wrap"> <style type="text/css">._1syGnXOL{padding-right:18px;font-size:14px;line-height:0;letter-spacing:-.25px;color:#000}._1syGnXOL span,._1syGnXOL strong{line-height:49px}._1syGnXOL:before{display:inline-block;content:"";vertical-align:top;background-image:url(https://static-whale.pstatic.net/main/sprite-20200907@2x.png);background-repeat:no-repeat;background-size:114px 104px;width:18px;height:18px;margin:16px 8px 0 0;background-position:-46px -63px}[data-useragent*="MSIE 8"] ._1syGnXOL:before{background-image:url(https://static-whale.pstatic.net/main/sprite-20200907.png)}._1syGnXOL._3dsvmZg2:before{background-position:-26px -83px}._1syGnXOL._18YOHi7v{color:#fff}._1syGnXOL._3di88A4c{padding-right:12px;font-size:17px}._1syGnXOL._3di88A4c:before{content:none}._1syGnXOL._3jtl_dKE{font-size:16px}._1syGnXOL ._19K4X1CD{text-decoration:underline}._2aeXMlrb{display:inline-block;position:relative;font-size:12px;height:49px;width:78px;text-decoration:none;color:#fff;font-weight:700;letter-spacing:-.5px;vertical-align:top}._2aeXMlrb span{text-align:center;margin:9px 0;height:31px;display:block;line-height:31px;border-radius:15px}._2aeXMlrb span:before{display:inline-block;content:"";vertical-align:top;background-image:url(https://static-whale.pstatic.net/main/sprite-20200907@2x.png);background-repeat:no-repeat;background-size:114px 104px}[data-useragent*="MSIE 8"] ._2aeXMlrb span:before{background-image:url(https://static-whale.pstatic.net/main/sprite-20200907.png)}._2aeXMlrb.BMgpjddw{font-size:11px;width:94px}._2aeXMlrb.BMgpjddw span:before{margin:9px 3px 0 0;width:17px;height:13px;background-position:-98px 0}._3h-N8T9V{position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0)}._1KncATpM{display:inline-block;content:"";vertical-align:top;background-image:url(https://static-whale.pstatic.net/main/sprite-20200907@2x.png);background-repeat:no-repeat;background-size:114px 104px;margin-top:14px;float:left;width:98px;height:21px;background-position:0 -21px}[data-useragent*="MSIE 8"] ._1KncATpM{background-image:url(https://static-whale.pstatic.net/main/sprite-20200907.png)}._1KncATpM._2v3uxv2x{background-position:0 0}._1KncATpM._1yl_Ow6o{background-position:0 -42px}._20PYt6lT{font-size:11px;height:49px;cursor:pointer;position:absolute;top:0;right:0;color:#666;opacity:.7}._20PYt6lT:after{width:15px;height:15px;margin-left:4px;background-position:-64px -63px;display:inline-block;content:"";vertical-align:top;background-image:url(https://static-whale.pstatic.net/main/sprite-20200907@2x.png);background-repeat:no-repeat;background-size:114px 104px}[data-useragent*="MSIE 8"] ._20PYt6lT:after{background-image:url(https://static-whale.pstatic.net/main/sprite-20200907.png)}._20PYt6lT._39oMCV2N:after{background-position:-46px -81px}._20PYt6lT._3wm5EzmJ{color:#fff}._20PYt6lT._3wm5EzmJ:after{background-position:0 -89px}._1hiMWemA{height:49px}._1hiMWemA .tY_u8r23{position:relative;width:1130px;margin:0 auto}._1hiMWemA .tY_u8r23 a{text-decoration:none}._1hiMWemA._23U_6TM_{position:relative}._1hiMWemA._23U_6TM_:after{position:absolute;z-index:1;content:"";display:block;width:100%;height:1px;bottom:0;background-color:rgba(0,0,0,.05)}</style>                  
<div id="NM_TOP_BANNER" data-clk-prefix="top" class="_1hiMWemA _23U_6TM_" style="background-color: #f9fafe;">
<div class="tY_u8r23">
<a class="_3h-N8T9V" href='https://whale.naver.com/details/quicksearch?=main&wpid=RydDy7'
data-clk="dropbanner1b"></a>
<i class="_1KncATpM"><span class="blind">NAVER whale</span></i>
<img src="https://static-whale.pstatic.net/main/img_quicksearch@2x.png" width="210" height="49" alt=""
style="padding-left: 112px;" />
<span class="_1syGnXOL _3di88A4c" data-clk="dropbanner1b" style="padding-left: 12px;"><span>환율부터 모르는 단어까지,
</span><strong>드래그 한 번에 해결!</strong></span>
<a href='https://static-whale.pstatic.net/downloads/WhaleSetup.exe' class="_2aeXMlrb BMgpjddw" id="NM_whale_download_btn"
data-clk="dropdownload1b"><span style="background-color: #3154b8;">다운로드</span></a>
<button type="button" data-ui-cookie-exp-days="3" data-ui-cookie-key="NM_TOP_PROMOTION" data-ui-cookie-value="1"
data-ui-hide-target="#NM_TOP_BANNER" data-clk="dropclose1b" class="_20PYt6lT _39oMCV2N" style="display: none;">
3일 동안 보지 않기
</button>
</div>
</div>  <div id="header" role="banner">










<div class="special_bg">
<div class="group_flex">
<div class="logo_area">
<h1 class="logo_default">
<a href="/" class="logo_naver" data-clk="top.logo"
><span class="blind">네이버</span></a
>
</h1>
</div>
<div class="service_area">
<a id="NM_set_home_btn" href="https://help.naver.com/support/welcomePage/guide.help" class="link_set" data-clk="top.mkhome">네이버를 시작페이지로</a>
<i class="sa_bar"></i>
<a href="https://jr.naver.com" class="link_jrnaver" data-clk="top.jrnaver"><i class="ico_jrnaver"></i><span class="blind">쥬니어네이버</span></a>
<a href="https://happybean.naver.com" class="link_happybin" data-clk="top.happybean"><i class="ico_happybin"></i><span class="blind">해피빈</span></a>
</div>

<div id="search" class="search_area" data-clk-prefix="sch">
<form id="sform" name="sform" action="https://search.naver.com/search.naver" method="get">
<fieldset>
<legend class="blind">검색</legend>
<input type="hidden" id="sm" name="sm" value="top_hty" />
<input type="hidden" id="fbm" name="fbm" value="0" />
<input type="hidden" id="acr" name="acr" value="" disabled="disabled" />
<input type="hidden" id="acq" name="acq" value="" disabled="disabled" />
<input type="hidden" id="qdt" name="qdt" value="" disabled="disabled" />
<input type="hidden" id="ie" name="ie" value="utf8" />
<input type="hidden" id="acir" name="acir" value="" disabled="disabled" />
<input type="hidden" id="os" name="os" value="" disabled="disabled" />
<input type="hidden" id="bid" name="bid" value="" disabled="disabled" />
<input type="hidden" id="pkid" name="pkid" value="" disabled="disabled" />
<input type="hidden" id="eid" name="eid" value="" disabled="disabled" />
<input type="hidden" id="mra" name="mra" value="" disabled="disabled" />



<div class="green_window" style="">
<input id="query" name="query" type="text" title="검색어 입력" maxlength="255" class="input_text" tabindex="1" accesskey="s" style="ime-mode:active;" autocomplete="off" onclick="document.getElementById('fbm').value=1;" value="" />
</div>
<button id="search_btn" type="submit" title="검색" tabindex="3" class="btn_submit" onclick="window.nclick(this,'sch.action','','',event);" style="">
<span class="blind">검색</span>
<span class="ico_search_submit"></span>
</button>
</fieldset>
</form>
<!-- 한글입력기 -->
<a id="ke_kbd_btn" href="javascript:;" role="button" class="btn_keyboard" onclick="nx_ime_load(this)" data-clk="ime"><span class="ico_keyboard"></span>
<p class="msg_keybord"><span class="blind">입력도구</span></p>
</a>
<style type="text/css" id="_nx_kbd_style"></style>
<div id="_nx_kbd" style="display:none;"></div>
<!-- 자동완성 열린 경우 fold 클래스 추가, 딤드인 경우 dim 추가 -->
<div id="nautocomplete" class="autocomplete">
<a href="javascript:;" role="button" tabindex="2" class="btn_arw _btn_arw fold"><span class="blind _text">자동완성/최근검색어 펼치기</span><span class="ico_arr"></span></a>
</div>
<!-- 자동완성레이어 -->
<div id="autoFrame" class="reatcmp" style="background-color:rgb(255, 255, 255);display:none;">
<div class="api_atcmp_wrap _atcmp" style="display:none;">
<div class="words _words">
<div class="_atcmp_result_wrap">
<ul class="_resultBox"></ul>
<ul class="_resultBox"></ul>
<ul class="_resultBox"></ul>
<ul class="_resultBox"></ul>
</div>
<!-- 우측 정답형 영역 -->
<div class="add_group _atcmp_answer_wrap"></div>
</div>
<!-- 컨텍스트 자동완성 플러스 -->
<!-- [AU] _plus -->
<div class="atcmp_plus _plus">
<span class="desc">
<span class="plus_txt _plusTxt">시간대와 관심사에 맞춘 <em class='txt'>컨텍스트 자동완성</em></span>
<a onclick="__atcmpCR(event, this, 'plus.help', '','','');" href="https://help.naver.com/support/contents/contents.nhn?serviceNo=606&categoryNo=16658" target="_blank" class="spat ico_info _plusHelp"><span class="blind">도움말 보기</span></a>
</span>
<!-- [AU] _plus_btn -->
<span class="switch _plus_btn">
<a href="#" class="btn_turnon active" onclick="__atcmpCR(event, this, 'plus.use', '','','');">ON<span class="blind">선택됨</span></a>
<a href="#" class="btn_turnoff" onclick="__atcmpCR(event, this, 'plus.unuse', '','','');">OFF</a>
</span>
<div class="layer_plus _plusAlert">
<strong class="tit">컨텍스트 자동완성</strong>
<div class="_logout" style="display:block;">
<p class="dsc"><em class="txt">동일한 시간대/연령/남녀별</em> 사용자 그룹의<br>관심사에 맞춰 자동완성을 제공합니다.</p>
<div class="btn_area">
<a onclick="__atcmpCR(event, this, 'plus.login', '','','');" href="https://nid.naver.com/nidlogin.login" class="btn btn_login">로그인</a>
<a target="_blank" onclick="__atcmpCR(event, this, 'plus.detail', '','','');" href="https://help.naver.com/support/alias/search/word/word_16.naver" class="btn btn_view">자세히</a>
</div>
</div>
<div class="_login" style="display:none;">
<p class="dsc">ON/OFF설정은<br>해당 기기(브라우저)에 저장됩니다.</p>
<div class="btn_area">
<a target="_blank" onclick="__atcmpCR(event, this, 'plus.detail', '','','');" href="https://help.naver.com/support/contents/contents.nhn?serviceNo=606&categoryNo=16659" class="btn btn_view">자세히</a>
</div>
</div>
<button type="button" class="btn_close _close" onclick="__atcmpCR(event, this, 'plus.close', '','','');"><i class="spat ico_close">컨텍스트 자동완성 레이어 닫기</i></button>
</div>
</div>
<!-- //컨텍스트 자동완성 플러스 -->
<p class="func _atcmpBtnGroup"><span class="fl"><a class="_help" onclick="__atcmpCR(event, this, 'help', '','','');" href="https://help.naver.com/support/service/main.nhn?serviceNo=606&categoryNo=1987" target="_blank">도움말</a><span class="atcmp_bar"></span><a onclick="__atcmpCR(event, this, 'report', '','','');" href="https://help.naver.com/support/contents/contents.nhn?serviceNo=605&categoryNo=18215" target="_blank" class="report">신고</a></span><span><em><a class="hisoff" href="javascript:;">검색어저장 켜기</a><span class="atcmp_bar"></span></em><a class="funoff" href="javascript:;">자동완성 끄기</a></span></p>
<span class="atcmp_helper _help_tooltip1">기능을 다시 켤 때는 <em class="ico_search spat">자동완성 펼치기</em>을 클릭하세요</span>
</div>
<div class="api_atcmp_wrap _atcmpIng" style="display:none;">
<div class="words"><p class="info_words">현재 자동완성 기능을 사용하고 계십니다.</p></div>
<p class="func _atcmpBtnGroup"><span class="fl"><a class="_help" onclick="__atcmpCR(event, this, 'help', '','','');" href="https://help.naver.com/support/service/main.nhn?serviceNo=606&categoryNo=1987" target="_blank">도움말</a><span class="atcmp_bar"></span><a onclick="__atcmpCR(event, this, 'report', '','','');" href="https://help.naver.com/support/contents/contents.nhn?serviceNo=605&categoryNo=18215" target="_blank" class="report">신고</a></span><span><em><a class="hisoff" href="javascript:;">검색어저장 켜기</a><span class="atcmp_bar"></span></em><a class="funoff" href="javascript:;">자동완성 끄기</a></span></p>
<span class="atcmp_helper _help_tooltip2">기능을 다시 켤 때는 <em class="ico_search spat">자동완성 펼치기</em>을 클릭하세요</span>
</div>
<div class="api_atcmp_wrap _atcmpStart" style="display:none;">
<div class="words"><p class="info_words">자동완성 기능이 활성화되었습니다.</p></div>
<p class="func _atcmpBtnGroup"><span class="fl"><a class="_help" onclick="__atcmpCR(event, this, 'help', '','','');" href="https://help.naver.com/support/service/main.nhn?serviceNo=606&categoryNo=1987" target="_blank">도움말</a><span class="atcmp_bar"></span><a onclick="__atcmpCR(event, this, 'report', '','','');" href="https://help.naver.com/support/contents/contents.nhn?serviceNo=605&categoryNo=18215" target="_blank" class="report">신고</a></span><span><em><a class="hisoff" href="javascript:;">검색어저장 켜기</a><span class="atcmp_bar"></span></em><a class="funoff" href="javascript:;">자동완성 끄기</a></span></p>
<span class="atcmp_helper _help_tooltip3">기능을 다시 켤 때는 <em class="ico_search spat">자동완성 펼치기</em>을 클릭하세요</span>
</div>
<div class="api_atcmp_wrap _atcmpOff" style="display:none;">
<div class="words"><p class="info_words">자동완성 기능이 꺼져 있습니다.</p></div>
<p class="func _atcmpBtnGroup"><span class="fl"><a class="_help" onclick="__atcmpCR(event, this, 'help', '','','');" href="https://help.naver.com/support/service/main.nhn?serviceNo=606&categoryNo=1987" target="_blank">도움말</a><span class="atcmp_bar"></span><a onclick="__atcmpCR(event, this, 'report', '','','');" href="https://help.naver.com/support/contents/contents.nhn?serviceNo=605&categoryNo=18215" target="_blank" class="report">신고</a></span><span><em><a class="hisoff" href="javascript:;">검색어저장 켜기</a><span class="atcmp_bar"></span></em><a class="funoff" href="javascript:;">자동완성 켜기</a></span></p>
</div>
<!-- 최근검색어 & 내검색어 -->
<div class="api_atcmp_wrap _keywords" style="display:none;">
<div class="my_words">
<div class="lst_tab">
<ul><li class="on _recentTab"><a href="javascript:;">최근검색어</a></li><li class="_myTab"><a href="javascript:;">내 검색어</a></li></ul>
</div>
<div class="words _recent">
<ul><li data-rank="@rank@"><a class="t@my@ _star _myBtn" title="내 검색어 등록" href="javascript:;"><em class="spat">내 검색어 등록</em></a><a href="javascript:;" class="keyword">@txt@</a><em class="keyword_date">@date@.</em><a href="javascript:;" class="btn_delete spat _del" title="검색어삭제">삭제</a><span style="display:none">@in_txt@</span></li></ul>
<div class="info_words _recentNone" style="display:none">최근검색어 내역이 없습니다.</div>
<p class="info_words _offMsg" style="display:none">검색어 저장 기능이 꺼져 있습니다.</p>
</div>
<div class="words _my" style="display:none">
<ul><li data-rank="@rank@"><a class="ton _star _myBtn" title="내 검색어 해제" href="javascript:;"><em class="spat">내 검색어 해제</em></a><a href="javascript:;" class="keyword">@txt@</a></li></ul>
<div class="info_words _myNone" style="display:none">설정된 내 검색어가 없습니다.<br />최근검색어에서 <span class="star spat">내 검색어 등록</span>를 선택하여 자주 찾는 검색어를<br />내 검색어로 저장해 보세요.</div>
<p class="info_words _offMsg" style="display:none">검색어 저장 기능이 꺼져 있습니다.</p>
</div>
<p class="noti"><em class="ico_noti spat"><span class="blind">알림</span></em>내 검색어 서비스가 종료될 예정입니다. <a href="https://www.naver.com/NOTICE/read/1100001014/10000000000030669251" target="_blank" class="link" onclick="window.nclick(this, 'sug.noticeclose', '', '', event);">네이버 공지게시판</a></p>
<p class="noti _noti" style="display:none"><em class="ico_noti spat"><span class="blind">알림</span></em>공용 PC에서는 개인정보 보호를 위하여 반드시 로그아웃을 해 주세요.</p>
<p class="func _recentBtnGroup"><span class="fl"><a class="_delMode" href="javascript:;">기록 삭제</a></span><span><a class="_keywordOff" href="javascript:;">검색어저장 끄기</a><span class="atcmp_bar"></span><a class="_acOff" href="javascript:;">자동완성 끄기</a></span></p>
<p class="func _recentDelBtnGroup" style="display:none"><span class="fl"><a class="_delAll" href="javascript:;" title="최근 검색어 기록을 모두 삭제합니다.">기록 전체 삭제</a></span><span><a class="_delDone" href="javascript:;">완료</a></span></p>
<p class="func _myBtnGroup" style="display:none"><span class="fl"><a class="_delAll" href="javascript:;" title="설정된 내 검색어를 모두 삭제합니다.">기록 전체 삭제</a></span><span><a class="_keywordOff" href="javascript:;">검색어저장 끄기</a><span class="atcmp_bar"></span><a class="_acOff" href="javascript:;">자동완성 끄기</a></span></p>
<span class="atcmp_helper _help2">기능을 다시 켤 때는 <em class="ico_search spat">자동완성 펼치기</em>을 클릭하세요</span>
<div class="ly_noti _maxLayer" style="display:none">
<span class="mask"></span>
<p><span class="ico_alert spat"></span>내 검색어는 <em>최대 10</em>개 까지 저장할 수 있습니다.<br />추가하시려면 기존 내 검색어를 지워주세요. <a href="javascript:;" class="btn_close _close"><i class="spat ico_close">닫기</i></a></p>
</div>
</div>
</div>
<!-- 자동완성 안내문구 (선거) -->
<div class="api_atcmp_wrap _alert" style="display:none;">
<div class="api_atcmp_alert">
<p class="dsc_txt">
<span class="ico_alert spat"></span><span class="_passage"></span>
<span class="term"><span class="_term"></span><a href="#" target="_blank" class="link _link" onclick="window.nclick(this,'sug.vote','','',event);">자세히보기</a></span>
</p>
</div>
</div>
<!-- //자동완성 안내문구 (선거) -->
<!-- [D] IE 계열, wmode="window" flash와 겹치지 않기 위함 -->
<iframe vspace="0" hspace="0" border="0" style="display:none;display:block\9;display:block\0/;position:absolute;left:0;top:0;width:100%;height:100%;z-index:-1;" title="빈 프레임"></iframe>
</div>
<!--자동완성 템플릿 추가-->
<!-- 신규 공통 템플릿 -->
<script type="text/template" id="_atcmp_answer_0">
<div class="add_opt _item" data-sm="@2@" data-keyword="@1@" data-template_id="@0@" data-acir="@rank@" data-os="@8@" data-bid="@9@" data-eid="@3@" data-pkid="@10@" data-mra="@11@" >
<a href="#" class="opt_dsc">
<span class="dsc_thmb" style="@style7@">@image7@</span>
<span class="dsc_group">
<span class="dsc_cate">@6@</span>
<strong class="dsc_word">@1@</strong>
<span class="dsc_sub" style="@style12@">@12@</span>
</span>
</a>
</div>
</script>
<!-- 로또당첨번호 -->
<script type="text/template" id="_atcmp_answer_3">
<div class="add_opt _item" data-sm="@2@" data-keyword="@1@" data-template_id="@0@" data-acir="@rank@">
<a href="javascript:;" class="opt_lotto">
<span class="lotto_num_area">
<span class="spat lotto_num lotto_num@6@">@6@</span><span class="spat lotto_num lotto_num@7@">@7@</span><span class="spat lotto_num lotto_num@8@">@8@</span><span class="spat lotto_num lotto_num@9@">@9@</span><span class="spat lotto_num lotto_num@10@">@10@</span><span class="spat lotto_num lotto_num@11@">@11@</span><span class="spat lotto_bonus">+</span><span class="spat lotto_num lotto_num@12@">@12@</span>
</span>
<span class="lotto_sub">@5@회차<em class="lotto_date">(@13@.)</em></span>
</a>
</div>
</script>
<!-- 환율:엔화환율 -->
<script type="text/template" id="_atcmp_answer_9">
<div class="add_opt _item" data-sm="@2@" data-keyword="@1@" data-template_id="@0@" data-acir="@rank@">
<a href="javascript:;" class="opt_exchange opt_exchange_@11@">
<span class="opt_nation">
<img src="https://ssl.pstatic.net/sstatic/keypage/lifesrch/exchange/ico_@12@1.gif" alt="" />
@14@<span class="tx_nation">@money@</span>
</span>
<span class="opt_amount">
<span class="amount"><strong>@6@</strong>원</span><span class="changes"><i class="bullet">@10@</i> @8@ (@9@%)<span class="opt_time"><time datetime="@fulldate@">@7@</time></span></span>
</span>
</a>
</div>
</script>
<!-- 해외날씨 : 파리날씨 -->
<script type="text/template" id="_atcmp_answer_10">
<div class="add_opt _item" data-sm="@2@" data-keyword="@1@" data-template_id="@0@" data-acir="@rank@">
<a href="javascript:;" class="opt_weather">
<span class="opt_weather_thmb">
<img src="https://ssl.pstatic.net/sstatic/search/pc/img/wt_@6@.png" width="56" height="56" alt="@7@">
</span>
<span class="opt_weather_group">
<span class="opt_weather_state">@7@</span>
<span class="opt_weather_state">기온 <em class="opt_deg">@8@</em><span class="opt_unit">℃</span></span>
<span class="opt_weather_state">@9@ <em>@10@</em><span class="opt_unit">@11@</span></span>
<span class="opt_weather_state"><span class="opt_time"><time datetime="@fulldate@">@5@</time></span></span>
</span>
</a>
</div>
</script>
<!-- 국내날씨 : 서울날씨 -->
<script type="text/template" id="_atcmp_answer_11">
<div class="add_opt _item" data-sm="@2@" data-keyword="@1@" data-template_id="@0@" data-acir="@rank@">
<a href="javascript:;" class="opt_weather">
<span class="opt_weather_thmb">
<img src="https://ssl.pstatic.net/sstatic/search/pc/img/wt_@6@.png" width="56" height="56" alt="@7@">
</span>
<span class="opt_weather_group">
<span class="opt_weather_state">@7@</span>
<span class="opt_weather_state">기온 <em class="opt_deg">@8@</em><span class="opt_unit">℃</span></span>
<span class="opt_weather_state">@9@ <em>@10@</em><span class="opt_unit">@11@</span></span>
<span class="opt_weather_state"><span class="opt_time"><time datetime="@fulldate@">@5@</time></span></span>
</span>
</a>
</div>
</script>
<!-- 바로가기 -->
<script type="text/template" id="_atcmp_answer_17">
<div class="add_opt _item" data-sm="@2@" data-keyword="@1@" data-template_id="@0@" data-acir="@rank@">
<a href="@5@" target="_blank" class="opt_shortcut">
<span class="opt_url">@display_link@</span>
<span class="opt_txt">사이트로 바로 이동</span>
</a>
</div>
</script>
<!-- 해외날씨 : 국내날씨 형태로 제공하기 위한 새로운 템플릿(10번으로 ID변경됨) -->
<script type="text/template" id="_atcmp_answer_20"></script>
<!-- 문맥검색 -->
<script type="text/template" id="_atcmp_intend">
<div class="add_opt type_context _item" data-sm="asct" data-keyword="@transquery@" data-acir="@rank@">
<a href="#" class="opt_context">
<span class="opt_tit"><strong>@query@</strong></span>
<span class="opt_sub">@intend@</span>
</a>
</div>
</script>
<!-- 결과 키워드 템플릿 (좌측 결과목록 템플릿:정답형 템플릿 아님) -->
<script type="text/template" id="_atcmp_result_item_tpl">
<li class="_item @url_class@" data-acr="@rank@">
<a href="#" class="atcmp_keyword" onclick="return false;" title=""><span class="atcmp_keyword_txt">@txt@<span class="spat ic_expand"></span></span></a>
<a href="@url@" target="_blank" class="mquick">바로이동</a>
<span style="display:none">@in_txt@</span>
</li>
</script>
<!-- 일반 자동완성 하이라이팅 템플릿 -->
<script type="text/template" id="_atcmp_keyword_highlight_tpl">
@mismatch_before@<strong>@match@</strong>@mismatch_after@
</script>
<!-- 부분 자동완성 하이라이팅 템플릿 -->
<script type="text/template" id="_atcmp_keyword_partial_match_highlight_tpl">
@mismatch_before@<strong>@match@</strong>@mismatch_after@
</script>
</div>

</div>
</div>

<div id="promotion11">
<a href="https://search.naver.com/search.naver?sm=top_ros&amp;fbm=0&amp;ie=utf8&amp;query=%EB%8F%85%EB%8F%84%EC%9D%98+%EB%82%A0&amp;mra=bkI3" data-clk="top.ann">
<img src="https://s.pstatic.net/static/www/mobile/edit/2020/1015/mobile_170721960226.png" width="225" height="56" alt="독도의 날">
</a>
</div>
<div id="gnb">
<div id="NM_FAVORITE" class="gnb_inner">
<div class="group_nav">
<ul class="list_nav type_fix">
<li class="nav_item">
<a href="https://mail.naver.com/" class="nav" data-clk="svc.mail"><i class="ico_mail"></i>메일</a>
</li>
<li class="nav_item"><a href="https://section.cafe.naver.com/" class="nav" data-clk="svc.cafe">카페</a></li>
<li class="nav_item"><a href="https://section.blog.naver.com/" class="nav" data-clk="svc.blog">블로그</a></li>
<li class="nav_item"><a href="https://kin.naver.com/" class="nav" data-clk="svc.kin">지식iN</a></li>
<li class="nav_item"><a href="https://shopping.naver.com/" class="nav" data-clk="svc.shopping">쇼핑</a></li>
<li class="nav_item"><a href="https://order.pay.naver.com/home" class="nav" data-clk="svc.pay">Pay</a></li>
<li class="nav_item">
<a href="https://tv.naver.com/" class="nav" data-clk="svc.tvcast"><i class="ico_tv"></i>TV</a>
</li>
</ul>
<ul
class="list_nav NM_FAVORITE_LIST"
>
<li class="nav_item"><a href="https://dict.naver.com/" class="nav" data-clk="svc.dic">사전</a></li>
<li class="nav_item"><a href="https://news.naver.com/" class="nav" data-clk="svc.news">뉴스</a></li>
<li class="nav_item"><a href="https://finance.naver.com/" class="nav" data-clk="svc.stock">증권</a></li>
<li class="nav_item"><a href="https://land.naver.com/" class="nav" data-clk="svc.land">부동산</a></li>
<li class="nav_item"><a href="https://map.naver.com/" class="nav" data-clk="svc.map">지도</a></li>
<li class="nav_item"><a href="https://movie.naver.com/" class="nav" data-clk="svc.movie">영화</a></li>
<li class="nav_item"><a href="https://vibe.naver.com/" class="nav" data-clk="svc.vibe">VIBE</a>
<li class="nav_item"><a href="https://book.naver.com/" class="nav" data-clk="svc.book">책</a></li>
<li class="nav_item"><a href="https://comic.naver.com/" class="nav" data-clk="svc.webtoon">웹툰</a></li>

</ul>
<ul class="list_nav type_empty" style="display: none;"></ul>
<a href="#" role="button" class="btn_more" data-clk="svc.more">더보기</a>
<div class="ly_btn_area">
<a href="more.html" class="btn NM_FAVORITE_ALL" data-clk="map.svcmore">서비스 전체보기</a>
<a href="#" role="button" class="btn btn_set" data-clk="map.edit">메뉴설정</a>
<a href="#" role="button" class="btn btn_reset" data-clk="edt.reset">초기화</a>
<a href="#" role="button" class="btn btn_save" data-clk="edt.save">저장</a>
</div>
</div>
<div id="rtk" class="group_keyword" data-clk-prefix="lve">
<div id="NM_RTK_ROLLING_WRAP" class="keyword_area" data-clk="open"></div>
</div>
<div id="NM_RTK_VIEW" data-clk-prefix="lve"></div>

</div>
<div class="ly_service">
<div class="group_service NM_FAVORITE_ALL_LY"></div>
<div class="group_service NM_FAVORITE_EDIT_LY" style="display: none;"></div>
</div>
</div>
</div>
 <div id="container" role="main"> <div style="position:relative;width:1130px;margin:0 auto;z-index:11"> <div id="da_top"></div> <div id="da_expwide"></div> </div> <div id="NM_INT_LEFT" class="column_left">  <div id="veta_top"> <iframe id="da_iframe_time" name="da_iframe_time" data-iframe-src="https://siape.veta.naver.com/fxshow?su=SU10599&amp;nrefreshx=0" data-veta-preview="main_time" title="광고" width="750" height="135" marginheight="0" marginwidth="0" scrolling="no" frameborder="0"> </iframe> <span class="veta_bd_t"></span> <span class="veta_bd_b"></span> <span class="veta_bd_l"></span> <span class="veta_bd_r"></span> </div> <div id="newsstand" class="sc_newscast"> <h2 class="blind">뉴스스탠드</h2> <div id="NM_NEWSSTAND_HEADER" class="group_issue" data-clk-prefix="ncy"> <div class="issue_area"> <a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y" class="link_media" data-clk="newsflash">연합뉴스</a> <div id="yna_rolling" class="list_issue"> <div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968851" class="issue" data-clk="quickarticle">문대통령, 이건희 빈소에 조화…유족에 메시지 보낼 예정</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968372" class="issue" data-clk="quickarticle">이건희 주식재산만 18조…"상속세 10조 넘어 역대최대"</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968963" class="issue" data-clk="quickarticle">[이건희 별세] 외신, 장문 기사로 명암 상세히 조명</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968962" class="issue" data-clk="quickarticle">김봉현, 룸살롱 언제 갔나…'접대시점' 특정 주력</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968990" class="issue" data-clk="quickarticle">"클럽발 감염 기억해야" 핼러윈 앞두고 이태원-홍대 클럽등 점검</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968960" class="issue" data-clk="quickarticle">박능후 "독감백신 염려 끼쳐 송구…접종은 계속해야"</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968483" class="issue" data-clk="quickarticle">양심적 병역거부 63명, 내일 첫 소집…교도소서 36개월 합숙복무</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968579" class="issue" data-clk="quickarticle">5·18 부당징계 경찰관 급여 정산액 10만원…'40년 전 봉급대로'</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011969025" class="issue" data-clk="quickarticle">말 없이 굳은 표정…이재용, 아들·딸과 함께 아버지 빈소 도착</a></div>
<div><a href="http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011968460" class="issue" data-clk="quickarticle">사전투표한 트럼프 "트럼프라는 사내 찍었다"…멜라니아는 따로</a></div> </div> </div> <div class="direct_area"> <a href="http://news.naver.com/" class="link_news" data-clk="newshome">네이버뉴스</a>
<a href="http://entertain.naver.com/home" class="link_direct" data-clk="entertainment">연예</a>
<a href="http://sports.news.naver.com/" class="link_direct" data-clk="sports">스포츠</a>
<a href="http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101" class="link_direct" data-clk="economy">경제</a> </div> </div>       <div id="NM_NEWSSTAND_TITLE" class="group_title" data-clk-prefix="nsd"> <a href="http://newsstand.naver.com/" class="link_newsstand" data-clk="title" target="_blank">뉴스스탠드</a> <div id="NM_NEWSSTAND_data_buttons" class="sort_area">  <a href="#" role="button" data-type="my" data-clk="my" class="btn_sort">구독한 언론사</a> <a href="#" role="button" data-type="all" data-clk="all" class="btn_sort sort_on">전체언론사</a>  </div> <div id="NM_NEWSSTAND_view_buttons" class="set_area">  <a href="#" role="button" data-type="list" data-clk="articleview" class="btn_set"> <i class="ico_list"><span class="blind">리스트형</span></i></a> <a href="#" role="button" data-type="thumb" data-clk="pressview" class="btn_set set_on"> <i class="ico_tile"><span class="blind">썸네일형</span></i></a>  <a href="http://newsstand.naver.com/config.html" class="btn_set" data-clk="set" target="_blank"> <i class="ico_set"><span class="blind">설정</span></i></a> </div> </div> <div id="NM_NEWSSTAND_VIEW_CONTAINER" style="position:relative"> <div id="NM_NEWSSTAND_DEFAULT_LIST" class="group_news" style="display:none" data-clk-prefix="nsd_all"> <a href="#" role="button" class="pm_btn_prev_l _NM_NEWSSTAND_LIST_prev_btn" data-clk-custom="prev"><i class="ico_btn"><span class="blind">이전</span></i></a> <a href="#" role="button" class="pm_btn_next_l _NM_NEWSSTAND_LIST_next_btn" data-clk-custom="next"><i class="ico_btn"><span class="blind">다음</span></i></a> <div class="list_view"> <div class="option_area"> <div class="list_option_wrap"> <ul class="list_option"> <li class="option_item" data-cateid="ct2"><a href="#" class="option" data-clk="daei">종합/경제</a></li> <li class="option_item" data-cateid="ct3"><a href="#" class="option" data-clk="dtvcom">방송/통신</a></li> <li class="option_item" data-cateid="ct4"><a href="#" class="option" data-clk="dit">IT</a></li> <li class="option_item" data-cateid="ct5"><a href="#" class="option" data-clk="deng">영자지</a></li> <li class="option_item" data-cateid="ct6"><a href="#" class="option" data-clk="dsporent">스포츠/연예</a></li> <li class="option_item" data-cateid="ct7"><a href="#" class="option" data-clk="dmagtec">매거진/전문지</a></li> <li class="option_item" data-cateid="ct8"><a href="#" class="option" data-clk="dloc">지역</a></li> </ul> </div> </div> <div class="_NM_NEWSSTAND_ARTICLE_CONTAINER" data-clk-sub="*a"></div> </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_invalid" style="display:none" data-clk-sub="*a"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg">해당 언론사 사정으로 접근이 일시 제한됩니다.</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE">확인</a> </div> </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_undescribe_confirm" style="display:none" data-clk-sub="*a"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE" data-clk="usclose"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg"><strong class="NM_NEWSSTAND_POPUP_PNAME"></strong>을(를)<br>구독해지 하시겠습니까?</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CONFIRM" data-clk="usdone">확인</a> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE" data-clk="uscancel">취소</a> </div> </div> <div class="ly_toast NM_NEWSSTAND_TOAST" style="display:none"> <p class="toast_msg">구독한 언론사에 추가되었습니다.</p> </div> </div>     <div id="NM_NEWSSTAND_DEFAULT_THUMB" class="group_news" style="display:block" data-clk-prefix="nsd_all"> <a href="#" role="button" class="pm_btn_prev_l _NM_UI_PAGE_PREV" data-clk-custom="prev"><i class="ico_btn"><span class="blind">이전</span></i></a> <a href="#" role="button" class="pm_btn_next_l _NM_UI_PAGE_NEXT" data-clk-custom="next"><i class="ico_btn"><span class="blind">다음</span></i></a> <div class="_NM_UI_PAGE_CONTAINER" style="height:100%;overflow:hidden" data-clk-sub="*p">   <div style="width: 750px; float: left;">
<div class="tile_view">
<div class="frame_area">
<i class="line to_right1"></i>
<i class="line to_right2"></i>
<i class="line to_right3"></i>
<i class="line to_bottom1"></i>
<i class="line to_bottom2"></i>
<i class="line to_bottom3"></i>
<i class="line to_bottom4"></i>
<i class="line to_bottom5"></i>
</div>
<div class="thumb_area">
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="020"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/020.png"
height="20"
alt="동아일보"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="020"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="020"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=020"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="020"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="038"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/038.png"
height="20"
alt="한국일보"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="038"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="038"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=038"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="038"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="904"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/904.png"
height="20"
alt="JTBC"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="904"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="904"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=904"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="904"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="214"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/214.png"
height="20"
alt="MBC"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="214"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="214"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=214"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="214"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="055"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/055.png"
height="20"
alt="SBS"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="055"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="055"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=055"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="055"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="047"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/047.png"
height="20"
alt="오마이뉴스"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="047"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="047"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=047"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="047"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="006"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/006.png"
height="20"
alt="미디어오늘"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="006"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="006"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=006"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="006"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="023"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/up/2020/0903/nsd185246724.png"
height="20"
alt="조선일보"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="023"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="023"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=023"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="023"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="015"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/015.png"
height="20"
alt="한국경제"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="015"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="015"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=015"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="015"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="016"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/016.png"
height="20"
alt="헤럴드경제"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="016"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="016"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=016"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="016"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="079"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/079.png"
height="20"
alt="노컷뉴스"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="079"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="079"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=079"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="079"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="005"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/005.png"
height="20"
alt="국민일보"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="005"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="005"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=005"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="005"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="002"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/002.png"
height="20"
alt="프레시안"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="002"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="002"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=002"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="002"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="025"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/025.png"
height="20"
alt="중앙일보"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="025"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="025"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=025"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="025"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="018"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/018.png"
height="20"
alt="이데일리"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="018"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="018"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=018"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="018"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="143"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/143.png"
height="20"
alt="쿠키뉴스"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="143"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="143"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=143"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="143"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="934"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/934.png"
height="20"
alt="아리랑TV"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="934"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="934"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=934"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="934"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="955"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/955.png"
height="20"
alt="독서신문"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="955"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="955"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=955"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="955"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="346"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/346.png"
height="20"
alt="헬스조선"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="346"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="346"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=346"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="346"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="135"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/135.png"
height="20"
alt="시사저널"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="135"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="135"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=135"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="135"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="094"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/094.png"
height="20"
alt="월간 산"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="094"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="094"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=094"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="094"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="361"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/361.png"
height="20"
alt="채널예스"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="361"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="361"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=361"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="361"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="960"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/up/2020/1011/nsd205137204.png"
height="20"
alt="e대한경제"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="960"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="960"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=960"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="960"
>기사보기</a
>
</div>
</div>
<div
class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"
data-pid="908"
>
<a href="#" class="thumb">
<img
src="https://s.pstatic.net/static/newsstand/2020/logo/dark/0604/908.png"
height="20"
alt="국방일보"
class="news_logo"
/>
<span class="thumb_dim"></span
></a>
<div class="popup_wrap">
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_subscribe_press"
data-pid="908"
data-clk="sub"
>구독</a
>
<a
href="#"
role="button"
class="btn_popup _NM_NEWSSTAND_THUMB_unsubscribe_press"
data-pid="908"
data-clk="unsub"
>해지</a
>
<a
href="http://newsstand.naver.com/?list=&pcode=908"
target="_blank"
class="btn_popup"
data-clk="logo"
data-pid="908"
>기사보기</a
>
</div>
</div>
</div>
</div>
</div>
  </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_invalid" style="display:none"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg">해당 언론사 사정으로 접근이 일시 제한됩니다.</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE">확인</a> </div> </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_undescribe_confirm" style="display:none" data-clk-sub="*a"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE" data-clk="usclose"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg"><strong class="NM_NEWSSTAND_POPUP_PNAME"></strong>을(를)<br/>구독해지 하시겠습니까?</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CONFIRM" data-clk="usdone">확인</a> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE" data-clk="uscancel">취소</a> </div> </div> <div class="ly_toast NM_NEWSSTAND_TOAST" style="display:none"> <p class="toast_msg">구독한 언론사에 추가되었습니다.</p> </div> </div> <div id="NM_NEWSSTAND_MY_LIST" class="group_news" style="display:none" data-clk-prefix="nsd_myn"> <a href="#" role="button" class="pm_btn_prev_l _NM_NEWSSTAND_LIST_prev_btn" data-clk-custom="prev"><i class="ico_btn"></i><span class="blind">이전</span></a> <a href="#" role="button" class="pm_btn_next_l _NM_NEWSSTAND_LIST_next_btn" data-clk-custom="next"><i class="ico_btn"></i><span class="blind">다음</span><span class="blind">다음</span></a> <div class="list_view"> <div class="option_area"> <div class="list_option_wrap"> <ul class="list_option _NM_NEWSSTAND_MY_presslist"> <!-- nvpaperlist:empty --> </ul> </div> </div> <div class="_NM_NEWSSTAND_ARTICLE_CONTAINER" data-clk-sub="*a">  </div> </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_invalid" style="display:none"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg">해당 언론사 사정으로 접근이 일시 제한됩니다.</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE">확인</a> </div> </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_undescribe_confirm" style="display:none" data-clk-sub="*a"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE" data-clk="usclose"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg"><strong class="NM_NEWSSTAND_POPUP_PNAME"></strong>을(를)<br>구독해지 하시겠습니까?</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CONFIRM" data-clk="usdone">확인</a> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE" data-clk="uscancel">취소</a> </div> </div> </div> <div id="NM_NEWSSTAND_MY_THUMB" class="group_news" style="display:none" data-clk-prefix="nsd_myn"> <a href="#" role="button" class="pm_btn_prev_l _NM_UI_PAGE_PREV" data-clk-custom="prev"><i class="ico_btn"><span class="blind">이전</span></i></a> <a href="#" role="button" class="pm_btn_next_l _NM_UI_PAGE_NEXT" data-clk-custom="next"><i class="ico_btn"><span class="blind">다음</span></i></a> <div class="_NM_UI_PAGE_CONTAINER" data-clk-sub="*p"></div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_invalid" style="display:none"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg">해당 언론사 사정으로 접근이 일시 제한됩니다.</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE">확인</a> </div> </div> <div class="ly_popup NM_NEWSSTAND_POPUP NM_NEWSSTAND_undescribe_confirm" style="display:none" data-clk-sub="*a"> <a href="#" role="button" class="btn_close NM_NEWSSTAND_POPUP_CLOSE" data-clk="usclose"><i class="ico_close"></i><span class="blind">닫기</span></a> <p class="popup_msg"><strong class="NM_NEWSSTAND_POPUP_PNAME"></strong>을(를)<br>구독해지 하시겠습니까?</p> <div class="popup_btn"> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CONFIRM" data-clk="usdone">확인</a> <a href="#" role="button" class="btn_confirm NM_NEWSSTAND_POPUP_CLOSE" data-clk="uscancel">취소</a> </div> </div> </div> <div id="NM_NEWSSTAND_MY_EMPTY" class="group_news" style="display:none"> <div class="error_view"> <div class="error_area"> <strong class="error_msg">구독한 언론사가 없습니다.</strong> <p class="dsc_msg">언론사 구독 설정에서 관심있는 언론사를 구독하시면<br>언론사가 직접 편집한 뉴스들을 네이버 홈에서 바로 보실 수 있습니다.</p> <a href="http://newsstand.naver.com/config.html" class="link_redirect" target="_blank">언론사 구독 설정하기</a> </div> </div> </div> </div> </div> <!-- EMPTY --> <div id="NM_THEMECAST_CONTENTS_CONTAINER"> <div id="themecast" class="sc_themecast id_law" >
	<h2 class="blind">주제별 캐스트</h2>
	<div class="theme_head">
		<div class="group_title">
	<div class="title_area">
		<strong class="title">오늘 읽을만한 글</strong><span class="dsc">주제별로 분류된 다양한 글 모음</span>
	</div>
	<div class="info_area">
		
			<span class="info"><strong class="new">2,063</strong> 개의 글</span>
		
		<a id="NM_THEME_EDIT_SET" href="#" role="button" class="btn_set" data-clk="tca.like">관심주제 설정</a>
	</div>
</div>
<div class="theme_fix_wrap">
	<div id="NM_THEME_CATE_GROUPS" class="group_category" data-demo-key="m_19_29">
		<div class="main_category">
			<a href="#" role="button" class="pm_btn_prev NM_THEME_PREV" data-clk="tct.prev" style="display: none;">
				<i class="ico_btn"><span class="blind">이전</span></i>
			</a>
			<a href="#" role="button" class="pm_btn_next NM_THEME_NEXT" data-clk="tct.next" style="display: none;">
				<i class="ico_btn"><span class="blind">다음</span></i>
			</a>
			<div id="NM_THEME_CATE_FLICK" class="_NM_UI_PAGE_CONTAINER" style="height: 49px; overflow: hidden;">
				
					<div style="width: 750px;">
						<ul class="list_category" role="tablist">
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_enter"
									   aria-selected="false"
									   data-clk="tct.tvc" data-panel-code="ENTER">엔터</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_sports"
									   aria-selected="false"
									   data-clk="tct.spo" data-panel-code="SPORTS">스포츠</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_bboom"
									   aria-selected="false"
									   data-clk="tct.web" data-panel-code="BBOOM">웹툰</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_cargame"
									   aria-selected="false"
									   data-clk="tct.aut" data-panel-code="CARGAME">자동차</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_gameapp"
									   aria-selected="false"
									   data-clk="tct.gam" data-panel-code="GAMEAPP">게임</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_ittech"
									   aria-selected="false"
									   data-clk="tct.tec" data-panel-code="ITTECH">테크</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_movie"
									   aria-selected="false"
									   data-clk="tct.mov" data-panel-code="MOVIE">영화</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_finance"
									   aria-selected="false"
									   data-clk="tct.fin" data-panel-code="FINANCE">경제M</a>
								</li>
							
						</ul>
					</div>
				
					<div style="width: 750px;">
						<ul class="list_category" role="tablist">
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_living"
									   aria-selected="false"
									   data-clk="tct.fod" data-panel-code="LIVING">푸드</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_science"
									   aria-selected="false"
									   data-clk="tct.sci" data-panel-code="SCIENCE">과학</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_job"
									   aria-selected="false"
									   data-clk="tct.job" data-panel-code="JOB">JOB&amp;</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_travel"
									   aria-selected="false"
									   data-clk="tct.tra" data-panel-code="TRAVEL">여행+</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_wedding"
									   aria-selected="false"
									   data-clk="tct.wed" data-panel-code="WEDDING">연애·결혼</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_culture"
									   aria-selected="false"
									   data-clk="tct.bok" data-panel-code="CULTURE">책문화</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_health"
									   aria-selected="false"
									   data-clk="tct.hea" data-panel-code="HEALTH">건강</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_livinghome"
									   aria-selected="false"
									   data-clk="tct.lif" data-panel-code="LIVINGHOME">리빙</a>
								</li>
							
						</ul>
					</div>
				
					<div style="width: 750px;">
						<ul class="list_category" role="tablist">
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_business"
									   aria-selected="false"
									   data-clk="tct.bsn" data-panel-code="BUSINESS">비즈니스</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_law"
									   aria-selected="true"
									   data-clk="tct.law" data-panel-code="LAW">법률</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_beauty"
									   aria-selected="false"
									   data-clk="tct.bty" data-panel-code="BEAUTY">패션뷰티</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_animal"
									   aria-selected="false"
									   data-clk="tct.ani" data-panel-code="ANIMAL">동물공감</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_design"
									   aria-selected="false"
									   data-clk="tct.des" data-panel-code="DESIGN">디자인</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_china"
									   aria-selected="false"
									   data-clk="tct.chn" data-panel-code="CHINA">중국</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_show"
									   aria-selected="false"
									   data-clk="tct.sow" data-panel-code="SHOW">공연전시</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_farm"
									   aria-selected="false"
									   data-clk="tct.far" data-panel-code="FARM">FARM</a>
								</li>
							
						</ul>
					</div>
				
					<div style="width: 750px;">
						<ul class="list_category" role="tablist">
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_momkids"
									   aria-selected="false"
									   data-clk="tct.mom" data-panel-code="MOMKIDS">부모i</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_with"
									   aria-selected="false"
									   data-clk="tct.pub" data-panel-code="WITH">함께N</a>
								</li>
							
								<li class="category_item" role="presentation">
									
									
									<a href="#" role="tab" class="_NM_THEME_CATE tab id_school"
									   aria-selected="false"
									   data-clk="tct.scl" data-panel-code="SCHOOL">스쿨잼</a>
								</li>
							
						</ul>
					</div>
				
			</div>
		</div>
	</div>
</div>

	</div>
	<div class="theme_cont" data-panel-code="LAW">
		<div class="group_topstory" data-block-id="5f928021d6960d1025ccdc00" data-block-code="PC-THEME-LAW-EDIT-AREA" data-block-type="BLOCKS" data-template-code="PC-THEMECAST-EDIT-AREA"

	 data-da="margin-top"
	 >

	<div class="topstory_inner" data-block-id="5f927eac362010101331d43d" data-block-code="PC-THEME-LAW-EDIT-AREA-ITEM" data-block-type="A-MATERIAL" data-template-code="IMAGE1"

	 >

	
		<div class="topstory_view ">

			
			
			<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29770713&amp;memberNo&#x3D;38212397" class="topstory_thumb"
			   data-clk="tcc_law.editbigimg1"
			   target="_blank">
				<img src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_728x360_45376680972946707.jpeg" data-src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_728x360_45376680972946707.jpeg" alt="&quot;살찌는 것 싫어&quot; 여친에게 몰래 식욕억제제 먹인 남성" width="364" height="180">

				
					<span class="thumb_bd"></span>
				
			</a>
			<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29770713&amp;memberNo&#x3D;38212397" class="topstory_info"
			   data-clk="tcc_law.editbigtxt1"
			   target="_blank">
				
					<em class="theme_category">생활법률 뉴스</em>
				

				<strong class="title line_two ">"살찌는 것 싫어" 여친에게 몰래 식욕억제제 먹인 남성</strong>
				

				
					<div class="source_area">
						<span class="source"><span class="source_inner">네이버 법률</span></span>
					</div>
				
			</a>
			
		</div>
	
</div>
<div class="topstory_inner" data-block-id="5f927f5b162575baec1640c1" data-block-code="PC-THEME-LAW-EDIT-AREA-ITEM" data-block-type="MATERIALS" data-template-code="IMAGE3"

	 >

	<div class="list_theme_wrap type_topstory">
		<ul class="list_theme">
			
			<li class="theme_item">
				
				
				<a href="https://blog.naver.com/naverlaw/222123245866" class="theme_thumb" data-clk="tcc_law.editsmallimg1" target="_blank">
					<img src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_196x196_45376721804432299.png" data-src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_196x196_45376721804432299.png" alt="&quot;역주행 자전거가 달려와 쿵&quot;…무조건 치료비 내놓으라는 부모" width="98" height="98">

					
						<span class="thumb_bd"></span>
					
				</a>
				<a href="https://blog.naver.com/naverlaw/222123245866" class="theme_info" data-clk="tcc_law.editsmalltxt1" target="_blank">
					<em class="theme_category">온라인 핫이슈</em>
					<strong class="title">"역주행 자전거가 달려와 쿵"…무조건 치료비 내놓으라는 부모 </strong>
					<div class="source_box">
						<span class="source"><span class="source_inner">네이버 법률</span></span>
					</div>
				</a>
			</li>
			
			<li class="theme_item">
				
				
				<a href="https://blog.naver.com/naverlaw/222121850576" class="theme_thumb" data-clk="tcc_law.editsmallimg2" target="_blank">
					<img src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_196x196_45376819411890056.jpeg" data-src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_196x196_45376819411890056.jpeg" alt="&quot;남의 물건인지 알면서도…&quot; 잘못 배송된 &#x27;몽클○○&#x27; 패딩 가로챈 이웃" width="98" height="98">

					
						<span class="thumb_bd"></span>
					
				</a>
				<a href="https://blog.naver.com/naverlaw/222121850576" class="theme_info" data-clk="tcc_law.editsmalltxt2" target="_blank">
					<em class="theme_category">온라인 핫이슈</em>
					<strong class="title">"남의 물건인지 알면서도…" 잘못 배송된 '몽클○○' 패딩 가로챈 이웃 </strong>
					<div class="source_box">
						<span class="source"><span class="source_inner">네이버 법률</span></span>
					</div>
				</a>
			</li>
			
			<li class="theme_item">
				
				
				<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29770073&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.editsmallimg3" target="_blank">
					<img src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_196x196_45376849419831984.jpeg" data-src="https://s.pstatic.net/static/www/mobile/edit/2020/1023/cropImg_196x196_45376849419831984.jpeg" alt="&#x27;품절 한정판 LP&#x27; 웃돈 붙여 되파는 리셀러들, 막을 수 없을까" width="98" height="98">

					
						<span class="thumb_bd"></span>
					
				</a>
				<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29770073&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.editsmalltxt3" target="_blank">
					<em class="theme_category">생활법률 뉴스</em>
					<strong class="title">'품절 한정판 LP' 웃돈 붙여 되파는 리셀러들, 막을 수 없을까 </strong>
					<div class="source_box">
						<span class="source"><span class="source_inner">네이버 법률</span></span>
					</div>
				</a>
			</li>
			
		</ul>
	</div>
</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-0" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="1"
	 >

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_e6e0dba4-14c9-11eb-b67a-afbafbc9d16e" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222123323074" class="theme_thumb" data-clk="tcc_law.list1cont1" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19432697128274806NxM4W.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19432697128274806NxM4W.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;평생 맞고 살았다&quot; 전 남편 성기 절단한 60대, 정당방위 인정될까" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222123323074" class="theme_info" data-clk="tcc_law.list1cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"평생 맞고 살았다" 전 남편 성기 절단한 60대, 정당방위 인정될까</strong>
						<p class="desc">수면제를 먹인 후 이혼한 전 남편의 성기와 오른쪽 손목을 흉기로 절단한 엽기적인 사건이 발생했습니다. 그런데 재판부는 사건의 범인인 60대 여성에 대한 1심 선고를 연기했습니다. 이 여성이 이런 범행을 실행에 옮기게 된 과정이 참 딱했기 때문입니다. ​지난 6월 범행을 저지르고 재판에 넘겨진 A씨의 선고 공판은 당초 지난 22일 서울북부지법에서 열릴 예정이</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_340007fb-11d7-11eb-a65c-6fc2a9f3b37c" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29739666" class="theme_thumb" data-clk="tcc_law.list1cont2" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19108644370673067twstJ.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19108644370673067twstJ.jpg%22&amp;type&#x3D;nf340_228" alt="담배 회사의 끔찍한 실험...&quot;마스크 씌운채 강제로 담배 연기 마시게 해&quot;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29739666" class="theme_info" data-clk="tcc_law.list1cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">담배 회사의 끔찍한 실험..."마스크 씌운채 강제로 담배 연기 마시게 해"</strong>
						<p class="desc">담배의 해로움 측정위한 동물실험일부 담배 회사에서 담배의 해로움을 알아보기 위해 동물들에게 해로운 물질을 강제적으로 주입한다는 사실이 드러났습니다. 실험용 비글부터 토끼, 원숭이 등 다양한 동물들이 인간에게 덜 해로운 담배를 만들기 위해 이용되고 있습니다. 다시 말해, 담배 제품이 출시되기 전에 동물실험이 진행되고 있다는 것입니다.담배 동물실험의 종류세계보</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">팸타임스</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_f8e6f40c-1362-11eb-9673-af9a647a355d" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222122136270" class="theme_thumb" data-clk="tcc_law.list1cont3" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19278731492400940dCvCO.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19278731492400940dCvCO.jpg%22&amp;type&#x3D;nf340_228" alt="불법 도박 빠져 학생회비 2000만원 &#x27;꿀꺽&#x27;한 학생회 간부" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222122136270" class="theme_info" data-clk="tcc_law.list1cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">불법 도박 빠져 학생회비 2000만원 '꿀꺽'한 학생회 간부</strong>
						<p class="desc">지난 19일, 서경대학교 총학생회 임원이 불법 도박을 목적으로 학생회비를 횡령한 사실이 밝혀져 논란이 일고 있습니다.​서경대 학생회 측은 사무국장 A씨가 7월부터 10월까지 총 38회, 불법 사설 도박 및 통신비의 목적으로 2004만 1600원을 횡령한 사실을 확인했다고 전했습니다. 이에 집행부를 긴급 소집하고 사무국장을 소환해 자필 진술서와 변제 각서를 </p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_340007fc-11d7-11eb-a65c-b1423d16e491" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29758917" class="theme_thumb" data-clk="tcc_law.list1cont4" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19279388216559312MmY3O.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19279388216559312MmY3O.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;관람객 충격&#x27; 곰에게 습격 받은 후 질질 끌려간 동물원 사육사" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29758917" class="theme_info" data-clk="tcc_law.list1cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'관람객 충격' 곰에게 습격 받은 후 질질 끌려간 동물원 사육사</strong>
						<p class="desc">얼마 전 중국의 상하이 야생 동물 공원에서 끔찍한 사고가 일어났습니다. 바로 작업 중이던 사육사가 곰 떼의 습격을 받아 숨진 것이었습니다.이 사육사가 참변을 당한 곳은 관람객들도 사파리 차량을 타고 들어가야 구경을 할 수 있는 장소였는데요. 이곳에서 작업을 하다 곰의 공격을 받은 것이었습니다. 이 사육사가 곰의 공격을 받자 인근에서 작업 중이던 굴착기 운전</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">레드프라이데이</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-1" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="1"
	 >

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_e6e0dba5-14c9-11eb-b67a-83ea7d8ee758" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222120020794" class="theme_thumb" data-clk="tcc_law.list2cont1" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_1943276469981945628Xyl.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_1943276469981945628Xyl.jpg%22&amp;type&#x3D;nf340_228" alt="현실판 &#x27;인간수업&#x27;, 동갑내기 성매매 협박한 남고생 집행유예... 왜?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222120020794" class="theme_info" data-clk="tcc_law.list2cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">현실판 '인간수업', 동갑내기 성매매 협박한 남고생 집행유예... 왜?</strong>
						<p class="desc">​ 동갑 여학생을 30여 차례 성매매하도록 강요한 10대 남고생이 집행유예를 선고받아 논란입니다. ​피고인 A학생은 지난해 11월 트위터로 피해자를 알게 됐습니다. A 학생은 채팅 어플을 통해 성매매를 알선했고 알선 수수료를 챙기는 등 용돈벌이를 했는데요. 피해자가 20여 차례 성매매를 한 뒤 더 이상 하지 않겠다며 거부했지만 A 학생은 &#x27;산부인과에 다닌 </p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_31694f65-14c5-11eb-9673-974919a5c944" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222122588589" class="theme_thumb" data-clk="tcc_law.list2cont2" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19430842957393453YLTse.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19430842957393453YLTse.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;장소·커피 협찬해주세요&quot; 막무가내 요구 거절했더니…" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222122588589" class="theme_info" data-clk="tcc_law.list2cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"장소·커피 협찬해주세요" 막무가내 요구 거절했더니…</strong>
						<p class="desc">최근 한 온라인 커뮤니티에 올라온 카페 협찬 요구 문자가 화제입니다. ​이 카페사장 A씨는 한 학생으로부터 카페를 대여하고 싶다는 문자를 받았습니다. 8명의 학생이 모여 매주 합평회를 하는데 8인 테이블을 보유한 카페가 이곳밖에 없다는 이유였습니다.​A씨는 코로나로 인해 매장 대여를 하고 있지 않다며 학생의 요구를 거절했습니다. 그러나 학생은 갑자기 장소와</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_8e7354d3-1434-11eb-9673-a9878ce4637f" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29763182&amp;memberNo&#x3D;5011620" class="theme_thumb" data-clk="tcc_law.list2cont3" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19368577793594720gPKt7.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19368577793594720gPKt7.jpg%22&amp;type&#x3D;nf340_228" alt="주민등록번 변경하면, 새번호는 어떻게 정할까?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29763182&amp;memberNo&#x3D;5011620" class="theme_info" data-clk="tcc_law.list2cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">주민등록번 변경하면, 새번호는 어떻게 정할까?</strong>
						<p class="desc">[2020년 달라지는 법, 퀴즈로 알자] 10월부터 주민등록번호를 신규부여받거나 변경하는 경우,성별표시 첫 자리를 제외하고 6자리 임의번호가 부여된다?주민등록번호 뒷자리 성별표시 첫 자리를 제외하고 6자리 임의번호가 부여된다?맞으면 O, 틀리면 X!법령퀴즈 참여자 중 정답을 맞힌 총 5명을 추첨하여 달콤한 고구마 라떼를 선물로 드릴게요! -참여기간: 20.</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">법제처</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_77066173-14f2-11eb-b67a-b78edef7b651" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29779125&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list2cont4" target="_blank">
						<img src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_194503121668214568yEfP.jpg%22&amp;type&#x3D;nf340_228" data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_194503121668214568yEfP.jpg%22&amp;type&#x3D;nf340_228" alt="연기학원에서 댄스·보컬 강의까지? 법원 &quot;교습정지 정당&quot;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29779125&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list2cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">연기학원에서 댄스·보컬 강의까지? 법원 "교습정지 정당"</strong>
						<p class="desc">&quot;춤과 노래 역시 연기의 일부에 해당한다.&quot; 학원 원장의 이 주장은 받아들여지지 않았다. 법원은 연기로만 교습과정을 등록해두고 춤이나 노래까지 함께 가르친 학원의 행위는 제재 받아 마땅하다고 판단했다. 서울행정법원 행정11부(부장판사 박형순)는 서울 강남구 신사동 가로수길 인근 A 연기학원이 낸 교습정지처분취소 청구를 최근 </p>
						<div class="source_box">
							<span class="date">2일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-2" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="2"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_8e7354d4-1434-11eb-9673-0993794afbd7" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29682271&amp;memberNo&#x3D;5011620" class="theme_thumb" data-clk="tcc_law.list3cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19368760055550948lIdyK.jpg%22&amp;type&#x3D;nf340_228" alt="예전에 쓰던 차량 번호 자동차, 그대로 다시 쓸 수 있나요?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29682271&amp;memberNo&#x3D;5011620" class="theme_info" data-clk="tcc_law.list3cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">예전에 쓰던 차량 번호 자동차, 그대로 다시 쓸 수 있나요?</strong>
						<p class="desc">말소등록 된 차량 소유자가 그 번호를 신규등록 차량에 다시 부여받으려면 말소등록된 날부터 6개월 이내여야 합니다. 「자동차등록령」 제21조제1항 및 제2항</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">법제처</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_09f48440-14ce-11eb-a5fb-93ea55c9729c" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222122997507" class="theme_thumb" data-clk="tcc_law.list3cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19358439489485015wCa6r.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;마음에 들어요&quot; 수능 원서 보고 연락한 수능 감독관" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222122997507" class="theme_info" data-clk="tcc_law.list3cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"마음에 들어요" 수능 원서 보고 연락한 수능 감독관</strong>
						<p class="desc">&quot;사실 A씨가 맘에 듭니다&quot;​지난 2018년 겨울, 대학수학능력시험을 치른 수험생 A양이 수능 열흘 후 모르는 남성으로부터 뜻밖의 카카오톡 메시지를 받습니다. ​알고 보니 A양에게 연락을 한 건 수능 시험 당일 A양이 시험을 본 고사장의 감독을 맡았던 30대 남성이었습니다. 조사 결과 고교 교사로 재직중인 이 남성은 당시 감독관 신분으로 교육청에게 받은 응</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_77066172-14f2-11eb-b67a-2fa8c6b5d750" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29779103&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list3cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19450271883818404Hzeui.jpg%22&amp;type&#x3D;nf340_228" alt="퇴근 중 사고로 공황장애 악화돼 극단적 선택했다면…" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29779103&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list3cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">퇴근 중 사고로 공황장애 악화돼 극단적 선택했다면…</strong>
						<p class="desc">평소 공황장애를 앓던 회사원 A씨가 있다. 그는 어느날 퇴근을 위해 탄 회사 엘리베이터에 갇히고 말았다. 이후 공황장애가 더 심해진 A씨는 끝내 극단적 선택을 하고 말았다. 이 경우 법적으로 &#x27;업무상 재해&#x27;를 인정받을 수 있을까? 법원은 인정해야 한다고 판단했다. 서울행정법원 행정3부는 A씨의 유족이 근로복지공단을 상대로 낸 유족급여 및 장의비부지급처분취소</p>
						<div class="source_box">
							<span class="date">2일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_499e8bfc-11d7-11eb-82bf-952ee0fba295" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29746738" class="theme_thumb" data-clk="tcc_law.list3cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19436132967891584Yiib9.jpg%22&amp;type&#x3D;nf340_228" alt="‘역대급’으로 심각한 20대, 현실도 미래도 깜깜" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29746738" class="theme_info" data-clk="tcc_law.list3cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">‘역대급’으로 심각한 20대, 현실도 미래도 깜깜</strong>
						<p class="desc">‘요즘 안 힘든 사람이 어디 있냐’, ‘우리도 힘들었다’ 이런 말은 위로가 안 된다는 거 잊지 마세요. 기획 : 이석희 기자 / 그래픽 : 홍연택 기자 &lt;ⓒ 온라인 경제미디어 뉴스웨이 - 무단전재 및 재배포 금지&gt;</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">뉴스웨이</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_e6e0dba6-14c9-11eb-b67a-c5c106687aac" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222122103347" class="theme_thumb" data-clk="tcc_law.list3cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_194328281893969712pgIK.jpg%22&amp;type&#x3D;nf340_228" alt="AI로 &#x27;딥페이크 사진&#x27; 만든 텔레그램 대화방" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222122103347" class="theme_info" data-clk="tcc_law.list3cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">AI로 '딥페이크 사진' 만든 텔레그램 대화방</strong>
						<p class="desc">인공지능(AI) 기술을 이용해 여성의 나체사진을 만들어주는 텔레그램 대화방이 등장해 논란입니다.​해당 텔레그램방의 존재는 영국 공영방송 BBC의 보도로 세상에 알려졌는데요. 이 텔레그램방은 &#x27;딥페이크봇&#x27; 기술을 이용, SNS에 올라온 여성들의 사진을 조작해 나체사진으로 만들었습니다. AI 기술로 사진 속 여성의 옷을 제거해 나체 상태로 만드는 건데...</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-3" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="2"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_499e8bfd-11d7-11eb-82bf-c3393ace47ea" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29756644&amp;memberNo&#x3D;30654798&amp;searchKeyword&#x3D;%EC%B2%AD%EB%85%84%EC%A0%95%EC%B1%85&amp;searchRank&#x3D;11" class="theme_thumb" data-clk="tcc_law.list4cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_194359421000233501K5kb.jpg%22&amp;type&#x3D;nf340_228" alt="담당자에게 직접 물었다! 청년특별구직지원금 Q&amp;A" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29756644&amp;memberNo&#x3D;30654798&amp;searchKeyword&#x3D;%EC%B2%AD%EB%85%84%EC%A0%95%EC%B1%85&amp;searchRank&#x3D;11" class="theme_info" data-clk="tcc_law.list4cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">담당자에게 직접 물었다! 청년특별구직지원금 Q&A</strong>
						<p class="desc">코로나19 상황 속 청년들을 위한 지원금인 만큼 많은 관심을 받은 &#x27;청년특별구직지원금&#x27;! 많은 관심만큼 청년들의 궁금증도 많을텐데요. 그래서 준비했습니다. 청년특별구직지원금 15문 15답! 청정이가 질문을 받고, 담당 사무관님에게 답변을 들어봤습니다! 하나씩 함께 살펴볼까요?Q1. 청년특별구직활동지원금의 취지는 무엇인가요? ▶ 코로나19로 인한 채용 축소&amp;</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">청년정책</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_99926b37-14c3-11eb-9673-e3abe9195df4" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29769533&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list4cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19429955948143063J6Rqt.jpg%22&amp;type&#x3D;nf340_228" alt="아직도 엄마 카드 쓴다는 홍현희, 증여세 내야 할까?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29769533&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list4cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">아직도 엄마 카드 쓴다는 홍현희, 증여세 내야 할까?</strong>
						<p class="desc">사진&#x3D;TV 조선 &#x27;아내의 맛&#x27; 캡처 개그우먼 홍현희가 아직까지 엄마 신용카드를 쓴다고 밝혀 화제입니다. 홍현희는 최근 한 방송에서 양가 부모님 용돈에 대해 이야기하며 &quot;친정 어머니한테 생활비를 안 드린다&quot;고 말해 출연진을 놀라게 했는데요.홍현희는 어머니가 항상 자신보다 돈이 많다며 &quot;39살인데 아직도 가끔씩 어머니 카드를 사용한다&quot;고 </p>
						<div class="source_box">
							<span class="date">2일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_176fdd9c-129b-11eb-8043-176632bffc74" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29750761&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list4cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1021%2Fupload_19192898102766793bVq4Z.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;롤렉스만 돌려줘 3000만원 줄게&quot; 시계 가져간 男 자수했는데..." width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29750761&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list4cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"롤렉스만 돌려줘 3000만원 줄게" 시계 가져간 男 자수했는데...</strong>
						<p class="desc">/사진&#x3D;온라인 커뮤니티 캡처 고속도로 휴게소에서 주인이 두고 간 고가의 명품 시계를 챙긴 남성이 자수했습니다. 시계 주인이 사례금을 걸고 온라인 커뮤니티에 글을 올린 지 이틀만입니다. ◇실수로 화장실에 두고 온 손가방…시계만 사라졌다 30대 남성 A씨는 지난 8월 충북 괴산휴게소 화장실에 명품 시계와 현금이 담긴 손가방을 두고 나왔습니다. 비슷한 시</p>
						<div class="source_box">
							<span class="date">2일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_176fdd9d-129b-11eb-8043-ad0789e4c241" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222121104152" class="theme_thumb" data-clk="tcc_law.list4cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1021%2Fupload_19193522503049625aW4MQ.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;볼 일 급한&#x27; 음주 뺑소니범이 찾아간 곳이 하필이면..." width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222121104152" class="theme_info" data-clk="tcc_law.list4cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'볼 일 급한' 음주 뺑소니범이 찾아간 곳이 하필이면...</strong>
						<p class="desc">화장실이 급해 제 발로 경찰서를 찾아간 음주 뺑소니범의 이야기가 화제입니다.​지난 15일 운전 중이던 A씨는 볼일을 보기 위해 인근에 위치한 해운대경찰서를 들렀습니다. 시동 끌 정신도 없었던 A씨는 요란한 음악을 그대로 켜놓은 채 화장실로 달려갔는데요. 해당 차량을 수상하게 여긴 경찰이 운전자를 찾아 나섰고 마침 볼일을 마치고 나온 A씨와 마주치게 됐습니다</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_99926b3b-14c3-11eb-9673-c1e60f7ea427" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?memberNo&#x3D;38212397&amp;volumeNo&#x3D;29760058" class="theme_thumb" data-clk="tcc_law.list4cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19430182030244016VcLSZ.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;민식이법 기소&#x27; 50대에 무죄…&#x27;0.3초&#x27;가 처벌 갈랐다" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?memberNo&#x3D;38212397&amp;volumeNo&#x3D;29760058" class="theme_info" data-clk="tcc_law.list4cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'민식이법 기소' 50대에 무죄…'0.3초'가 처벌 갈랐다</strong>
						<p class="desc">어린이보호구역(스쿨존)에서 발생한 어린이 교통사고 처벌 규정을 강화한 &#x27;민식이법&#x27;(특정범죄가중처벌 등에 관한 법률상 어린이치상)으로 기소된 50대 여성 A씨에게 무죄가 선고됐습니다.A씨는 지난 4월 승용차량을 몰고 전주의 한 스쿨존을 지나다 B양을 치어 다치게 한 혐의를 받아 재판에 넘겨졌습니다. B양은 이 사고로 발목을 다쳤고 전치 8주의 진단을 받았습니</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-4" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="3"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_99926b39-14c3-11eb-9673-45b3ada2ea93" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222121036638" class="theme_thumb" data-clk="tcc_law.list5cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19430049065061430PPoQe.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;학폭 가해자가 경찰되는 것은 막아주세요&quot;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222121036638" class="theme_info" data-clk="tcc_law.list5cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"학폭 가해자가 경찰되는 것은 막아주세요"</strong>
						<p class="desc">지난 8일 &#x27;학교폭력 범죄자가 경찰이 되는 것을 막아주세요!&#x27;라는 제목의 국민청원이 올라왔습니다. 해당 글은 현재 중앙경찰학교에서 교육을 받고 있는 A 씨가 학교폭력 가해자라는 내용이 담겨있습니다. ​청원인은 과거 피해 사실을 구체적으로 언급했습니다. 교육생 A 씨는 급소, 명치, 뺨, 머리 등 신체 부위를 때리거나 라이터를 가까이 대며 위협하는 등 폭행.</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_a09499ad-1404-11eb-b67a-3f81ca28ebc6" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29620726&amp;memberNo&#x3D;36765180&amp;searchRank&#x3D;25" class="theme_thumb" data-clk="tcc_law.list5cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19348144806243853cCQWb.jpg%22&amp;type&#x3D;nf340_228" alt="빚 수렁에 빠진 20대... 신용위험 &#x27;빨간불&#x27;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29620726&amp;memberNo&#x3D;36765180&amp;searchRank&#x3D;25" class="theme_info" data-clk="tcc_law.list5cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">빚 수렁에 빠진 20대... 신용위험 '빨간불'</strong>
						<p class="desc">최근 빚투(빚내서 투자) 열풍과 함께 빚 수렁에 빠진 20대가 급증한 것으로 나타났다. 이들은 자산을 늘리기 위해 빚투를 통해 마이너스통장을 개설하는 수가 늘면서 대출 연체율이 높아짐과 동시에 개인회생으로까지 연결되는 악순환이 이어지고 있다. 경기 침체로 인한 20대의 위기감이 기존 세대의 자산 증식법을 답습하며 신용위험도를 높이고 있다는 분</p>
						<div class="source_box">
							<span class="date">2주일 전</span>
							<span class="source"><span class="source_inner">업다운뉴스</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_99926b38-14c3-11eb-9673-cb4fa8e8c886" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29769329&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list5cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19429956586275942W3Unh.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;룸살롱 접대&#x27; 주장에 술렁…법으로 허용되는 접대 범위는?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29769329&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list5cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'룸살롱 접대' 주장에 술렁…법으로 허용되는 접대 범위는?</strong>
						<p class="desc">정치권과 법조계가 유흥업소 출입과 접대비 등으로 술렁이고 있습니다. 사실 접대비는 그 자체로 문제가 되는 건 아닙니다. 세법에도 등장할 정도니 접대비는 법적으로도 어느 정도는 인정된 내용으로 볼 수 있습니다. 법인세법에도 접대비의 손금불산입 규정을 두고 있습니다. 그러므로 접대비 자체는 불법이 아닙니다. 문제는 선을 지키느냐입니다. 언제나 그렇듯 선을 넘는</p>
						<div class="source_box">
							<span class="date">2일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_6f2695cf-13ff-11eb-9673-c383a3c077ba" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29528917&amp;memberNo&#x3D;45855057" class="theme_thumb" data-clk="tcc_law.list5cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19345957159125586VekMr.jpg%22&amp;type&#x3D;nf340_228" alt="알아두면 좋은 계약해제의 3가지 종류" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29528917&amp;memberNo&#x3D;45855057" class="theme_info" data-clk="tcc_law.list5cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">알아두면 좋은 계약해제의 3가지 종류</strong>
						<p class="desc">얼마 전, 부동산을 매수한 의뢰인으로부터 다음과 같은 이유로 상담연락이 왔습니다. 매수인은 잔금 지급일에 잔금을 지급하지 못하였고, 매도인은 이를 이유로 잔금지급기일 다음 날 매수인에게 ‘계약금을 포기하고 매매계약을 해제할 것’을 요청하였는데요. 계약금을 교부한 이유로 한 해제(약정해제)와 법정해제를 착각한 것이 아닌지 </p>
						<div class="source_box">
							<span class="date">1개월 전</span>
							<span class="source"><span class="source_inner">생활법률연구회</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_2b20cc12-13ff-11eb-9673-6d17cdfa292f" data-da-position="true">
					<a href="https://blog.naver.com/polinlove2/222119711323" class="theme_thumb" data-clk="tcc_law.list5cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19345857484700104cfH9n.jpg%22&amp;type&#x3D;nf340_228" alt="익산 약촌 오거리 택시기사 살인사건, 그날의 진실" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/polinlove2/222119711323" class="theme_info" data-clk="tcc_law.list5cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">익산 약촌 오거리 택시기사 살인사건, 그날의 진실</strong>
						<p class="desc">안녕하세요 경찰청 블로그 구독자 여러분! 오늘은 국내 장기미제 해결사건 중 ‘익산 약촌 오거리 택시기사 살인사건’에 대해 이야기해보려 합니다.​​익산 약촌 오거리 택시기사 살인사건은 잘못된 수사로 인해 범행과 무관한 사람이 무려 10년간 억울하게 옥살이를 했던 사건인데요. 이 사건은 재심, 무죄 판결, 진범 재판 등 18년이라는 시간을 거쳐 진실을 되찾게 </p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">대한민국 경찰청</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-5" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="3"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_850d6408-11d7-11eb-82bf-f548fd6a4244" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29766719&amp;memberNo&#x3D;5011620" class="theme_thumb" data-clk="tcc_law.list6cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1024%2Fupload_19435582001857474PvIMZ.jpg%22&amp;type&#x3D;nf340_228" alt="해커에게 고객 개인정보 털린 통신사, 배상책임 있을까요?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29766719&amp;memberNo&#x3D;5011620" class="theme_info" data-clk="tcc_law.list6cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">해커에게 고객 개인정보 털린 통신사, 배상책임 있을까요?</strong>
						<p class="desc">통신사는 개인정보 유출에 책임져야 할까요?최해커씨는 2012년 자신이 개발한 해킹프로그램을 이용하여 인증서버를 우회하는 방식으로 A통신사의 고객정보 데이터베이스에 침입해 고객정보를 취득·유출했습니다. 이 사건으로 개인정보가 유출된 피해자들은 A통신사를 상대로 이 정보유출사고로 인해 개인정보통제에 관한 인격권이 침해되었다고 주장하면서, 위자료를 </p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">법제처</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_a09499ac-1404-11eb-b67a-4bf97dd16455" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29707631&amp;memberNo&#x3D;45987910&amp;navigationType&#x3D;push" class="theme_thumb" data-clk="tcc_law.list6cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19348134275416278DH29v.jpg%22&amp;type&#x3D;nf340_228" alt="요즘 유행이라는 &#x27;빚투&#x27;, 신용점수 영향 없나?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29707631&amp;memberNo&#x3D;45987910&amp;navigationType&#x3D;push" class="theme_info" data-clk="tcc_law.list6cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">요즘 유행이라는 '빚투', 신용점수 영향 없나?</strong>
						<p class="desc">올해 3~4월은 아무도 몰랐던 코로나19로 인해 경제가 침체되면서 주식 시장 또한 폭락했다. 그러나 유동 자본의 공급이 몰리면서 증시가 다시 호황기를 누리고 있다. 특히 빚을 내어 많은 사람들이 주식에 뛰어들어 이로 인해 빚을 내 투자한 규모가 16조 5,555억 원이다. 올해 3월 신용공여잔고는 6조 원에 불과했지만 반 년 만에 신용공여잔고가 두 배 넘게</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">올크레딧</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_df0ff368-13fd-11eb-9673-d1e653d381a5" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222120056526" class="theme_thumb" data-clk="tcc_law.list6cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19344943789437990efvvy.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;무한리필은 공짜?&quot; 양파거지 이어 이번엔 &#x27;코스트코 콜라거지&#x27; 논란" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222120056526" class="theme_info" data-clk="tcc_law.list6cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"무한리필은 공짜?" 양파거지 이어 이번엔 '코스트코 콜라거지' 논란</strong>
						<p class="desc">한 온라인 커뮤니티에 올라온 &#x27;코스트코 음료거지&#x27; 사연에 네티즌들의 갑론을박이 이어지고 있습니다. ​ 미국계 창고형 할인매장인 코스트코는 음료값을 지불하면 종이컵을 제공하고 무제한으로 음료를 마실 수 있도록 하고 있습니다. 그런데 음료값을 내지 않은 것으로 보이는 고객이 개인이 소지한 보온병에 음료를 채워가 논란이 되고 있는 건데요. ​글쓴이에 따...</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_df0ff366-13fd-11eb-9673-67beee984455" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29760671&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list6cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_193450889597229732reS8.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;혼자 사는 여성 택배에 몹쓸짓&#x27; 서대문 변태남 한 짓 보니" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29760671&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list6cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'혼자 사는 여성 택배에 몹쓸짓' 서대문 변태남 한 짓 보니</strong>
						<p class="desc">/사진&#x3D;게티이미지뱅크 혼자 사는 여성의 원룸에 도착한 택배를 가져가 몹쓸 짓을 한 뒤 다시 갖다 놓은 이른바 &#x27;서대문 변태남&#x27;이 경찰에 붙잡혔습니다.서대문경찰서에 따르면 20대 남성 A씨는 피해여성의 집 앞에 놓인 택배를 가져가 몹쓸 짓을 하는 변태행각을 이어왔는데요. A씨는 피해여성이 같은 건물에 거주한다는 점을 악용해 이 같은 범행을 저질렀습니다</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_df0ff365-13fd-11eb-9673-8b5d04ae1a34" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29760058&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list6cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19345107605808405naQeL.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;민식이법 기소&#x27; 50대에 무죄…&#x27;0.3초&#x27;가 처벌 갈랐다" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29760058&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list6cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'민식이법 기소' 50대에 무죄…'0.3초'가 처벌 갈랐다</strong>
						<p class="desc">어린이보호구역(스쿨존)에서 발생한 어린이 교통사고 처벌 규정을 강화한 &#x27;민식이법&#x27;(특정범죄가중처벌 등에 관한 법률상 어린이치상)으로 기소된 50대 여성 A씨에게 무죄가 선고됐습니다.A씨는 지난 4월 승용차량을 몰고 전주의 한 스쿨존을 지나다 B양을 치어 다치게 한 혐의를 받아 재판에 넘겨졌습니다. B양은 이 사고로 발목을 다쳤고 전치 8주의 진단을 받았습니</p>
						<div class="source_box">
							<span class="date">3일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-6" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="4"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_df0ff369-13fd-11eb-9673-7945b6261db4" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?memberNo&#x3D;38212397&amp;volumeNo&#x3D;29740689" class="theme_thumb" data-clk="tcc_law.list7cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19345209934517449R4cGp.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;아기 팔아요&quot; 충격의 아기 판매글, &#x27;연락두절&#x27; 아기 아빠의 법적 책임은?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?memberNo&#x3D;38212397&amp;volumeNo&#x3D;29740689" class="theme_info" data-clk="tcc_law.list7cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"아기 팔아요" 충격의 아기 판매글, '연락두절' 아기 아빠의 법적 책임은?</strong>
						<p class="desc">20대 미혼모가 중고물품을 거래하는 애플리케이션(앱) &#x27;당근마켓&#x27;에 아기를 입양시킨다는 충격적인 글이 올라와 논란이 계속되고 있습니다. 제주도에 거주하는 20대 여성 A씨는 지난 16일 &#x27;아이 입양합니다 36주 되어있어요&#x27;라는 제목의 글을 당근마켓에 올렸습니다. 아이 사진 2장을 첨부하며 입양 가격으로 20만원을 책정하기도 했습니다. 게시물은</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_06b85eb9-1366-11eb-9673-e5d51cd650a6" data-da-position="true">
					<a href="https://blog.naver.com/ntscafe/222117126047" class="theme_thumb" data-clk="tcc_law.list7cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_192800350430330311VSXU.jpg%22&amp;type&#x3D;nf340_228" alt="세무사가 알려주는 종부세 절약 &#x27;꿀팁&#x27;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/ntscafe/222117126047" class="theme_info" data-clk="tcc_law.list7cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">세무사가 알려주는 종부세 절약 '꿀팁'</strong>
						<p class="desc">서울에 아파트를 보유하고 있는 장 씨는 최근 상승한 기준시가 때문에 종합부동산세(이하 ‘종부세’라고 한다)가 걱정입니다. 종부세는 어떤 경우에 얼마 정도를 내야 하는지, 임대주택으로 등록한 주택은 종부세를 안내도 된다고 들었는데 사실인지, 단독명의로 할 때와 부부 공동명의 중에 무엇이 유리한지 궁금합니다.6월 1일 현재, 인별로 기준시가 6억 원을 초과하는</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">국세청</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_9dd0aa77-133e-11eb-a746-e36deb9a8806" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29701321&amp;memberNo&#x3D;45335898&amp;searchRank&#x3D;200" class="theme_thumb" data-clk="tcc_law.list7cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19263088113517950mu3Rw.jpg%22&amp;type&#x3D;nf340_228" alt="살던 집 경매 넘어가 보증금 떼먹힌 세입자 무려…" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29701321&amp;memberNo&#x3D;45335898&amp;searchRank&#x3D;200" class="theme_info" data-clk="tcc_law.list7cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">살던 집 경매 넘어가 보증금 떼먹힌 세입자 무려…</strong>
						<p class="desc">최근 5년간 거주하던 주택이 경매로 넘어가면서 전세보증금을 돌려받지 못한 임차인(세입자)이 1만 4천명 가까이에 달하는 것으로 나타났다. 이들이 못 받은 금액만 4천500억원을 넘었다. 14일 국회 국토교통위원회 소속 박상혁 더불어민주당 의원이 대법원으로부터 제출받은 자료에 따르면 2015년부터 2020년 7월까지 주택이 경매로 넘어가면서 세</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">비즈엠</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_9dd0aa76-133e-11eb-a746-858168a1a3fc" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29637077&amp;memberNo&#x3D;11292208&amp;searchRank&#x3D;145" class="theme_thumb" data-clk="tcc_law.list7cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_192630824986363450qzAN.jpg%22&amp;type&#x3D;nf340_228" alt="토지 &#x27;열탕&#x27; 상가 &#x27;냉탕&#x27;, 요즘 경매 트렌드" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29637077&amp;memberNo&#x3D;11292208&amp;searchRank&#x3D;145" class="theme_info" data-clk="tcc_law.list7cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">토지 '열탕' 상가 '냉탕', 요즘 경매 트렌드</strong>
						<p class="desc">우주성 기자 | wjs89@econovill.com [이코노믹리뷰&#x3D;우주성 기자] 신종 코로나바이러스 감염증(코로나19)로 인한 사회적 거리두기 상향으로 전국 법원 경매가 다시 한 번 멈춰 섰다. 경매 절차는 현재 다시 정상화됐지만, 경매 시장 역시 소강상태에 빠졌다. 그러나 경기권 아파트와 토지 물건을 중심으로 시장은 빠르게 회복세를 보이는 </p>
						<div class="source_box">
							<span class="date">2주일 전</span>
							<span class="source"><span class="source_inner">이코노믹리뷰</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_6f2695ce-13ff-11eb-9673-ed89debe181b" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29699532&amp;memberNo&#x3D;45855057" class="theme_thumb" data-clk="tcc_law.list7cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1023%2Fupload_19345911343556473xqTaw.jpg%22&amp;type&#x3D;nf340_228" alt="범죄피해자는 어떤 보호를 받을 수 있나요 ?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29699532&amp;memberNo&#x3D;45855057" class="theme_info" data-clk="tcc_law.list7cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">범죄피해자는 어떤 보호를 받을 수 있나요 ?</strong>
						<p class="desc">상담을 진행하다 보면 법적 절차의 진행에 따른 각종 보복을 두려워하는 의뢰인들을 종종 보게 됩니다. 이런 분들이 법정 진술이나 고소 ․ 고발 등을 이유로 그 상대방으로부터 예상되는 위해로부터 보호받을 수 있는 법적인 방법은 무엇이 있을까요? 오늘 범죄피해자 보호 ․ 지원 제도에 대하여 살펴보도록 하겠습니다. 1. 보복범죄 가중처벌 먼저, 특정범죄 가중처벌 </p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">생활법률연구회</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-7" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="4"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_06b85eb8-1366-11eb-9673-2dcd4712af56" data-da-position="true">
					<a href="https://blog.naver.com/ntscafe/222121151933" class="theme_thumb" data-clk="tcc_law.list8cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19279834107598281tk0Nm.jpg%22&amp;type&#x3D;nf340_228" alt="종업원이 받은 팁, 세금은 업주가 낸다?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/ntscafe/222121151933" class="theme_info" data-clk="tcc_law.list8cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">종업원이 받은 팁, 세금은 업주가 낸다?</strong>
						<p class="desc">관할 세무서로부터 세무조사를 받고 1,500만 원의 세금을 추징당했습니다. 추징세액을 살펴보니 종업원에게 지급한 봉사료 1억 원에 대한 부가가치세 900만 원이 포함되어 있었죠. 이것은 A씨의 실제 수입이 아님에도 불구하고 A씨가 영수증을 발행할 때 음식 가격과 봉사료를 구분해 표시하지 않아서 A씨에게 추징된 것입니다. 봉사료 처리는 어떻게 해야 하는 걸까</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">국세청</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_daf60599-1336-11eb-83df-970c9395588b" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29750843&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list8cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19259575427956912jlleM.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;통장엔 100만원뿐&quot; 성폭행 고소인 배상 못한다는 박유천" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29750843&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list8cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"통장엔 100만원뿐" 성폭행 고소인 배상 못한다는 박유천</strong>
						<p class="desc">/사진&#x3D;머니투데이 가수 겸 배우 박유천이 자신을 성폭행 혐의로 고소했던 A씨에게 5000만원을 배상하라는 법원의 결정을 1년 넘게 따르지 않고 있습니다. 지난 2016년 A씨를 비롯한 여성 3인은 박유천을 성폭행 혐의로 고소했으나 무혐의 판결이 났습니다. 이에 박유천은 역으로 A씨를 무고 및 출판물에 의한 명예훼손 혐의로 고소했지만 A씨에게 무죄 판</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_daf6059c-1336-11eb-83df-2f698ae92f58" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29713717&amp;memberNo&#x3D;36310338" class="theme_thumb" data-clk="tcc_law.list8cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_192597132278199772WYWz.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;예쁘다고 좋아했는데&#x27; 핑크뮬리의 충격적인 실체" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29713717&amp;memberNo&#x3D;36310338" class="theme_info" data-clk="tcc_law.list8cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'예쁘다고 좋아했는데' 핑크뮬리의 충격적인 실체</strong>
						<p class="desc">&#x27;거리두기 완화&#x27; 여행 가볼까?,10월말 여행주간 시행 검토      문체부 내부 검토 통해 예정대로 &#x27;안전&#x27; 방점에 둔 가을 여행주간 시행 가닥…&quot;방역당국과 최종 협의 후 결정&quot;기사 자세히▶     [단독]&#x27;거리두기 완화&#x27; 가을여행 가볼까…10월말 여행주간 시행 검토 - 머니투데이 news.mt.co.kr</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">머니투데이</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_daf6059a-1336-11eb-83df-c75ac42b091c" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29750530&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list8cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19259773303615235YrHrP.jpg%22&amp;type&#x3D;nf340_228" alt="아내 몰래 빅히트에 1억 투자한 남편의 고민 &quot;이혼사유되나요?&quot;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29750530&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list8cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">아내 몰래 빅히트에 1억 투자한 남편의 고민 "이혼사유되나요?"</strong>
						<p class="desc">올해 기업공개(IPO) 최대어로 꼽히던 &#x27;빅히트 엔터테인먼트&#x27;가 개미들의 무덤이란 불명예를 안고야 말았습니다. 상장 이후 거듭된 주가 하락 때문인데요. 방탄소년단(BTS)의 소속사로 더 유명한 빅히트는 지난 15일 코스피 시장에서 첫 거래를 시작했습니다. 공모가(13만5000원)의 2배인 27만원에 시초가가 형성되는 이른바 &#x27;따상&#x27;을 기록할 때만 해도 분위</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_daf6059d-1336-11eb-83df-873b3c7600f9" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29742470&amp;memberNo&#x3D;12282441" class="theme_thumb" data-clk="tcc_law.list8cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19259785090638934ipS0D.jpg%22&amp;type&#x3D;nf340_228" alt="두 아들 둔 가장인데… 1㎞ 끌려간 경찰관 ‘의식불명’" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29742470&amp;memberNo&#x3D;12282441" class="theme_info" data-clk="tcc_law.list8cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">두 아들 둔 가장인데… 1㎞ 끌려간 경찰관 ‘의식불명’</strong>
						<p class="desc">음주측정 거부 차량에 매달린 채 끌려가 도로에 떨어진 경찰관이 의식불명에 빠진 사실이 뒤늦게 밝혀졌다. 19일 경찰에 따르면 부산 동래경찰서 사직지구대 A경위(55)는 지난 6월 19일 0시46분쯤 동래구 한 도로에서 음주운전 의심 차량을 발견하고 운전자 B씨를 상대로 음주측정을 시도했다. 그러나 B씨는 이를 거부하고 도주하기 시작했고 A경위</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">국민일보</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-8" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="5"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_daf6059b-1336-11eb-83df-213aacd5c2da" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222121009192" class="theme_thumb" data-clk="tcc_law.list9cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_19259782578598652fyZbQ.jpg%22&amp;type&#x3D;nf340_228" alt="하늘에서 쏟아져내린 5만원권 지폐 120장, 주우면 임자?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222121009192" class="theme_info" data-clk="tcc_law.list9cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">하늘에서 쏟아져내린 5만원권 지폐 120장, 주우면 임자?</strong>
						<p class="desc">지난 19일 낮, 서울 서대문구의 한 아파트 단지에서 말 그대로 하늘에서 5만원권 지폐가 쏟아져내리는 행복한(?) 상황이 연출됐습니다. 이날 하늘에서 떨어진 지폐는 5만원권 총 120장이었는데요. 전체 600만원의 적지 않은 금액입니다. ​ 놀란 주민들의 신고로 경찰이 출동해 지폐를 수거하는 소동이 빚어졌습니다. 알고 보니 이 황당한 상황은 이 아파트에 거</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_3ae7f8cc-1270-11eb-82bf-b5c7e132518a" data-da-position="true">
					<a href="https://blog.naver.com/loveacrc/222110294810" class="theme_thumb" data-clk="tcc_law.list9cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1021%2Fupload_19174419551100418MG6cy.jpg%22&amp;type&#x3D;nf340_228" alt="통장·이장 자녀에 대학등록금까지 준다고?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/loveacrc/222110294810" class="theme_info" data-clk="tcc_law.list9cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">통장·이장 자녀에 대학등록금까지 준다고?</strong>
						<p class="desc">통장·이장 자녀 장학금 제도를 아시나요?​​통장·이장 자녀 장학금은 지역인재를 양성하기 위해 만들어진 제도입니다. 그러나! 장학금 지급기준, 대상, 절차, 부적절한 신청서류 항목 등과 관련하여 꾸준히 문제가 발생하고 있었습니다. 그동안의 문제점들과 국민권익위원회 제도개선으로 바뀌는 통장·이장 자녀 장학금 제도를 청백리포터 카드뉴스와 함께 살펴보아요~​​​​</p>
						<div class="source_box">
							<span class="date">2주일 전</span>
							<span class="source"><span class="source_inner">국민권익위원회</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_27db1e9c-1274-11eb-82bf-4386d1dd1242" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29641995&amp;memberNo&#x3D;16296850&amp;navigationType&#x3D;push" class="theme_thumb" data-clk="tcc_law.list9cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1021%2Fupload_19176093720300260jCP7b.jpg%22&amp;type&#x3D;nf340_228" alt="집 팔 계획이라면 &#x27;이 세금&#x27;부터 확인!" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29641995&amp;memberNo&#x3D;16296850&amp;navigationType&#x3D;push" class="theme_info" data-clk="tcc_law.list9cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">집 팔 계획이라면 '이 세금'부터 확인!</strong>
						<p class="desc">제네시스박의 친절한 부동산 절세 #102‘절세의 꽃&#x27;이라 불리는 양도소득세, 세액 자체도 클 뿐더러 이에 따라 투자수익률이 결정나기에 더욱 그러할 것입니다. 여기에 양도소득세 세부담이 급격히 늘어나는 ‘양도세 중과’가 실행중이고 이 역시 내년에 더욱 강화된다고 하니 이에 대해 잘 아셔야겠죠? 이번 칼럼에서는 내년(21</p>
						<div class="source_box">
							<span class="date">2주일 전</span>
							<span class="source"><span class="source_inner">직방</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_3ae7f8cb-1270-11eb-82bf-558585cd1278" data-da-position="true">
					<a href="https://blog.naver.com/loveacrc/222120194756" class="theme_thumb" data-clk="tcc_law.list9cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1021%2Fupload_191743782411520205p4pR.jpg%22&amp;type&#x3D;nf340_228" alt="“민원인이 고맙다며 밥 샀는데...” 징계받은 공무원들" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/loveacrc/222120194756" class="theme_info" data-clk="tcc_law.list9cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">“민원인이 고맙다며 밥 샀는데...” 징계받은 공무원들</strong>
						<p class="desc">2017년 법원은 공무원에게 식사를 접대한 A회의 사무국장 나태한(가명)씨에게 과태료 20만원을 선고했습니다. 그런데 접대를 받은 공무원 2명에게는 “과태료에 처하지 아니한다”고 결정합니다. ​접대를 받은 쪽이나, 접대를 한 쪽 모두 「부정청탁 및 금품등 수수의 금지에 관한 법률」 위반인데…. 법원은 왜 이런 결정을 내렸을까요? 접대받은 공무원들은 정말 무</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">국민권익위원회</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_3f1f3071-1342-11eb-83df-d78aa16600ae" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222121916845" class="theme_thumb" data-clk="tcc_law.list9cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1022%2Fupload_192646715581348909gjmA.jpg%22&amp;type&#x3D;nf340_228" alt="이재용 &#x27;경영권승계 의혹&#x27; 열쇠, 대법원이 4년째 들고있다" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222121916845" class="theme_info" data-clk="tcc_law.list9cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">이재용 '경영권승계 의혹' 열쇠, 대법원이 4년째 들고있다</strong>
						<p class="desc">삼성물산 합병비율 1:0.35가 정당했느냐를 가를 수 있는 열쇠는 이미 대법원이 갖고 있다. 일성신약이 삼성물산을 상대로 제기한 주식매수가격 결정 사건이 그것이다. 합병 성사 직후 제기돼 2016년 5월 2심 결정까지 나왔다. 이후 4년 넘게 대법원에 걸려있는 상황이다.​&#x27;삼성 합병비율&#x27;에 배신감…법적 분쟁 비화​일성신약은 합병 전 옛 삼성물산 지분을 2.</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-9" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="5"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_27db1e9b-1274-11eb-82bf-2f16a4944b54" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29723678&amp;memberNo&#x3D;4795084&amp;searchKeyword&#x3D;%EC%A0%88%EC%84%B8&amp;searchRank&#x3D;15" class="theme_thumb" data-clk="tcc_law.list10cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1021%2Fupload_19176069295486384MFUsg.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;단독명의 VS 공동명의&#x27; 종합부동산세 아끼려면?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29723678&amp;memberNo&#x3D;4795084&amp;searchKeyword&#x3D;%EC%A0%88%EC%84%B8&amp;searchRank&#x3D;15" class="theme_info" data-clk="tcc_law.list10cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'단독명의 VS 공동명의' 종합부동산세 아끼려면?</strong>
						<p class="desc">서울에 아파트를 보유하고 있는 장 씨는 최근 상승한 기준시가 때문에 종합부동산세(이하 ‘종부세’라고 한다)가 걱정입니다. 종부세는 어떤 경우에 얼마 정도를 내야 하는지, 임대주택으로 등록한 주택은 종부세를 안내도 된다고 들었는데 사실인지, 단독명의로 할 때와 부부 공동명의 중에 무엇이 유리한지 궁금합니다.6월 1일 현재,</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">국세청</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_3943b34e-126f-11eb-82e3-054b81781263" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29739655&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list10cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19104415807977152uVo95.jpg%22&amp;type&#x3D;nf340_228" alt="이혼소송 중 아이 강제로 데려간 아빠, 처벌은?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29739655&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list10cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">이혼소송 중 아이 강제로 데려간 아빠, 처벌은?</strong>
						<p class="desc">이혼 소송중인 40대 남성이 처가에서 아이들을 몸싸움 끝에 데려와 재판을 받았습니다. 법원서 선처에 해당하는 판결을 받긴 했지만, 이런 경우 형사 처벌까지 이뤄질 수 있다고 합니다. 친아빠라고 해도 이혼 소송 중이라면 조심해야 하는 부분이 어떤 것인지 알아봅니다. 부부 사이인 A씨와 아내 B씨는 시집 때문에 사이가 트러졌습니다. 급기야 B씨는 아이들을 데리</p>
						<div class="source_box">
							<span class="date">4일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_b294b248-11a4-11eb-82bf-df57e265bc98" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29740689&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list10cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19108167893968398e6jF9.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;아기 팔아요&quot; 충격의 판매글, &#x27;연락두절&#x27; 아빠의 책임은?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29740689&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list10cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"아기 팔아요" 충격의 판매글, '연락두절' 아빠의 책임은?</strong>
						<p class="desc">/사진&#x3D;뉴스1 20대 미혼모가 중고물품을 거래하는 애플리케이션(앱) &#x27;당근마켓&#x27;에 아기를 입양시킨다는 충격적인 글이 올라와 논란이 계속되고 있습니다. 제주도에 거주하는 20대 여성 A씨는 지난 16일 &#x27;아이 입양합니다 36주 되어있어요&#x27;라는 제목의 글을 당근마켓에 올렸습니다. 아이 사진 2장을 첨부하며 입양 가격으로 20만원을 책정하기도 했습니다. </p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_08679770-11a3-11eb-82bf-67bf1b2ba49a" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29682487&amp;memberNo&#x3D;45478542&amp;searchRank&#x3D;24" class="theme_thumb" data-clk="tcc_law.list10cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19086263445964713bwBu9.jpg%22&amp;type&#x3D;nf340_228" alt="복잡한 재혼가정 상속순위 어떻게 따질까" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29682487&amp;memberNo&#x3D;45478542&amp;searchRank&#x3D;24" class="theme_info" data-clk="tcc_law.list10cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">복잡한 재혼가정 상속순위 어떻게 따질까</strong>
						<p class="desc">재혼가정 예전에는 이혼이 흠이 되던 시절이 있었습니다. 그러다 보니 이혼을 해도 감추기 급급했는데요. 이제는 이혼이 흠이 되는 시대가 아닌 자신의 권리를 찾기 위해서는 이혼이 필요한 경우도 있다는 생각으로 인식이 바뀌면서 불합리한 부부생활을 할 때에 이혼을 선택하는 가정이 늘어나고 있습니다. 이와 더불어 함께 늘어난 가정, 바로 재혼가정입니다. 재혼가정 역</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">김수진변호사</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_f1a742a4-0f6b-11eb-82e3-0f798f9f2070" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222117364567" class="theme_thumb" data-clk="tcc_law.list10cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1017%2Fupload_188470521317807950FhBs.jpg%22&amp;type&#x3D;nf340_228" alt="주운 카드 쓰면 &#x27;횡령·사기죄&#x27;...여자 명의 카드 남자가 쓰려다 적발" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222117364567" class="theme_info" data-clk="tcc_law.list10cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">주운 카드 쓰면 '횡령·사기죄'...여자 명의 카드 남자가 쓰려다 적발</strong>
						<p class="desc">지난 16일, 직원의 눈썰미로 신용카드를 무단 사용하려 했던 남성이 붙잡혔습니다.​거리에서 신용카드를 주운 40대 남성 A 씨는 마트에서 카드를 이용해 등산복을 구매하려 했습니다. 그러나 마트의 직원은 행색이 추레한 남성의 카드 명의자가 여성의 이름인 것을 수상히 여겨 본인의 카드가 맞느냐고 추궁했는데요. A 씨는 &#x27;내 카드가 맞다&#x27;고 우기며 직원과 실랑.</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-10" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="6"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_8e3bf4df-11a2-11eb-82e3-6b40a731b10e" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222119723518" class="theme_thumb" data-clk="tcc_law.list11cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19086126101670130q7wtM.jpg%22&amp;type&#x3D;nf340_228" alt="성폭력 사건과 ‘거짓말탐지기 검사’" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222119723518" class="theme_info" data-clk="tcc_law.list11cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">성폭력 사건과 ‘거짓말탐지기 검사’</strong>
						<p class="desc">과학수사의 한 방법인 ‘심리생리반응 검사’는 흔히 ‘거짓말탐지기 검사’라고 불리운다. 거짓말탐지기는 피검사자가 질문을 받고 대답할 때 나타나는 생리적 변화(혈압, 맥박, 호흡의 변화 등)를 기록하는 기계장치이다. 즉 거짓말탐지기 검사는 심리변화에 따른 생리적 반응을 측정하여 측정된 반응을 토대로 진술의 진위 여부를 ‘추정’하는 검사이다. 검사 결과는 ‘이 </p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_b294b24b-11a4-11eb-82bf-37f871a645eb" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29720790&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list11cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1017%2Fupload_18844872567114898DvfHg.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;진료비 1만원에 예약비 10만원&quot; 병원예약대행 괜찮은 걸까" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29720790&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list11cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"진료비 1만원에 예약비 10만원" 병원예약대행 괜찮은 걸까</strong>
						<p class="desc">/사진&#x3D;뉴시스 인기가 많아 줄을 서야만 진료가 가능한 병원에 대리접수를 해주고 최대 11만원에 달하는 접수비를 받는 대리접수업체가 있다고 해 논란이 일었습니다.대구 A병원은 이명 치료를 잘한다는 소문이 자자합니다. 당일 선착순으로 30명만 접수를 받기에 전날 또는 이른 새벽부터 줄을 서서 접수해야 합니다. 예약 없이는 진료를 받을 수 없다보니 환자에</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_0867976f-11a3-11eb-82bf-3b379d7834ae" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29713682&amp;memberNo&#x3D;4795084&amp;searchKeyword&#x3D;%EC%83%81%EC%86%8D&amp;searchRank&#x3D;2" class="theme_thumb" data-clk="tcc_law.list11cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19086242461459456TsrT3.jpg%22&amp;type&#x3D;nf340_228" alt="숨겨진 가족이 내게 상속을 했다면 세금은 얼마?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29713682&amp;memberNo&#x3D;4795084&amp;searchKeyword&#x3D;%EC%83%81%EC%86%8D&amp;searchRank&#x3D;2" class="theme_info" data-clk="tcc_law.list11cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">숨겨진 가족이 내게 상속을 했다면 세금은 얼마?</strong>
						<p class="desc">어느 날 숨겨진 가족이 나에게 상속세를 남겼다면? 이런 상상해본 적 있으신가요? 로또 1등 당첨 다음으로 꾸는 헛헛한 꿈이죠.억대 상속인이 되고 싶다!!나도 잘 모르는 누군가가 나에게 상속을 했다 치고, 상속을 받으려면 반드시 납부해야 하는 상속세 계산 방법과 상속순위, 상속비율까지… 차근차근 알아보면서 상속받아 상속세 낼 행복한 상상을 한 번</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">국세청</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_855a0f48-11a5-11eb-82bf-0da09e188d27" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222119739733" class="theme_thumb" data-clk="tcc_law.list11cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_190874073097786963u6Kx.jpg%22&amp;type&#x3D;nf340_228" alt="도박치료단체 간부가 도박에 빠져 회비 탕진…&#x27;집행유예&#x27;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222119739733" class="theme_info" data-clk="tcc_law.list11cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">도박치료단체 간부가 도박에 빠져 회비 탕진…'집행유예'</strong>
						<p class="desc">[the L][친절한 판례씨]도박치료단체 간부가 도박에 빠져 회비 수천만원을 탕진해 처벌받은 황당한 사건이 있어 소개한다.​최근 서울중앙지방법원 형사15단독 안재천 판사는 업무상횡령 등 혐의로 재판에 넘겨진 A씨(36)에 대해 징역 6개월에 집행유예 1년을 선고하고, 80시간의 사회봉사를 명령했다.​A씨는 지난해 1월1일부터 같은해 10월26일까지 도박치료</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_b294b24a-11a4-11eb-82bf-8780f98e227b" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29740528&amp;memberNo&#x3D;38212397" class="theme_thumb" data-clk="tcc_law.list11cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19107275130889412E2Ddv.jpg%22&amp;type&#x3D;nf340_228" alt="유튜브서 폭탄제조법 배웠다는 그 스토커, 영상 올린 사람도 처벌" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29740528&amp;memberNo&#x3D;38212397" class="theme_info" data-clk="tcc_law.list11cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">유튜브서 폭탄제조법 배웠다는 그 스토커, 영상 올린 사람도 처벌</strong>
						<p class="desc">/사진&#x3D;게티이미지 자신을 만나주지 않는다는 이유로 사제 폭발물을 들고 좋아하는 여성의 집을 찾아간 남성이 경찰에 붙잡혔습니다. 20대 남성 A씨는 몇년 전부터 피해 여성 B씨에게 일방적으로 교제를 요구해왔습니다. B씨가 받아주지 않자 A씨는 끝내는 직접 만든 폭발물을 가지고 B씨가 사는 아파트를 찾아갔습니다. 폭발물로 B씨를 위협하기 위한 의도로 추</p>
						<div class="source_box">
							<span class="date">5일 전</span>
							<span class="source"><span class="source_inner">네이버 법률</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>
<div class="group_theme" data-block-id="" data-block-code="PC-THEME-LAW-MOBILE-RANKING-DEFAULT-11" data-block-type="MATERIALS" data-template-code="MOBILE-RANKING-LIST"

	 data-da="container"
	 data-index=""
     data-page="6"
	 style="display:none">

	<div class="list_theme_wrap">
		<ul class="list_theme">
			
				<li class="theme_item" data-gdid="CAS_6a0f37f1-0f4e-11eb-82bf-c50839a00b9e" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222117323056" class="theme_thumb" data-clk="tcc_law.list12cont1" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19082370880223699Fj2lW.jpg%22&amp;type&#x3D;nf340_228" alt=" &quot;피투성이 사진에 무차별 태그&quot;…하니에게 무슨 일이?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222117323056" class="theme_info" data-clk="tcc_law.list12cont1" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss"> "피투성이 사진에 무차별 태그"…하니에게 무슨 일이?</strong>
						<p class="desc">EXID 출신 방송인 하니(안희연)의 소속사가 하니의 신변을 위협하는 다수의 온라인 게시물에 대해 엄정하게 법적 대응하겠다고 밝혀 시선을 모았습니다. ​하니의 소속사 써브라임 아티스트 에이전시는 최근 SNS(사회관계망서비스)에서 하니의 신변을 위협하는 게시물이 다수 발견됐고 해당 게시물의 삭제와 게시자에 대한 조치를 요청했다고 밝혔습니다. ​문제의 SNS.</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_fbd5352e-11a2-11eb-82bf-f7e4f0b44ad2" data-da-position="true">
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29715853" class="theme_thumb" data-clk="tcc_law.list12cont2" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19102650402671256ifL6h.jpg%22&amp;type&#x3D;nf340_228" alt="새로 가게를 오픈했습니다!! 그런데 영업을 못한다고요?" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://post.naver.com/viewer/postView.nhn?volumeNo&#x3D;29715853" class="theme_info" data-clk="tcc_law.list12cont2" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">새로 가게를 오픈했습니다!! 그런데 영업을 못한다고요?</strong>
						<p class="desc">[법.잘.알의 사건 노트] 5화- 새령이의 뷰티살롱미용실을 개업한 새령이, 영업신고서를 구청에 제출했는데… 신고증이 나올 때까지 영업을 시작 못한다? 행정기본법 제정으로, 행정의 사각지대를 해소합니다!행정기본법 추진배경명문화된 집행 원칙의 부재는 법치행정과 적극행정의 장애가 되고, 국민은 행정 법 집행을 예측하거나 신뢰하기 어려워 빈번한 행정 </p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">법제처</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_855a0f47-11a5-11eb-82bf-2fdde3e539ff" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222119738456" class="theme_thumb" data-clk="tcc_law.list12cont3" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19087372603194538oG9dN.jpg%22&amp;type&#x3D;nf340_228" alt="&#x27;페어플레이&#x27; 해치는 에임핵…대법 &quot;악성프로그램은 아냐&quot;" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222119738456" class="theme_info" data-clk="tcc_law.list12cont3" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">'페어플레이' 해치는 에임핵…대법 "악성프로그램은 아냐"</strong>
						<p class="desc">[theL][친절한 판례씨]FPS(1인칭 사격게임)에서 이기고 싶어하는 게이머들이 흔히 쓰는 &#x27;꼼수&#x27;는 여러가지가 있다. 그 중 하나가 자동으로 게임 내 움직임을 조작해주는 &#x27;에임핵&#x27;이다. 이 에임핵을 쓰면 총구가 상대방을 향해 자동 조준돼 사격 버튼을 누르기만 하면 무조건 명중한다.​이 에임핵은 암암리에 유료로 팔리기도 한다. 정상적인 게이머들은...</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_a8ef8e27-0f3f-11eb-a65c-35aef0a8990b" data-da-position="true">
					<a href="https://blog.naver.com/loveacrc/222119786971" class="theme_thumb" data-clk="tcc_law.list12cont4" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1020%2Fupload_19091053552917792GtmDh.jpg%22&amp;type&#x3D;nf340_228" alt="&quot;아이 낳으라더니...&quot; 14일 때문에 지원금 못받은 쌍둥이 부부 [출처] &quot;아이 낳으라더니...&quot; 14일 때문에 지원금 못받은 쌍둥이 부부" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/loveacrc/222119786971" class="theme_info" data-clk="tcc_law.list12cont4" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">"아이 낳으라더니..." 14일 때문에 지원금 못받은 쌍둥이 부부 [출처] "아이 낳으라더니..." 14일 때문에 지원금 못받은 쌍둥이 부부</strong>
						<p class="desc">저희 부부는 눈에 넣어도 아프지 않을 쌍둥이를 얻었습니다. 그런데 아가들이 예정일보다 2개월 먼저 세상에 나와 집중 치료를 받고 있어요. 얼마 전 시청에 양육비 신청을 했는데 전입신고 후 10개월이 지나지 않았다는 이유로 거절당했습니다. 하지만 아이들이 예정일에 태어났다면 10개월이 지났을 겁니다. 우리처럼 조산으로 거주기간을 채우지 못하고 출산한 경우까지</p>
						<div class="source_box">
							<span class="date">6일 전</span>
							<span class="source"><span class="source_inner">국민권익위원회</span></span>
						</div>
					</a>
				</li>
			
				<li class="theme_item" data-gdid="CAS_6a0f37f2-0f4e-11eb-82bf-6da87f871a51" data-da-position="true">
					<a href="https://blog.naver.com/naverlaw/222117339460" class="theme_thumb" data-clk="tcc_law.list12cont5" target="_blank">
						<img  data-src="https://s.pstatic.net/dthumb.phinf/?src&#x3D;%22https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fmobile%2Fedit%2F2020%2F1017%2Fupload_18844627247899468qFLt0.jpg%22&amp;type&#x3D;nf340_228" alt="한밤중 후미등 끄고 달린 &#x27;스텔스 경찰차&#x27;, 법으로 따져보면…" width="170" height="114">
						<span class="thumb_bd"></span>
					</a>
					<a href="https://blog.naver.com/naverlaw/222117339460" class="theme_info" data-clk="tcc_law.list12cont5" target="_blank">
						<em class="theme_category"> 법률</em>
						<strong class="title elss">한밤중 후미등 끄고 달린 '스텔스 경찰차', 법으로 따져보면…</strong>
						<p class="desc">최근 온라인 커뮤니티에 후미등이 꺼진 채로 야간 주행 중인 이른바 &#x27;스텔스 경찰차&#x27; 사진이 올라와 논란이 되고 있습니다. ​스텔스 차량은 야간이나 악천후 등 시야가 좋지 않은 상황에서 전조등이나 후미등을 켜지 않은 채 달리는 차량을 일컫는데요. 레이더에도 포착되지 않는 스텔스 전투기처럼 존재를 알아채기 어렵다는 의미를 담고 있습니다. ​실제 이런 스텔...</p>
						<div class="source_box">
							<span class="date">1주일 전</span>
							<span class="source"><span class="source_inner">법률N미디어</span></span>
						</div>
					</a>
				</li>
			
		</ul>
	</div>
</div>


	<p class="alert_msg" data-clk-prefix="tcc_law">법률 판의 컨텐츠는 <a href="https://blog.naver.com/naverlaw/221063633529" data-clk-suffix="corp" target="_blank">㈜법률N미디어</a>에 의해 운영·편집 됩니다.</p>



	<div class="btn_more_wrap">
		<button type="button" class="btn_more" data-clk-custom="tcc_law.more" data-next-page="2"><i class="ico_more"></i>새로운 글 더보기</button>
	</div>


	</div>
</div>
 </div> </div> <div id="NM_INT_RIGHT" class="column_right"> <div class="column_fix_wrap"> <div id="da_brand"></div> 
<div class="sc_my" style="height: 135px;">
<iframe id="minime" name="minime" data-iframe-src="/my.html" title="MY" style="position:relative;width:390px;height:135px;border:0px" frameborder="0" framespacing="0" marginheight="0" marginwidth="0" scrolling="no" vspace="0">
</iframe>
</div>

 <div id="timesquare" class="sc_timesquare"> <h2 class="blind">타임스퀘어</h2> <div class="card_wrap">
<div class="card_nav">
<a href="#" role="button" class="btn_nav btn_prev" data-clk="squ.pre"><span class="blind">이전</span></a>
<a href="#" role="button" class="btn_nav btn_next" data-clk="squ.next"><span class="blind">다음</span></a>
</div>
<div id="NM_TS_ROLLING_WRAP" style="height: 100%;">
<div>
<a href="https://search.naver.com/search.naver?sm=top_hty&amp;fbm=0&amp;ie=utf8&amp;query=%EC%BD%94%EB%A1%9C%EB%82%9819" class="card_news" data-clk="squ.line3"><i class="news_badge">이슈</i><span class="news">코로나바이러스감염증19 현황</span></a>
</div>
<div>
<a data-clk="squ.weat" href="https://weather.naver.com/today/09290139" class="card_weather ico_w06">
<div class="current_box">
<strong class="current" aria-label="현재기온">15.0°</strong><strong class="state">구름많음</strong>
</div>
<div class="degree_box">
<span class="min" aria-label="최고기온">19.0°</span><span class="max" aria-label="최저기온">4.0°</span>
</div>
<span class="location">석관동</span>
</a>
</div>
<div>
<a data-clk="squ.dust" href="https://weather.naver.com/today/09290139" class="card_air">
<ul class="list_air">
<li class="air_item">미세<strong class="state state_normal">보통</strong></li>
<li class="air_item">초미세<strong class="state state_good">좋음</strong></li>
</ul>
<span class="location">석관동</span>
</a>
</div>


</div>
</div> <!-- EMPTY --> </div>  <div id="veta_branding"> <iframe id="da_iframe_rolling" name="da_iframe_rolling" data-iframe-src="https://siape.veta.naver.com/fxshow?su=SU10601&amp;nrefreshx=0" data-veta-preview="main_rolling" title="광고" width="350" height="200" marginheight="0" marginwidth="0" scrolling="no" frameborder="0"></iframe> <span class="veta_bd_t"></span> <span class="veta_bd_b"></span> <span class="veta_bd_l"></span> <span class="veta_bd_r"></span> </div>   <div id="shopcast" class="sc_shopcast"> <iframe id="shopcast_iframe" data-iframe-src="https://castbox.shopping.naver.com/shoppingboxnew/main.nhn" title="쇼핑캐스트" width="350" height="1539" marginheight="0" marginwidth="0" scrolling="no" frameborder="0"></iframe> </div> </div> </div> <a id="NM_scroll_top_btn" href="#wrap" class="content_top"><span class="blind">TOP</span></a> <button id="NM_darkmode_btn" type="button" role="button" class="btn_theme" aria-pressed="true"  > <span class="blind">라이트 모드로 보기</span> </button> </div> <div id="footer" role="contentinfo"> <div class="footer_inner"> <div class="banner_area"> <div class="da_box_wrap">    <div id="da_public_left"> <iframe id="da_iframe_bottom_left" data-iframe-src="https://siape.veta.naver.com/fxshow?su=SU10641&amp;nrefreshx=0" title="광고" width="350" height="86" scrolling="no" frameborder="0"></iframe> </div> <div id="da_public_right"> <iframe id="da_iframe_bottom_right" data-iframe-src="https://siape.veta.naver.com/fxshow?su=SU10642&amp;nrefreshx=0" title="광고" width="350" height="86" scrolling="no" frameborder="0"></iframe> </div> <div id="veta_time2"> <iframe id="da_iframe_below" name="da_iframe_below" data-iframe-src="https://siape.veta.naver.com/fxshow?su=SU10640&amp;nrefreshx=0" data-veta-preview="main_below" width="350" height="86" scrolling="no" frameborder="0" title="광고"> </iframe> </div> </div> </div> <div class="notice_area" data-clk-prefix="ntc"> <div class="notice_box"> <h3 class="title"><a href="https://www.naver.com/NOTICE">공지사항</a> </h3> <!-- EMPTY --> </div> <a href="more.html" class="link_all" data-clk="svcmap">서비스 전체보기</a> </div> <div class="aside_area"> <div class="partner_box_wrap"> <div class="partner_box" data-clk-prefix="crt"> <h3 class="title">Creators</h3> <a href="https://www.navercorp.com/service/creators" class="link_partner" data-clk="creator">크리에이터</a> <a href="https://www.navercorp.com/service/business" class="link_partner" data-clk="smbusiness">스몰비즈니스</a> </div> <div class="partner_box" data-clk-prefix="ptn"> <h3 class="title">Partners</h3> <a href="https://business.naver.com/service.html" class="link_partner" data-clk="service">비즈니스 · 광고</a> <a href="https://sell.storefarm.naver.com/#/home/about" class="link_partner" data-clk="store">스토어 개설</a> <a href="https://smartplace.naver.com" class="link_partner" data-clk="place">지역업체 등록</a> </div> <div class="partner_box" data-clk-prefix="dvl"> <h3 class="title">Developers</h3> <a href="https://developers.naver.com" class="link_partner" data-clk="center">네이버 개발자 센터</a> <a href="https://developers.naver.com/docs/common/openapiguide/#/apilist.md" class="link_partner" data-clk="openapi">오픈 API</a> <a href="https://naver.github.io" class="link_partner" data-clk="opensource">오픈소스</a> <a href="https://d2.naver.com" class="link_partner" data-clk="d2">네이버 D2</a> <a href="http://d2startup.com" class="link_partner" data-clk="naverD2SF">네이버 D2SF</a> <a href="https://www.naverlabs.com" class="link_partner" data-clk="labs">네이버 랩스</a> </div> </div> <div class="service_box_wrap"> <div class="service_box" data-clk-prefix="wbd"> <a href="http://whale.naver.com/" class="service_logo" data-clk="bt"> <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAAC91BMVEUAAACE1dAbf6jE1Nq/z9e82drQ3OG7ytOzws+6x9QNs7MeLpQSx60QrLAfL50gMakTxKyzwc8fMacSr6yywc8fMKIdLYzJ1d4KrrW6ydMJrrUbr6QgMKW2xNEcr6W7ydUfL5cIr7XBztgMtbMeL50fMaQQzrI0tK4cLIQUvqsVvqofMKLL0eGzxM+4xtIZuKcJr7XCyNt0xsILsLW1w9AdLYZwvL8gMaoeLY6CzMceLYyxz9fI1d0JwLMeLY4KrbXFzeAgMqvN2OEIrLUGsrVIurMfLpAcLIIIsbVWs7MeLpXIzt0UvakgMqwfL5x4wcEJsLYfMagWt6k6qqoil6DV2+UdK4EeMoEfLpOzws4/s7YgMacXvqoC27QcK38B17TE1dobKW0bKnID0bTP3OACzrQcKngcLIMbKXAD07QeLYfi6uzY4+YfLpDN2+DK2d0cK3zU4eTS3+IFzLQeL5ccKnXk7O7G19wgMJ3R3uHa5ejL2t7c5unI2Nzg6esBxrMfMKPp7vEeLYrr8fMNr7X2+PkeLYzt8vQE2LTx9fYfLpPz9/gHyLMOsrUHr7UCybQLs7YKu7UIuLUFvLQGwbUIxbQGw7QcKnTZ5OfV4uUJv67e5+rd5+rl7e8Ju6z3+vvm7vDp8PHs8vPw9fbv9PUgMaj6/PwgMqwJs6kNw7AFubULtrUGtbUJvrQEv7QAwq8MrqYKuKsKtqn+/v4Osaf7/P0K1rMHq6UeqKQNqKQhNoIgSH0Vvqoie5MhWIdV3cAcsaYhhZoglJkdLXnJ7+ia5tU61rgp1rceoKIhb4whZYgcM3fj9vJw3sdJx7xtd6sXt6hCT5AvPpAfPYQbKIMcJ34fP3q+8uSy49ux0tWd2NKYzM+A48yE08t6xchdv8FP0b1zfbcSpKIgToEbJ3nE5OG12Nmn19WM5tGKk8ehqMZlxcJJuLwgtLcbvbYc2bUTtaknNpA1Q4bZ7uuzuNuP3M9p0cNfbLUKtq5IVqk8Sp8jZpxaZZrUCA9eAAAAXXRSTlMABAj99BcO6IpfLhj9hPLp5ryyq6ZzXDnd2cuYkHtzbFFOQj0yJv76+ebc29fXx8TCuJuVlIqHgX5gPS0kEvn49/f08O3t6+fj2tLR0MzGeGNfWvbz7sXBpYN4PB4CDkIdAAAFcUlEQVRo3q3TdVwTYRjA8eeI0SKgYnd3d3d362tgO7u7Y4rd3d2K4pwwQkAQJUSxu7vbPzwYg9vufe+eO/neP9vtPr/n7t53gFMobxXPVu719pu4t/LM2a4gBwioeGZP9/0U9TyrFEyHepUSeyW45+wB/8GmXetZskpkdlGbz+w+CyVDThdV+QyT0FSMyFtikiIZMnOggIvnOMWaFwS0LBkkQj/q/mL8UpVDvv2ui6V89XvF+qm1C2rnNx8u6ferq8zfGlcHWdUbD/8PtbPI7p7aC5R49Mn6TFWZ5Z2jzKNPolOVJPtD04HEhLxFh6YH5lsqWHQQ1dVBCjFW2qUJo+8Xq3BAUeputenci27Qo6u9FGpC+8dV6pUODAZDQkKCwdAFRNz+s2wMiYwbQkwi7oWVBCvOHUep9yQkTkfMIsIv+/HygKVigaPoYuMFX+InGEQXJIS4kjRBN/b5JZutAaHcxDhQ3gVD7AWrU0a9TpgPO5OqnMUOciWJA9O8jh+IYwwmAhE39gnMrwFpchByQXCjn/kvCOf1ROil7z4LgnWuVZiQ8UpFh/gTgYs3tlvzFj4AiVbYN7oSoaDL20VaQAou6drE9UpcCCUWruyeL+ZbM3UL8Yw+YrHD4n2ozgdY9X3n05g3UnHCC6R0Xvv9pfaj/ImFoN3zqbQcJOlJkugpofWfafnoSGIp4rIvg5N5iXn+0aIS7vUQ/zBfFtMyFyPJogajXOpHrIQvYprNJf0JiEkAJu8TQqwF7VnE5mTaQyaX5PvRwUQkbLeEpH1UhqRw9ZHrP3ElInf3SOkEABmJWWhfaVG9iciHywulzNWAjY6kuiSV9wklFOELpeWHAsINZ2T3+d1JcXHrLmkVITcRGMJ8hsDehCZ8rozSkINYCKTmn8QRQn8AuQElwYtYCj4vyieG6gjdy51y6kMZYkUXmmj58kP9CcOHL7PlaKElEdEFR5031wPjCNvd2fKgOKHqF6CP1AeI7j1k+PA/aSfDdsiDjESBgDm8SJIiaCuCsgH6a7xAkuLmBASFA67zzAMuanEDdAoUHvX06dNgncldLQYU763Ex6hLkebPz7TaCfIHtOyt0kMtCpRROyAc1R8GXvy1Q1Qc/htmYNQFtyHqXEH1N2eD9ioH3NyM4gHO/VSJ2IKTC7ixqgZ8m4bjDVBMTb/waFx/IwfgNUCFK1NwHACgvZoBN5EDMgGAzRJWZSyz/3ADkjfwGo1V7PYwnPoc8MovZ2Dll18cjRzgAUnsDy5hYE24NwwpPyRrNJNuOcOSZxtx7MCk2kG6JQzfRyM5Qooix2lmsjxH9qdqIEX5TTRrGR6OQcoEZlwRSp/5BC/GjEYdI+whVfltYgfX0sXgH0CgiKh/fB3D7ck4thoQqHbS2kFGP2YyUi6w0OyUpW1rGG73x3HgwIJ98AGhU0cZ/Rhkf2oNsNLGYsC2YwwvkAMcQaTZ6TQfjzK8QfazcSDCdTiRajXD++cjUOzsgaKG3tz/uZLhHq4/PT9QVTt3NtmB1QwxI3EDnIChzeNzvLMrGd7fmoriCEyVH/P9Qyx3cP2KAJITDq9iuD8SxREkdT/C6j+Yjup3A0nOTQ8zPJiIyds6gaQCDY8wvJk4HcHOGyS1XbqC4f50jNL2IMWmwlKGd3cmItjmknn92VcwvL2F6ZeqKX37bszbv98HwU5mdfNlncfw4FYf3kSpg887aqQ3T1lW/u2dPnLk8/nKLmMoW9nDVjZfyomTzjdl1BtWcAYA+zylpGY4ONYEOc5u2evMs5a1QoHU+9I4ZXKwpcU98tgDDufc1s0re9YGdZYta5A1u5dbvlpgReOdp6JHNgc7fpCtnUO20ply5UfG/wEFXaai/lOVTwAAAABJRU5ErkJggg==" alt="웨일" width="48" height="48"> </a> <div class="service_info"> <strong class="title">웨일 브라우저</strong> <a href="http://whale.naver.com/" class="dsc" data-clk="bt">다운받기</a> </div> </div> <div class="service_box" data-clk-prefix="prj"> <a href="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EA%BD%83" class="service_logo" data-clk="link"> <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF4AAABkCAMAAAA47XeXAAAAgVBMVEUAAADN5PdGm99Gm99Gm99Gm99Gm95Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gm99Gmt9Gm99Gm99Gm99Gm95Gm99Gm99Gm95Gm99Hm99Gm99Gm9/////3+/5cp+LO5PfR5/fO5fdcp+P7/f/zv5GhAAAAInRSTlMA/v7vH9u5qJNgGwb6l8a9uqF9WFUyLxYMCtbVmLCwe4OCj8gzEgAAA0NJREFUaN7NmmFz4iAQhkkwMTHGWrWtWvWuq8mF+/8/8Ey2nb0OhSwQZnw+MHQ7pbjAy2s2gsuiLPJMLpcyy4tyISZltnmHbxw3MzEVr/MUNNL5q5iCt2ccXCN9fhPB7CQYkTsRRlWDlboSAexzGCHfC28OKxhldfDOzBMwePLNTw0sauHFFphshQcLCUwkaQRfXYBPSkrEUBdv3jezcXXhw1ciUhc+fCUidQlH7qzqEk5d2dQlnHxvU5dwVgdXdSGclaiGyamt6hLO1qIu4ZASzcFE092SBprk1jagulvXAAw/qb5N7m176xQYmOPoLymYaK/X65/PNhlagE6LGUhfRM8FjNzuf/73//bHmInzoJEpjMyeWpp9RzGz/PT6+QvMNO2Q+67PPeYZY5h7jDVg5OM+/BGikd13JfDAj/Ad1WLMyEyUwKPT00ypN1GKAljQJtFiFgqRe86eYhbWIvPPPR5d+9pKiIgUwKNJdHXBvW9jyRye1EWLWYfnJcd141Byspizz7gbUyWDuqiW0v15D9g3ZgF86JwyKUgUHJaATUmS5rsEdkkTZLjZS8Alw+skFr8Nl6H6uosShaKOp3Zo+/jgFTDe+wcSfv0yFGfQaLX7tDO0reXOPRuMCG4Q11Y3IiYblWgzS7R+h31qdRtlGB7zikeUckz+AB3a8FuMqD7Cd2nhUHLOEIkLubQIkEuLxIdwEwUy3HyXxsbgPMJcGuGox+TSIugxuTQ+KHIaAS5N92eIIuMT5tJoPfHy5q9yKoXLelLuKRri0mjMQdhwTPw6Sv8pzKXhFyhNilEwkSCXRrnAnaPnJdyl0UrqXircpeHVglnv+62K4NJo3lFcGmWd79KO7OQoXAE8XNO6tIQGxj7fpfHTwk8RubQLWEGvgTNGKzj01fixunCMCCYcvSSlaFwUyKVx86J3bczpUR3zimq1LqdosAUbJF54ar+uk5Gju436mPTk8ZAXFdO93HRYTesUVgf3B+y0XdxLfdVputmfKp/iBtNjyl3c0kzUwtJIWewIPvAL9LOyWLsV9WAps3VRzh6hJBm3oOqsRKfHLGYzS/GP+iLBuBKdqkd+iWPkFZTHf4Em4us/uhI5qss/6zK5u8+AXpwAAAAASUVORK5CYII=" alt="꽃" width="47" height="50"> </a> <div class="service_info"> <strong class="title">프로젝트 꽃</strong> <a href="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EA%BD%83" class="dsc" data-clk="link">바로가기</a> </div> </div> </div> </div> <div class="corp_area" data-clk-prefix="plc"> <h3 class="blind">네이버 정책 및 약관</h3> <ul class="list_corp"> <li class="corp_item"><a href="https://www.navercorp.com" data-clk="intronhn">회사소개</a></li> <li class="corp_item"><a href="https://recruit.navercorp.com/naver/recruitMain" data-clk="recruit">인재채용</a></li> <li class="corp_item"><a href="https://www.navercorp.com/naver/proposalGuide" data-clk="contact">제휴제안</a></li> <li class="corp_item"><a href="/policy/service.html" data-clk="service">이용약관</a></li> <li class="corp_item"><a href="/policy/privacy.html" data-clk="privacy"><strong>개인정보처리방침</strong></a></li> <li class="corp_item"><a href="/policy/youthpolicy.html" data-clk="youth">청소년보호정책</a></li> <li class="corp_item"><a href="/policy/spamcheck.html" data-clk="policy">네이버 정책</a></li> <li class="corp_item"><a href="https://help.naver.com/" data-clk="helpcenter">고객센터</a></li> </ul> <address class="addr"><a href="https://www.navercorp.com" target="_blank" data-clk="nhn">ⓒ NAVER Corp.</a></address> </div> </div> </div> </div> <div id="adscript" style="display:none"></div> </body> </html>
"""
    
    
