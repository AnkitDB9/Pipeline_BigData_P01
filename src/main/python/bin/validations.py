
def get_curr_date(spark):
    try:
        opDF = spark.sql(""" select current_date """)
        print("Validate the Spark object by printing Current Date - " + str(opDF.collect()))
    except NameError as exp:
        print("NameError in the method - spark_curr_date(). Please check the Stack Trace. " + str(exp))
        raise
    except Exception as exp:
        print("Error in the method - spark_curr_date(). Please check the Stack Trace. " + str(exp))
        raise
    else:
        print("Spark object is validated. Spark Object is ready.")






