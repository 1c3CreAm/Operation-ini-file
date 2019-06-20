import os,hashlib,sys,time

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def write_file(filepath,num):
    stack,a_list ,b_list = [],[],[]
    _output = sys.stdout
    stack.append(filepath)
    while stack != []:
        path = stack.pop()
        if os.path.isdir(path):
            for a_path in os.listdir(path):
                stack.append(path+'\\'+a_path)
        if os.path.isfile(path):
            a_list.append(path)
    for i in range(len(a_list)):
        ff = a_list[i].replace(filepath + '\\','')
        dd = GetFileMd5(a_list[i])
        b_list.append(ff+','+dd)
        # b_list.append([i.replace(filepath + '\\',''),GetFileMd5(i)])
        if num == 0:
            with open("srcmd5.txt", "a") as f:
                f.write(ff+','+dd+'\n')
        _output.write(f'\r总进度:{((i+1)/len(a_list))*100:.0f}%')
    _output.flush()
    return b_list

def contrast(srclist,targetlist):
    list1 = list(set(srclist).difference(set(targetlist)))
    list2 = list(set(targetlist).difference(set(srclist)))
    with open('result' + '.txt', 'w') as f:
        f.write("源目录比对比目录多的文件：" + '\n')
        for i in list1:
            f.write(i + '\n')
        f.write("\n\n对比目录比源目录多的文件：" + '\n')
        for i in list2:
            f.write(i + '\n')
    os.system("result.txt")

def readfile(filename):
    srclist = []
    with open(filename,'r') as f:
        srclist1 = f.readlines()
    # print(len(srclist1))
    # print(srclist1)
    for i in srclist1:
        b = i[0:-1]
        srclist.append(b)
    return srclist

print('''1.获取md5特征文件
2.对比两个目录md5
3.对比两个md5文件，先将改名为src.txt和target.txt''')
a = input("1 or 2 or 3:")
if a == '1':
    os.system("del /F srcmd5.txt")
    filepath = input("源文件夹路径：")
    write_file(filepath,0)
elif a == '2':
    srclist = readfile('srcmd5.txt')
    filepath = input("待对比文件夹路径：")
    targetlist = write_file(filepath,1)
    contrast(srclist,targetlist)
elif a == '3':
    srclist,targetlist = [],[]
    srclist = readfile('src.txt')
    targetlist = readfile('target.txt')
    contrast(srclist, targetlist)






