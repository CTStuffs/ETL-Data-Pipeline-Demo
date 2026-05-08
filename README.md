# ETL-Data-Pipeline-Demo
This project entails building an ETL pipeline using a publicly available dataset, such as weather or transportation data. You will extract the data from a raw CSV file, clean and transform it using Python, and load the transformed data into Google BigQuery.

To make this project truly modern, try using Polars for your transformations instead of the traditional Pandas library. Polars is significantly faster and becoming a favorite tool in the data engineering community. Additionally, before loading the data into the cloud, practice converting it into Parquet format. Parquet is a columnar storage format that is far more efficient than CSV and is the standard for big data storage.

This project is excellent for beginners as it introduces core ETL concepts—data extraction, transformation, and loading—while giving exposure to cloud tools like BigQuery and critical file formats.

You'll also learn how to interact with cloud data warehouses, a core skill in modern data engineering, using simple tools like Python and the BigQuery API. For an introduction, review the beginner’s guide to BigQuery.

As for the data, you can select an available dataset from either Kaggle or data.gov.
