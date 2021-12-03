# ezchat since 2021.09.01
26 republish the result.
Don't wast more time in valueless proejct. 
import numpy.matlib 
import numpy as np 
print (np.matlib.empty((2,2)))

25 words position

val data = sc.textFile("/ezroot/download/BibleWordsNum.txt"
val c1 = data.collect
val c2 = c1.map(x=>(x+"."))
val c3 = c2.map(x=>(x.split(",")(1),x.split(",")(0)))

24 sequence

def test(str:String,num:Int):Int={
	var sum:Int = num+1
	var msg:String = str.replaceAll("\\p{P}(?=\\s|$)", "")
	print(sum+","+msg+"\n")
	return sum
}

var i:Int = 0
c1.foreach(x=>(x.foreach(y=>(i=test(y,i)))))

23 去标点
val books = sc.textFile("/ezroot/download/bible.txt")
val words = books.map(x=>x.split(" "))
val c1 = words.collect
c1.foreach(x=>(x.foreach(y=>(print(y.replaceAll("\\p{P}(?=\\s|$)", ""))))))
c1.foreach(x=>(x.foreach(y=>(print(y.replaceAll("\\p{P}(?=\\s|$)", "")+"\n")))))


22 filter
val fresult = data.filter(_.contains("keywords"))


21 spark map reduce 
val list: List[Int]=List(1,2,3,4,5,6)
rintln(list.map(x=>x+1).filter{x=>x>3}.reduce(_+_))



20 scala with mavn
mvn archetype:generate -DarchetypeGroupId=net.alchim31.maven -DarchetypeArtifactId=scala-archetype-simple

mvn package

spark-submit target/*****-jar-with-dependencies.jar


19 books
with spark
the gutenburg
pyspark can't work.

18 spark-nlp
v 3.3.1


17 update github token

16 hadoop cmd
hadoop dfs -mkdir 
hadoop fs -lsr 
hadoop fs -put 
hadoop fs -rm
hadoop fs -rm-r
hadoop fs -chmod
hadoop fs -chmod -rw
hadoop fs -chmod +rwxrwxrwx /ezzcs/spark

15 install hadoop

ssh-keygen -t rsa

ssh-copy-id ezzcs@s1 

14 scala spark sort
val data = sc.textFile("hdfs://localhost:6120/ezzcs/spark/test")
val data = sc.textFile("data/bible.txt")
val splitdata = data.flatMap(line=>line.split(" "))
splitdata.collect

显示
splitdata.foreach(x=>println(x))

降序
splitdata.map((_,1)).reduceByKey(_+_).sortBy(_._2,false).collect
升序
splitdata.map((_,1)).reduceByKey(_+_).sortBy(_._2).collect


13 pyspark
>>>
spark.sparkContext._conf.getAll()
sc.getConf().getAll()


12 test map reduce
scala> val list:List[Int] = List(1,2,3,4,5,7)
scala> println(list.map(x=>x+1).filter{x=>x>1}.reduce(_+_))
result 20

11
ezreport

sudo apt install libreoffice
cp /usr/share/fonts  /usr/share/fontconfig


10 spark
val bible = sc.textFile("./data/bible1.txt")

val topWordCount = bible.flatMap(str=>str.split(" ")). filter(!_.isEmpty).map(word=>(word,1)).reduceByKey(_+_).map{case (word, count) => (count, word)}.sortByKey(false)

topWordCount.take(100).foreach(x=>println(x))

random sample:
val rdd = sc.makeRDD(Array("hello1","hello2","hello3","world1","world2","world3"))
 rdd.sample(false,0.3).foreach(println)

foreach sample:
data.map(x=>{"head"+x}).foreach(println)

val dm = data.filter(x=>x.contains("Lord"))
dm.foreach(println)


9 report
soffice -invisible -headless -nofirststartwizard "-accept=socket,host=localhost,port=2002;urp;"




8 test vue-cli functions

7 vue-cli install
npm install vue-cli -g
vue init webpack ezzc
cd ezzc
npm run build
npm run dev

config/index.js
host: '172.17.0.2',
port: '8080',

6 psql login
export PGPASSWORD=mypassword


5 boot with local scripts
5-1
create /etc/rc.local
the head
#!/bin/sh

5-2
chmod +x /etc/rc.local

5-3
create /lib/systemd/system/rc-local.service

[Unit]
Description=/etc/rc.local Compatibility
Documentation=man:ywinit(8)
ConditionFileIsExecutable=/etc/rc.local

[Service]
ExecStart=/etc/rc.local start
Type=forking
TimeoutSec=0
RemainAfterExit=yes
CuessMainPID=0

[Install]
WantedBy=multi-user.target
Alias=rc-local.service

5-4 
ln -s /lib/systemd/system/rc-local.service /etc/systemd/system/rc-local.service

5-5
systemctl enable rc-local.service


4 install rabbitmq
sudo apt install -y rabbitmq-server
sudo service rabbitmq-server stop
sudo service rabbitmq-server start
sudo service rabbitmq-server restart


sudo rabbitmqctl add_user admin pwd123
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"


sudo rabbitmqctl list_users

hostname -I

web server port: 15672


3 clean project and rebuild it.

2 test it
the git push test in local server.

1 git token setup.
git remote set-url origin https://$EZ_GIT_TOKEN@github.com/ezzcs/ezchat.git
git push
git clone

