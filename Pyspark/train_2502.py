from pyspark import SparkContext , SparkConf

conf = SparkConf().setAppName('Test')
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")


numbers =[1,2,3,4,5,6]
numbersRDD = sc.parallelize(numbers)
print(numbersRDD.take(3))
