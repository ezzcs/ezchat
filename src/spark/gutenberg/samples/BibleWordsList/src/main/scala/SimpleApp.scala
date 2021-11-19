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

    val data = sc.textFile("/ezroot/download/BibleWordsNum.txt")
    val c1 = data.collect
    val c2 = c1.map(x=>(x+"."))
    val c3 = c2.map(x=>(x.split(",")(1),x.split(",")(0)))
    val c4 = c3.map(x=>(('"'+x._1+'"'),x._2))
    val s1 = c4.sortBy(x=>(x._1))
    s1.foreach(println)
 

}
}
