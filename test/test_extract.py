import pytest
import pandas as pd
from src.extract import extract_csv


def test_extract_csv_valid_file():
    result =  extract_csv("valid_file.csv")
    assert isinstance(result, pd.DataFrame)

def test_extract_empty_file_path():
    """Test handling of empty file paths"""
    with pytest.raises(SystemExit) as exc_info:
        extract_csv("")
    
    assert exc_info.value.code == "Exiting due to empty file..."


def test_extract_csv_file_not_found():
    """Test handling of non-existent file paths"""
    with pytest.raises(SystemExit) as exc_info:
        extract_csv("non_existent_file.csv")
    
    assert exc_info.value.code == "Exiting due to file not found..."


def test_extract_csv_empty_file():
    """Test behavior when CSV has no data rows"""
    with pytest.raises(SystemExit) as exc_info:
        extract_csv("empty_file.csv")
    
    assert exc_info.value.code == "Exiting due to invalid CSV format or empty file.."

def test_extract_bad_format_file():
    """Test behavior when CSV has no data rows"""
    with pytest.raises(SystemExit) as exc_info:
        extract_csv("badformatfile.csv")
    
    assert exc_info.value.code == "Exiting due to CSV parsing error..."    