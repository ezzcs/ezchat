import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.sql.SQLContext
import org.apache.spark.ml.feature.Word2Vec


object SimpleApp {
  def main(args: Array[String]): Unit = {

    val conf = new SparkConf()
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
    import sqlContext.implicits._
    val documentDF = sqlContext.createDataFrame(Seq(
            "Hi I heard about Spark".split(" "),
            "I wish Java could use case classes".split(" "),
            "Logistic regression models are neat".split(" ")
          ).map(Tuple1.apply)).toDF("text")
  
    val word2Vec = new Word2Vec().
            setInputCol("text").
            setOutputCol("result").
            setVectorSize(3).
            setMinCount(0)


    val model = word2Vec.fit(documentDF)
    val result = model.transform(documentDF)
    result.select("result").take(3).foreach(println)
  }


}
