def html_link_file(url_list,selected_list):
    '''
    메인 페이지에 걸려있는 모든 링크들을 html doc에 넣어서 링크집합을 만들어준다. 
    찾고자하는 단어를 포함하는 링크는 SELECTED URL LIST 로 분류되어 하단에 따로 표시된다. 
    내용은 image_make와 같다. 동일하게 동작한다. 다만 함수의 매개변수로 selected_list를 하나 더 받는다. 
    show_page_include_word에서 단어를 포함하는 링크의 리스트를 반환했는데, 그 반환한 값이 
    selected_list 매개변수에 들어오는 것이다. 
    '''

    html_doc_top = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <h1>ALL URL LIST</h1>
    '''
    html_doc_middle = ""
    html_doc_bottom = '''   
    </body>
    </html>'''

    f = open("bs4\\html_file_in\\html_file.html",mode = "wt",encoding="utf-8")
    for i in range(len(url_list)):
        html_doc_middle +=('<a href = "'+url_list[i]+'">'+url_list[i]+"</a>"+"\n"+"<br>")

    html_doc_middle+='<h1>SELECTED URL LIST </h1><br>'

    for i in range(len(selected_list)):
        html_doc_middle +=('<a href = "'+selected_list[i]+'">'+selected_list[i]+"</a>"+"\n"+"<br>")

    s = html_doc_top + html_doc_middle + html_doc_bottom
    f.write(s)
    f.close()
    