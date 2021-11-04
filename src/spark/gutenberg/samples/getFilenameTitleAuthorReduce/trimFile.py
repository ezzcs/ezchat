import os

fn = open('/home/spark/download/booksInfo.txt','r')
data = fn.readlines()
msg = set()
for line in data:
    try:
        l1 = line.split(",Title:")
        fname = l1[0].split('/')[-1]
        l2 = l1[1].split("Author:")
        ftitle = l2[0]
        fauthor = l2[1][:-2]
        print(fname+':['+ftitle+']['+fauthor+']')
    except(IndexError):
        print("error")


