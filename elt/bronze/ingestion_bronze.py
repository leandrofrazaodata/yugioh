from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Bronze") \
    .master("local[*]") \
    .getOrCreate()


df = spark.read.json("/home/leandro/dev/yugioh/yugioh/data/cards/*.json", multiLine=True)

df.createOrReplaceTempView("vw_cards")

spark.sql('''
          
SELECT 
    COUNT(id) AS qtd_total_id,
    COUNT(DISTINCT id) AS qtd_distinct_id
            
FROM 
    vw_cards
          
          ''').show()

# Finalizando a SparkSession após o uso
spark.stop()