import org.apache.spark.{SparkConf, SparkContext}
object SimpleApp {
    def main(args: Array[String]){
      val conf = new SparkConf().setAppName("test")
      conf.setMaster("local")
      val spark = new SparkContext(conf)
      val data= spark.textFile("/ezroot/download/bible.txt")
      val c1 = data.flatMap(_.split(" ")).map((_,1))
      val cc = c1.reduceByKey(_+_).sortBy(_._2,false).collect
 //     val cc = data.collect.flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect
      cc.foreach(println)

    }

}
