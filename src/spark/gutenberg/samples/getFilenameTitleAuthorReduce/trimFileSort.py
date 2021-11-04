import os

fn = open('/home/spark/download/booksInfo.txt','r')
data = fn.readlines()
fileList = list()
bookDict = dict()
setList = set()
mergedList = list()
error = 0
for line in data:
    try:
        l1 = line.split(",Title:")
        fname = l1[0].split('/')[-1]
        l2 = l1[1].split("Author:")
        ftitle = l2[0]
        fauthor = l2[1][:-2]
        fnid = fname[3:-4]
        if(fnid!=''):
            fniid = int(fnid)
            fileList.append(fniid)
            bookDict[fniid]= ':['+ftitle+']['+fauthor+']'
    except(IndexError):
        error = error+1
setList = set(fileList)
mergedList = list(setList)
mergedList.sort()
i =0 
for bk in mergedList:
    print(str(i)+'['+str(bk)+']'+bookDict[bk])
    i = i + 1






