import java.util.{Calendar, Date}
 
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{SparkSession, functions}
import org.apache.spark.sql._
case class vl(value:String,path:String)
object SimpleApp {
    def main(args: Array[String]){
      implicit val mapEncoder = org.apache.spark.sql.Encoders.kryo[Map[String, Any]]      
      implicit val encoder=org.apache.spark.sql.Encoders.STRING
      val conf = new SparkConf().setAppName("test")
      conf.setMaster("local")
      val spark = SparkSession.builder.config(conf).getOrCreate()
      val data= spark.read.textFile("/ezroot/download/books")
      val dm = data.withColumn("path",functions.input_file_name())
      val m1 = dm.rdd.map(row=>vl(row.getString(0),row.getString(1)))
      val f1 = m1.filter(x=>((x.value.startsWith("Title:")) || (x.value.startsWith("Author:"))))
      val m2 = f1.map(x=>(x.path,x.value))
      val r1 = m2.reduceByKey((x,y)=>(x+y))
      val cc = r1.collect
      cc.foreach(println)

    }

}
