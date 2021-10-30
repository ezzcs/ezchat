1 scala to collect  title to  files 
val books = sc.textFile("/ezroot/download/books")
val dm = books.filter(x=>x.contains("Title"))
dm.foreach(println)
dm.saveAsTextFile('/home/spark/download/titles')


