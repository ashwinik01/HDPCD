training foreach

## load a file in a RDD from the file system
fileRDD = sc.textFile(file:///home/maria_dev/files/titanic.csv) # read as RDD
fileList = open("/home/maria_dev/files/titanic.csv").read().splitlines() # read as a list

## Print method 1
for i in fileRDD.collect():
  print(i)

## Pront method 2
def printer(x):
  print(x)
  
 fileRDD.foreach(printer)
 
 #Operations map, foreach
 def increasing(x): \
    z = x + 2 

    
numberslist = sc.parallelize(range(10,25))
newlist = numberslist.foreach(increasing)
newRDD = sc.parallelize(newlist)

newlist = numberslist.map(lambda x: x + 2)
newlist.foreach(printer)

############################# March 12

from pyspark import SparkConf, SparkContext

conf= SparkConf().SetAppName('local')
sc = SparkContext (conf = conf)

fileRDD = sc.textFile('file:///home/cloudera/input/OD_2017-11.csv')

  ### map
columns = fileRDD.map(lambda x: x.split(',')).map(lambda y : y[0])
columnsdate = columns.filter(lambda x:  'start_date' != x).map(lambda y: (y,1))
numbersflat = columns.flatMap(lambda number: number.split("-"))
numbersmap = columns.map(lambda number: number.split("-"))

for i in numbersflat.take(5):
	print (i)

for i in numbersmap.take(5):
	print (i)

  
  ### count
 

  

 
 
