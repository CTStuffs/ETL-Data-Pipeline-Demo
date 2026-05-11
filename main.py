from src.extract import extract_csv
from src.transform import clean_data
from src.load import load_to_bigquery
from dotenv import load_dotenv
import os


project_id = os.getenv('GC_PROJECT_ID')

dataset_id = os.getenv('GC_DATASET_ID')

table_name = os.getenv('GC_TABLE_ID')

file_path = os.getenv('DATA_PATH')
load_dotenv()


df = extract_csv(file_path)
df = clean_data(df)
load_to_bigquery(df, project_id, dataset_id, table_name)