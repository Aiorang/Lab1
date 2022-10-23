def lab1_2(file,level):

    # 导入包
    import re

    # 导入文件
    f = open(file,'r')
    fs = f.readlines()
    s = fs
    s2 = fs
    f.close
  #testetstetst
    # 关键字字符串
    key = ['char','double','enum','float','int', 'long','short','signed','struct','union','unsigned','void', 'for','do','while',
       'break','continue','if','else','goto','switch','case','default','return','auto','extern','register','static','const',
       'sizeof','typedef','volatile']
    
    # 正则过滤
    for i in range(len(s)):
        s[i] = re.sub("[();{}:]"," ", s[i])

    # 拆分
    sp = []
    spl = [] 
    for i in range(len(s)):
        sp = s[i].split()
        for j in range(len(sp)):
            spl.append(sp[j])

    # level 1 and level 2
    total_Num = 0
    switch_Num = 0
    case_Num = 0
    case = []
    for i in range(len(spl)):
    
        if spl[i] == 'switch': 
            if(case_Num != 0):
                case.append(case_Num)
            switch_Num = switch_Num + 1
            case_Num = 0
        
        if spl[i] == 'case':
            case_Num = case_Num + 1
        
    
        for j in range(len(key)):
            if spl[i] == key[j]:        
                total_Num = total_Num + 1
            
    case.append(case_Num)


    # level 3 and level 4

    for i in range(len(s2)):
        s2[i] = s2[i].replace("else if","@")
        s2[i] = re.sub("[();{}:]"," ", s[i])

    sp2 = []
    spl2 = [] 
    for i in range(len(s2)):
        sp2 = s[i].split()
        for j in range(len(sp2)):
            spl2.append(sp2[j])

    # level3
    if_Else_num = 0
    if_Else_on = False

    for i in range(len(spl2)):
        if spl2[i] == 'if':
            if_Else_on = True
        
        if spl2[i] == '@':  
            if_Else_on = False
        
        if spl2[i] == 'else':
            if if_Else_on == True:
                if_Else_num = if_Else_num + 1
            
    # level4
    if_Elseif_else_Num = 0
    if_Elseif_else_On = False

    for i in range(len(spl2)):
        if spl2[i] == '@':
            if_Elseif_else_On = True
        if spl2[i] == 'if' or spl2[i] == 'else':
            if if_Elseif_else_On == True:
                if_Elseif_else_On = False
                if_Elseif_else_Num = if_Elseif_else_Num + 1
    
    # 输出
    if level == 1:
        print('total num:',total_Num)
        
    if level == 2:
        print('total num:',total_Num)
        print('switch num:',switch_Num)
        print('case num:',case)
        
    if level == 3:
        print('total num:',total_Num)
        print('switch num:',switch_Num)
        print('case num:',case)
        print('if-else num:',if_Else_num)
    
    if level == 4:
        print('total num:',total_Num)
        print('switch num:',switch_Num)
        print('case num:',case)
        print('if-else num:',if_Else_num)
        print('if-elseif-else num:',if_Elseif_else_Num)

lab1_2('E:/2.txt',4)
    

            

    
