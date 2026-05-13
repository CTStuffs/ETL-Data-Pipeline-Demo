# ETL Data Pipeline Demo

A Python-based ETL pipeline that extracts data from a raw CSV file, applies cleaning and transformation logic, and loads the result into Google BigQuery.

The data cleaning process acted on extremely strict rules. Any row with missing content was considered invalid.

## Project Overview

- Extract: read raw CSV data from `data/raw/`.
- Transform: clean, normalize, and validate rows in `src/transform.py`.
- Load: append transformed results into a BigQuery table using `src/load.py`.

## Architecture

- `main.py` — pipeline orchestrator using environment variables.
- `src/extract.py` — CSV ingestion logic.
- `src/transform.py` — data validation, normalization, and type conversion.
- `src/load.py` — BigQuery upload and dataset management.
- `data/` — local dataset storage.

## Dependencies

- Python 3.x
- pandas
- python-dotenv
- google-cloud-bigquery
- word2number

## Quick Start

1. Install dependencies:

```bash
pip install pandas python-dotenv google-cloud-bigquery word2number
```

2. Configure environment variables in `.env`:

```text
GC_PROJECT_ID=<your-gcp-project>
GC_DATASET_ID=<bigquery-dataset>
GC_TABLE_ID=<bigquery-table>
DATA_PATH=data/raw/<your-file>.csv
```

3. Run the pipeline:

```bash
python main.py
```

## Notes

- The current implementation uses `pandas` for transformation.
- The pipeline is designed to support future improvements such as Parquet conversion, Polars-based transformation, and more advanced BigQuery schema handling.

## Output

- Cleaned dataset loaded into `project.dataset.table` in Google BigQuery.
- Duplicate rows are removed, missing data is dropped, and numeric fields are normalized.

## Recommended Next Steps

- Replace `pandas` with `polars` for faster transformation.
- Add CLI flags and schema validation to improve production readiness.
