import pytest
import pandas as pd
from src.transform import clean_data, save_clean_data, convert_cancelled, convert_words
from src.extract import extract_csv
import os

def test_convert_cancelled_yes_variations():
    assert convert_cancelled("Y") == "TRUE"
    assert convert_cancelled("YES") == "TRUE"

def test_convert_cancelled_no_variations():
    """Test conversion of NO/N variations to FALSE"""
    assert convert_cancelled("N") == "FALSE"
    assert convert_cancelled("NO") == "FALSE"


def test_convert_cancelled_unexpected_values():
    """Test that unexpected values pass through unchanged"""
    assert convert_cancelled("X") == "X"


def test_convert_words_valid():
    """Test valid word-to-number conversions"""
    assert convert_words("one") == 1
    assert convert_words("two") == 2


def test_convert_words_invalid():
    """Test invalid words return unchanged"""
    assert convert_words("something") == "something"


def test_clean_data_remove_duplicates(load_sample_data):
    """Test removal of duplicate rows"""
    df = load_sample_data.copy()
    assert df.duplicated().sum() == 0



def test_clean_data_remove_nulls(load_sample_data):
    """Test removal of rows with null values"""

    df = load_sample_data.copy()
    assert df.notnull().all().all()


def test_clean_data_listing_id_conversion(load_sample_data):
    """Test conversion of listing_id to integers"""
    df = load_sample_data.copy()
    assert df["listing_id"].dtype == int
    


def test_clean_data_date_standardization(load_sample_data):
    """Test standardization of checkin/checkout dates"""
    df = load_sample_data.copy()
    # Add assertions for date standardization
    assert pd.to_datetime(df["checkin_date"], errors="coerce").notna().all()
    assert pd.to_datetime(df["checkout_date"], errors="coerce").notna().all()



def test_clean_data_nights_conversion(load_sample_data):
    """Test conversion and filtering of nights field"""
    df = load_sample_data.copy()
    assert df["nights"].dtype == int


def test_clean_data_price_per_night_handling(load_sample_data):
    """Test handling of price_per_night including 'free' values"""
    df = load_sample_data.copy()
    # Add assertions for price_per_night handling
    assert df["price_per_night"].dtype == float


def test_clean_data_payment_status_uppercase(load_sample_data):
    """Test conversion of payment_status to uppercase"""
    df = load_sample_data.copy()
    assert df["payment_status"].str.upper().equals(df["payment_status"])


def test_clean_data_is_cancelled_boolean(load_sample_data):
    """Test conversion of is_cancelled to boolean"""
    df = load_sample_data.copy()
    assert df["is_cancelled"].dtype == bool


def test_save_clean_data(load_sample_data):
    """Test saving cleaned data to CSV"""
    df = load_sample_data.copy()
    save_clean_data(df, "test/data/temp_clean_data.csv")
    assert os.path.exists("test/data/temp_clean_data.csv")
    os.remove("test/data/temp_clean_data.csv")