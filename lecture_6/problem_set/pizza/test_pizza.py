import pytest
import sys
from unittest.mock import mock_open, patch
from pizza import handle_cli_arguments, process_and_read_csv, display_data  

# Unit test for handle_cli_arguments()

def test_no_arguments(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['script_name'])
    with pytest.raises(SystemExit) as e:
        handle_cli_arguments()
    assert str(e.value) == '1', "Expected sys.exit() with 'Too few command-line arguments.' but got a different response or no exit."

def test_single_argument_acceptance(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['script_name', 'filename.csv'])
    result = handle_cli_arguments()
    assert result == 'filename.csv', "Expected function to accept exactly one argument and proceed without error, but it did not."

def test_more_than_one_argument(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['script_name', 'filename.csv', 'extra_arg'])
    with pytest.raises(SystemExit) as e:
        handle_cli_arguments()
    assert str(e.value) == '1', "Expected sys.exit() with 'Too many command-line arguments.' but got a different response or no exit."

def test_single_argument_with_correct_extension(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['script_name', 'good_file.csv'])
    result = handle_cli_arguments()
    assert result == 'good_file.csv', "Expected function to validate '.csv' extension and proceed without error."

def test_single_argument_with_incorrect_extension(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['script_name', 'bad_file.txt'])
    with pytest.raises(SystemExit) as e:
        handle_cli_arguments()
    assert str(e.value) == '1', "Expected sys.exit() with 'Not a CSV file.' but got a different response or no exit."

# Unit tests for process_and_read_csv()
def test_file_does_not_exist():
    with patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(SystemExit) as e:
            process_and_read_csv('nonexistent.csv')
        assert str(e.value) == '1', "Expected sys.exit() with 'File does not exist.' but got a different response or no exit."

def test_successful_file_reading_and_parsing():
    # Mock CSV data
    csv_content = "header1,header2\nvalue1,value2\nvalue3,value4"
    m = mock_open(read_data=csv_content)
    with patch('builtins.open', m):
        with patch('csv.DictReader', return_value=[{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}]) as mock_dict_reader:
            result = process_and_read_csv('valid.csv')
            mock_dict_reader.assert_called_once()  # Ensures DictReader was invoked
            assert result == [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}], \
                "Expected function to return a list of dictionaries parsed from the CSV file but failed to do so."

# Run the test
if __name__ == "__main__":
    pytest.main()