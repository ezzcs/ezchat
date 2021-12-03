from operator import add
from pyspark import SparkContext
import json
import hashlib
import re

from operator import add
from pyspark import SparkContext
sc = SparkContext("local[4]","workdjoy")
lines = sc.textFile("file:/hl/users/ezzcs/data/SearchDataFile/*")

wc = lines.flatMap(lambda x:re.findall(r'1\d{10}',str(x))
        ).map(lambda x:(x,1)
                        ).reduceByKey(add)
for(word,count)in wc.collect():
        print("%s: %i"%(word,count))
#        print(word)
