import os
import pytest
from unittest.mock import patch, MagicMock
from app import check_user_exists


def test_check_user_exists_uses_environment_variables():
    """Test that check_user_exists uses environment variables for DB connection."""
    # Set environment variables
    test_env_vars = {
        "DB_NAME": "test_db",
        "DB_USER": "test_user",
        "DB_PASSWORD": "test_password",
        "DB_HOST": "test_host",
        "DB_PORT": "5433"
    }
    
    with patch.dict(os.environ, test_env_vars, clear=False):
        with patch('psycopg2.connect') as mock_connect:
            # Mock the connection and cursor
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = None
            mock_conn.cursor.return_value = mock_cursor
            mock_connect.return_value = mock_conn
            
            # Call the function
            result = check_user_exists("testuser", "testpass")
            
            # Verify psycopg2.connect was called with environment variables
            mock_connect.assert_called_once_with(
                dbname="test_db",
                user="test_user",
                password="test_password",
                host="test_host",
                port="5433"
            )


def test_check_user_exists_uses_default_values_when_no_env_vars():
    """Test that check_user_exists uses default values when environment variables are not set."""
    # Clear the specific environment variables if they exist
    env_vars_to_clear = ["DB_NAME", "DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT"]
    original_values = {}
    
    for var in env_vars_to_clear:
        if var in os.environ:
            original_values[var] = os.environ.pop(var)
    
    try:
        with patch('psycopg2.connect') as mock_connect:
            # Mock the connection and cursor
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = None
            mock_conn.cursor.return_value = mock_cursor
            mock_connect.return_value = mock_conn
            
            # Call the function
            result = check_user_exists("testuser", "testpass")
            
            # Verify psycopg2.connect was called with default values
            mock_connect.assert_called_once_with(
                dbname="your_db_name",
                user="your_db_user",
                password="p@ssw0rd",
                host="localhost",
                port="5432"
            )
    finally:
        # Restore original environment variables
        for var, value in original_values.items():
            os.environ[var] = value
