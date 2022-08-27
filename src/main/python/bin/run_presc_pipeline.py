### Import all the necessary Modules
import get_all_variables as gav
from create_objects import get_spark_object

def main():
    ### Get Spark Object
    spark = get_spark_object(gav.envn,gav.appName)
    print("Spark Object is created ...")
        # Validate Spark Object
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

    ### Initiate run_presc_data_ingest Script
        # Load the City File
        # Load the Prescriber Fact File
        # Validate
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

    ### Initiate run_presc_data_preprocessing Script
        # Perform data Cleaning Operations
        # Validate
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

    ### Initiate run_presc_data_transform Script
        # Apply all the transfrmations Logics
        # Validate
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

    ### Initiate run_data_extraction Script
        # Validate
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

### End of Application Part 1




if __name__ == "__main__" :
    main()