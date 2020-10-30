def mf(list):
    li = list
    f = open('opensource\\textfolder\\t_parsed.txt',mode = 'wt', encoding='utf-8')
    for i in range(len(li)):
        for j in range(len(li[i])):
            f.write(li[i][j])
    f.close()


