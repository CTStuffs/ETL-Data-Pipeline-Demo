from google.cloud import bigquery
import pandas as pd

def load_to_bigquery(df, project_id, dataset_id, table_name):
    # project_id = "project-f29ff3f0-617a-46c7-94f"

    # dataset_id = "test_data"

    # table_name = "tablename"

    table_id = f"{project_id}.{dataset_id}.{table_name}"
    client= bigquery.Client(project=project_id)

    # Create dataset if it doesn't exist
    dataset_ref = bigquery.Dataset(f"{project_id}.{dataset_id}")
    dataset_ref.location = "australia-southeast1"

    client.create_dataset(dataset_ref, exists_ok=True)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",  # or WRITE_TRUNCATE
    )

    # Upload dataframe to BigQuery
    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    print(f"Loaded {len(df)} rows into {table_id}")