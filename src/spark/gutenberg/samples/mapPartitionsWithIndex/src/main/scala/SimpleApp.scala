import org.apache.spark.{SparkConf, SparkContext}

object SimpleApp {
    def main(args: Array[String]){
      println("Hello AI")
      val conf = new SparkConf().setAppName("test")
      conf.setMaster("local")
      val sc=new SparkContext(conf)
      val data= sc.textFile("/ezroot/download/books1")
      val dm = data.mapPartitionsWithIndex(func2).collect
      dm.foreach(println)


    }

    def func2(index:Int,iter:Iterator[String]):Iterator[String]={
      iter.toList.map(x=>"[PartID:"+index+",value="+x+"]").iterator
    }
}
