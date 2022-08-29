import os

### Set Environment Variables
os.environ['envn'] = 'TEST'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

### Get Environment Variables
envn = os.environ['envn']
header = os.environ['header']
inferSchema = os.environ['inferSchema']

### Set Other Variables
appName="USA Prescriber Research Report"
current_path =  os.getcwd()
staging_dim_city = current_path + '\..\staging\dimentional_data'
staging_fact = current_path + '\..\staging\\fact'








