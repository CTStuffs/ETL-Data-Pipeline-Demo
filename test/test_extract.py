import pytest
import pandas as pd
from src.extract import extract_csv


def test_extract_csv_valid_file(sample_cleaned_data):
    result =  extract_csv(sample_cleaned_data)
    assert isinstance(result, pd.DataFrame)

def test_extract_csv_file_not_found(sample_non_existent_data):
    """Test handling of non-existent file paths"""
    with pytest.raises(FileNotFoundError, match=r"File does not exist: .*"):
        extract_csv(sample_non_existent_data)
    

def test_extract_csv_empty_file(sample_empty_data):
    """Test behavior when CSV has no data rows"""
    with pytest.raises(ValueError, match = r"Invalid CSV format in file.*"):
        extract_csv(sample_empty_data)

def test_extract_bad_format_file(sample_bad_data):
    """Test behavior when CSV has no data rows"""
    with pytest.raises(ValueError, match=r"Invalid CSV format in file.*"):
        extract_csv(sample_bad_data)  