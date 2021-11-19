import org.apache.spark.mllib.feature.Word2Vec
import org.apache.spark.mllib.feature.Word2VecModel
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.ml.feature.{IndexToString, StringIndexer}
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.sql.SQLContext
object SimpleApp {
  def test(str:String,num:Int):Int={
        var sum:Int = num+1
        var msg:String = str.replaceAll("\\p{P}(?=\\s|$)", "")
        print(sum+","+msg+"\n")
        return sum
}

  def main(args: Array[String]): Unit = {

    val conf = new SparkConf()
    val sc = new SparkContext(conf)

    var corpus:String = "/ezroot/download/bible.txt" 
    
    val input = sc.textFile(corpus).map(line => line.split(" ")).collect
    var i:Int = 0
    input.foreach(x=>(x.foreach(y=>(i=test(y,i)))))
    

}
}
