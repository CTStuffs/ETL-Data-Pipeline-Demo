from google.cloud import bigquery
import pandas as pd
from google.auth.exceptions import DefaultCredentialsError

def load_to_bigquery(df, project_id, dataset_id, table_name):
    if df.empty:
        raise ValueError("DataFrame is empty. No data to load to BigQuery.")

    table_id = f"{project_id}.{dataset_id}.{table_name}"
    client= bigquery.Client(project=project_id)

    # Create dataset if it doesn't exist
    dataset_ref = bigquery.Dataset(f"{project_id}.{dataset_id}")
    dataset_ref.location = "australia-southeast1"

    client.create_dataset(dataset_ref, exists_ok=True)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_EMPTY",  # or WRITE_TRUNCATE
    )

    try:
        # Upload dataframe to BigQuery
        job = client.load_table_from_dataframe(
            df,
            table_id,
            job_config=job_config
        )
        job.result()

        print(f"Loaded {len(df)} rows into {table_id}")
        return table_id
    except DefaultCredentialsError as e:
         raise RuntimeError("BigQuery authentication failed")
    except Exception as e:
        raise Exception(f"Error loading data to BigQuery: {e}") from e   
