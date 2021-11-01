#!/usr/bin/python
#encoding:utf-8
import urllib.request
import os
import time
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)
#    time.sleep(0.3)

ezloop = 5394 
while (ezloop<66631):

    url = 'https://www.gutenberg.org/cache/epub/'+str(ezloop)+'/pg'+str(ezloop)+'.txt'
    filename = url.split('/')[-1]
    print(filename)
    local = os.path.join('/ezroot/download/books/',filename)
    try:
        urllib.request.urlretrieve(url,local,Schedule)
    except(urllib.error.HTTPError):
        print("Retrieve error")
    ezloop = ezloop+1
