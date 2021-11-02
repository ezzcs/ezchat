import java.util.{Calendar, Date}
 
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{SparkSession, functions}

object SimpleApp {
    def main(args: Array[String]){
      val conf = new SparkConf().setAppName("test")
      conf.setMaster("local")
      val spark = SparkSession.builder.config(conf).getOrCreate()
      val data= spark.read.textFile("/ezroot/download/books1")
      val dm = data.withColumn("path",functions.input_file_name())
      val cc = dm.collectAsList
      cc.forEach(println)

    }

}
