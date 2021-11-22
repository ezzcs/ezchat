import org.apache.spark.mllib.feature.Word2Vec
import org.apache.spark.mllib.feature.Word2VecModel
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.ml.feature.{IndexToString, StringIndexer}
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.sql.SQLContext
object SimpleApp {

  def main(args: Array[String]): Unit = {

    val conf = new SparkConf()
    val sc = new SparkContext(conf)

    val data = sc.textFile("/ezroot/download/BibleWordsListClean.txt")
    val c1 = data.collect
    val r1 = sc.parallelize(c1) 
    val r2 = r1.collect 
    val r3 = r2.map(x=>(x.substring(1,x.length-1).split(","))) 
    //val r4= r5.reduce((x,y)=>(x))
    val r20=r3.map(x=>(x(0),x(1)))
    val r21 = sc.parallelize(r20)
    //val r22=r21.reduceByKey((_ + _))
    val r22=r21.reduceByKey((_ + ':'+ _))
    val r23  = r22.collect
    val s1 = r23.map(x=>(x))
    val s2 = s1.map(x=>(x._1,x._2.length))
    val s3 = s2.sortBy(x=>(x._2))
    s3.foreach(println)
 

}
}
