from src.extract import extract_csv
from src.transform import clean_data, save_clean_data
from src.load import load_to_bigquery
import os
from dotenv import load_dotenv
load_dotenv()

project_id = os.getenv('GC_PROJECT_ID')
dataset_id = os.getenv('GC_DATASET_ID')
table_name = os.getenv('GC_TABLE_ID')
file_path = os.getenv('DATA_PATH')
clean_data_path = os.getenv('CLEAN_DATA_PATH')

print(file_path)
df = extract_csv(file_path)
df = clean_data(df)
save_clean_data(df, clean_data_path)
load_to_bigquery(df, project_id, dataset_id, table_name)