from operator import add
from pyspark import SparkContext
sc = SparkContext("local[4]","workdjoy")
lines = sc.textFile("file:/hl/users/ezzcs/data/SearchDataFile/*")

#wc = lines.flatMap(lambda x:x.split(' ')
wc = lines.flatMap(lambda x:x.split(',')
	).map(lambda x:(x,2)
                        ).reduceByKey(add)
for(word,count)in wc.collect():
	print("%s: %i"%(word,count))
