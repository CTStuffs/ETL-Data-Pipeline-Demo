# ETL Data Pipeline Demo

A Python-based ETL pipeline that extracts data from a raw CSV file, applies cleaning and transformation logic, and loads the result into Google BigQuery. The dataset used was a modified version of the dataset sourced from [here](https://www.kaggle.com/code/alyashoush/data-cleaning).

The data cleaning process acted on extremely strict rules. Any row with missing content was considered invalid. 

## Project Overview

- Extract: read raw CSV data from `data/raw/`.
- Transform: clean, normalize, and validate rows in `src/transform.py`.
- Load: append transformed results into a BigQuery table using `src/load.py`.
- Test: unit tests for above three tasks in `test/`

## Architecture

- `main.py` — pipeline orchestrator using environment variables.
- `src/extract.py` — CSV ingestion logic.
- `src/transform.py` — data validation, normalization, and type conversion.
- `src/load.py` — BigQuery upload and dataset management.
- `data/` — local dataset storage.
- `test/` - unit tests

## Dependencies

- Python 3.x
- pandas
- python-dotenv
- google-cloud-bigquery
- word2number
- pytest

## Quick Start

1. Install dependencies:

```bash
pip install pandas python-dotenv google-cloud-bigquery word2number pytest
```

2. Configure environment variables in `.env`:

```text
GC_PROJECT_ID=<your-gcp-project>
GC_DATASET_ID=<bigquery-dataset>
GC_TABLE_ID=<bigquery-table>
DATA_PATH=data/raw/<your-file>.csv
```

3. Run the pipeline:

Ensure that your BigQuery credentials can be authorized. Then run:

```bash
python main.py
```

## Testing
```
pytest test/
```

## Notes

- The current implementation uses `pandas` for transformation.
- The pipeline is designed to support future improvements such as Parquet conversion, Polars-based transformation, and more advanced BigQuery schema handling.

## Output

- Cleaned dataset loaded into `project.dataset.table` in Google BigQuery.
- Duplicate rows are removed, rows with missing data are dropped, and numeric fields are normalized.

## Potential Next Steps

- Replace `pandas` with `polars` for faster transformation.
- CLI flags for improved production readiness.
- Integration testing for the entire pipeline