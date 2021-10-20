import sys
from pyspark.sql import SparkSession
def contains(str, substr):
  if substr in str:
    return True
  return False

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: CollectFemaleInfo <file> <keyword>")
    exit(-1)

  spark = SparkSession \
    .builder \
    .appName("CollectFemaleInfo") \
    .getOrCreate()

  inputPath = sys.argv[1]
  keyWord = sys.argv[2]
  result = spark.read.text(inputPath).rdd.map(lambda r: r[0])\
    .filter(lambda line: contains(line, keyWord)) \
    .map(lambda line: line.split(',')).collect() 
#    .map(lambda line: line.split(',')) \
#    .map(lambda dataArr: (dataArr[0], int(dataArr[2]))) \
#    .reduceByKey(lambda v1: v1+":::") \
#    .filter(lambda tupleVal: tupleVal[1] > 120) \
#    .collect()
#  for (k, v) in result:
#    print(k + "," + str(v))


  # 停止SparkContext
  print(result)
  spark.stop()
