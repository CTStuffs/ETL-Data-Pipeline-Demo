from google.cloud import bigquery
import pandas as pd

# Create a BigQuery client - it automatically picks up your project from ADC
client = bigquery.Client(project="project-f29ff3f0-617a-46c7-94f")

# Write a standard SQL query against the public stackoverflow dataset
query = """
SELECT * FROM `project-f29ff3f0-617a-46c7-94f.babynames.names_2024` LIMIT 1000
"""

# Execute the query and convert results directly to a Pandas DataFrame
df = client.query(query).to_dataframe()

print(df.head())
print(f"Total rows returned: {len(df)}")