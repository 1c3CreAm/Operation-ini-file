import re


def read_ini(ini_path):
    re_str = '\[(.*)\]((\n.*=.*)*)'
    result_dic = {}
    with open(ini_path) as f:
        a = f.read()
    result_list = re.findall(re_str,a)
    for i in result_list:
        part_dic = {}
        j_list = i[1].split('\n')
        for j in range(len(j_list)):
            if j < len(j_list)-1 :
                j = j + 1
                g_list = j_list[j].split('=')
                # print(j_list[j])
                # print(g_list)
                part_dic[g_list[0]] = g_list[1]
        result_dic[i[0]] = part_dic
    return result_dic

def inquire_ini(main_name,term_name):
    dic = read_ini(ini_path)
    for i in dic:
        if re.search(main_name,i,re.IGNORECASE):
            i = re.findall(main_name,i,re.IGNORECASE)[0]
            for j in dic[i]:
                if re.search(term_name,j,re.IGNORECASE):
                    j = re.findall(term_name,j,re.IGNORECASE)[0]
                    s = dic[i][j]
    return s

def modify_ini(main_name,term_name,a):
    dic = read_ini(ini_path)
    for i in dic:
        if re.search(main_name,i,re.IGNORECASE):
            i = re.findall(main_name,i,re.IGNORECASE)[0]
            for j in dic[i]:
                if re.search(term_name,j,re.IGNORECASE):
                    j = re.findall(term_name,j,re.IGNORECASE)[0]
                    dic[i][j] = a
    return dic

def write_ini(ini_path,modify_result):
    str = ''
    for i in modify_result:
        str = str + '['+i +']'+ '\n'
        for j in modify_result[i]:
            str = str + j + '=' + modify_result[i][j] + '\n'
    with open(ini_path,'w') as f:
        f.write(str)


if __name__ == '__main__':
    a = '1'
    main_name ='EYOONETSET'
    term_name = 'SaveLog'
    ini_path = 'C:\\Users\\Wang\\Desktop\\EyooNetConfig.ini'
    # write_ini(ini_path,modify_ini(main_name,term_name,a))
    print(inquire_ini(main_name,term_name))
