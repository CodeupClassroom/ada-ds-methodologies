# IPython log file


import pandas as pd, numpy as np, pyspark
df = pd.DataFrame({'x': ['a', 'b', np.nan, 'd', 'e']})
df
spark = pyspark.sql.SparkSession.builder.getOrCreate()
df
spark.createDataFrame(df)
df
import pyspark.sql.types as T
schema = T.StructType([T.StructField('x', T.StringType())])
schema
spark.createDataFrame(df, schema=schema)
spark.createDataFrame(df)
