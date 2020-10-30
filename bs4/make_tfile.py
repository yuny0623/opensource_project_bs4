def mf(list):
    ''' 문자열 파싱 잘되어있는지 확인하려고 만든 함수. 
        일단 지금은 쓰이지 않음. '''
    li = list
    f = open('opensource\\textfolder\\t_parsed.txt',mode = 'wt', encoding='utf-8')
    for i in range(len(li)):
        for j in range(len(li[i])):
            f.write(li[i][j])
    f.close()


