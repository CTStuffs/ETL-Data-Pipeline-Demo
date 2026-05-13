import pytest
import pandas as pd
from src.extract import extract_csv


def test_extract_csv_valid_file():
    result =  extract_csv("test/data/valid_data.csv")
    assert isinstance(result, pd.DataFrame)

# def test_extract_empty_file_path():
#     """Test handling of empty file paths"""
#     with pytest.raises(SystemExit) as exc_info:
#         extract_csv("")
    
#     assert exc_info.value.code == "Exiting due to empty file path..."


def test_extract_csv_file_not_found():
    """Test handling of non-existent file paths"""
    with pytest.raises(FileNotFoundError, match=r"File does not exist: .*"):
        extract_csv("test/data/non_existent_file.csv")
    

def test_extract_csv_empty_file():
    """Test behavior when CSV has no data rows"""
    with pytest.raises(ValueError, match = r"Invalid CSV format in file.*"):
        extract_csv("test/data/empty_file.csv")
    

def test_extract_bad_format_file():
    """Test behavior when CSV has no data rows"""
    with pytest.raises(ValueError, match=r"Invalid CSV format in file.*"):
        extract_csv("test/data/badformatfile.csv")  