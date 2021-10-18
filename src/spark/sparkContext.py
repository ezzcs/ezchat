from operator import add
from pyspark import SparkContext
sc = SparkContext("local[4]","workdjoy")
lines = sc.textFile("/home/ezzcs/spark/spark-3.1.2-bin-hadoop3.2/data/bible.txt")

wc = lines.flatMap(lambda x:x.split(' ')
	).map(lambda x:(x,1)
	).reduceByKey(add)
for(word,count)in wc.collect():
	print("%s: %i"%(word,count))
