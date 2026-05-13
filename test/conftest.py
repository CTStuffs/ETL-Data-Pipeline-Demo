import pytest
import pandas as pd
import tempfile
import os
from src.extract import extract_csv
from src.transform import clean_data

@pytest.fixture
def load_sample_data(sample_cleaned_data):
    df = extract_csv(sample_cleaned_data)
    df = clean_data(df)
    return df


@pytest.fixture
def sample_cleaned_data():
    return "test/data/valid_data.csv"

@pytest.fixture
def sample_bad_data():
    return "test/data/badformatfile.csv"

@pytest.fixture
def sample_empty_data():
    return "test/data/empty_file.csv"

@pytest.fixture
def sample_non_existent_data():
    return "test/data/non_existent_file.csv"

@pytest.fixture
def temp_csv_file():
    """Temporary CSV file for testing file operations"""
    pass


@pytest.fixture
def mock_bigquery_client():
    """Mock BigQuery client for testing"""
    pass