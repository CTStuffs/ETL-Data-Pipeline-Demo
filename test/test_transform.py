import pytest
import pandas as pd
from src.transform import clean_data, save_clean_data, convert_cancelled, convert_words


def test_convert_cancelled_yes_variations():
    """Test conversion of YES/Y variations to TRUE"""
    pass


def test_convert_cancelled_no_variations():
    """Test conversion of NO/N variations to FALSE"""
    pass


def test_convert_cancelled_unexpected_values():
    """Test that unexpected values pass through unchanged"""
    pass


def test_convert_words_valid():
    """Test valid word-to-number conversions"""
    pass


def test_convert_words_invalid():
    """Test invalid words return unchanged"""
    pass


def test_clean_data_remove_duplicates():
    """Test removal of duplicate rows"""
    pass


def test_clean_data_remove_nulls():
    """Test removal of rows with null values"""
    pass


def test_clean_data_listing_id_conversion():
    """Test conversion of listing_id to integers"""
    pass


def test_clean_data_date_standardization():
    """Test standardization of checkin/checkout dates"""
    pass


def test_clean_data_nights_conversion():
    """Test conversion and filtering of nights field"""
    pass


def test_clean_data_price_per_night_handling():
    """Test handling of price_per_night including 'free' values"""
    pass


def test_clean_data_payment_status_uppercase():
    """Test conversion of payment_status to uppercase"""
    pass


def test_clean_data_is_cancelled_boolean():
    """Test conversion of is_cancelled to boolean"""
    pass


def test_save_clean_data():
    """Test saving cleaned data to CSV"""
    pass