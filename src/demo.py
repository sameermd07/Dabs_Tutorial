from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Sameer"),
    (2, "Rahul"),
    (3, "Amit")
]

df = spark.createDataFrame(
    data,
    ["id", "name"]
)

df.show()