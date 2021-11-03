import os
file_path = "/home/spark/download/release/"
file_names = os.listdir(file_path)
#print(file_names)
count = 1
for fn in file_names:
    if fn[0] != '.' :
        current_file = open(file_path+fn,"r+")
        title = current_file.readlines()
        if len(title) > 0:
            print(str(count)+':::'+fn+':'+title[0])
            count=count+1
