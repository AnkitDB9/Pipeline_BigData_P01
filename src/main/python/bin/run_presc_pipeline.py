### Import all the necessary Modules
import get_all_variables as gav
from create_objects import get_spark_object
from validations import get_curr_date
import sys
import logging
import logging.config

### Load the Logging Configuration File
logging.config.fileConfig(fname='../util/logging_to_file.conf')

def main():
    try:
        logging.info("main() is started ...")
        ### Get Spark Object
        spark = get_spark_object(gav.envn,gav.appName)
        # Validate Spark Object
        get_curr_date(spark)
        # Set up Error Handling
        # Set up Logging Configuration Mechanism

        ### Initiate run_presc_data_ingest Script
        # Load the City File
        # Load the Prescriber Fact File
        # Validate
        # Set up Error Handling
        # Set up Logging Configuration Mechanism

        ### Initiate run_presc_data_preprocessing Script
        # Perform data Cleaning Operations
        # Validate
        # Set up Error Handling
        # Set up Logging Configuration Mechanism

        ### Initiate run_presc_data_transform Script
        # Apply all the transfrmations Logics
        # Validate

        # Set up Logging Configuration Mechanism

        ### Initiate run_data_extraction Script
        # Validate
        # Set up Error Handling
        # Set up Logging Configuration Mechanism

        ### End of Application Part 1
        logging.info("presc_run_pipeline.py is Completed.")
    except Exception as exp:
        print("Error Occured in the main() method. Please check the Stack Trace to go to the respective module and fix it." +str(exp))
        sys.exit(1)

if __name__ == "__main__" :
    logging.info("run_presc_pipeline is Started ...")
    main()