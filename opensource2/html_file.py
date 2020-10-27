def html_link_file(url_list,selected_list):

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

    f = open("html_file.html",mode = "wt",encoding="utf-8")
    for i in range(len(url_list)):
        html_doc_middle +=('<a href = "'+url_list[i]+'">'+url_list[i]+"</a>"+"\n"+"<br>")

    html_doc_middle+='<h1>SELECTED URL LIST </h1><br>'

    for i in range(len(selected_list)):
        html_doc_middle +=('<a href = "'+selected_list[i]+'">'+selected_list[i]+"</a>"+"\n"+"<br>")

    s = html_doc_top + html_doc_middle + html_doc_bottom
    f.write(s)
    f.close()
    