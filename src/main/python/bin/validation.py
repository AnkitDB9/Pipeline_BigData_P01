def validate(spark):
    df=spark.sql('''select current date''')
    print("current date is :- " + df.dict)