import org.apache.spark.{SparkConf, SparkContext}

object SimpleApp {
    def main(args: Array[String]){
      println("Hello AI")
      val conf = new SparkConf().setAppName("test")
      conf.setMaster("local")
      val sc=new SparkContext(conf)
      val data= sc.textFile("/ezroot/download/books")
      val dm = data.filter(x=>x.contains("Title"))
      dm.foreach(println)


    }
}
