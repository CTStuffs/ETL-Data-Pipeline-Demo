import pytest
import pandas as pd
from src.load import load_to_bigquery
from unittest.mock import MagicMock, patch
from google.auth.exceptions import DefaultCredentialsError

@patch("src.load.bigquery.Client")
def test_load_to_bigquery_success(mock_client_class, load_sample_data):
    mock_client = MagicMock()
    mock_job = MagicMock()

    mock_client.load_table_from_dataframe.return_value = mock_job
    mock_client_class.return_value = mock_client

    sample_df= load_sample_data
    result = load_to_bigquery(sample_df, "test-project", "test_dataset", "test_table")

    mock_client.load_table_from_dataframe.assert_called_once()

    mock_job.result.assert_called_once()
    assert result == "test-project.test_dataset.test_table"

@patch("src.load.bigquery.Client")
def test_load_to_bigquery_invalid_credentials(mock_client_class, load_sample_data):
    mock_client = MagicMock()
    mock_client.load_table_from_dataframe.side_effect = DefaultCredentialsError(
        "Invalid credentials"
    )
    mock_client_class.return_value = mock_client

    sample_df = load_sample_data
    with pytest.raises(
        RuntimeError,
        match="BigQuery authentication failed",
    ) as exc_info:
        load_to_bigquery(
            sample_df,
            "my-project",
            "analytics",
            "users",
        )

    assert exc_info.value.args[0] == "BigQuery authentication failed"

@patch("src.load.bigquery.Client")
def test_load_to_bigquery_empty_dataframe(mock_client_class):
    mock_client_class.side_effect = DefaultCredentialsError(
        "Empty Dataframe"
    )
    sample_df = pd.DataFrame([])
    with pytest.raises(
        ValueError,
        match="DataFrame is empty. No data to load to BigQuery.",
    ):
        load_to_bigquery(
            sample_df,
            "my-project",
            "analytics",
            "users",
        )