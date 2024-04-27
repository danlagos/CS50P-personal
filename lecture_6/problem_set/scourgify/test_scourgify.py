import pytest
import sys
from scourgify import handle_cli_arguments, validate_input_file, read_csv_file, process_data, write_to_output_csv
from unittest.mock import patch, mock_open, call
import os
import csv

# unit tetss for handle_cli_arguments()
def test_too_few_arguments(monkeypatch):
    # Test with too few arguments
    monkeypatch.setattr(sys, 'argv', ['scourgify.py'])
    with pytest.raises(SystemExit) as exc_info:
        handle_cli_arguments()
    assert exc_info.value.code != 0  # Ensure it exits with an error code
    assert str(exc_info.value) == 'Too few command-line arguments'

def test_too_many_arguments(monkeypatch):
    # Test with too many arguments
    monkeypatch.setattr(sys, 'argv', ['scourgify.py', 'input.csv', 'output.csv', 'extra_arg.csv'])
    with pytest.raises(SystemExit) as exc_info:
        handle_cli_arguments()
    assert exc_info.value.code != 0  # Ensure it exits with an error code
    assert str(exc_info.value) == 'Too many command-line arguments'

def test_correct_arguments(monkeypatch):
    # Test with correct number of arguments
    monkeypatch.setattr(sys, 'argv', ['scourgify.py', 'input.csv', 'output.csv'])
    input_file, output_file = handle_cli_arguments()
    assert input_file == 'input.csv'
    assert output_file == 'output.csv'

# unit tests for validate_input_file
def test_file_exists_and_readable(monkeypatch):
    """
    Test to ensure the function returns the filename when the file exists and is readable.
    """
    # Mock os.path.exists to always return True
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    # Mock open function to simulate opening a file successfully
    with patch('builtins.open', mock_open(read_data="data")):
        assert validate_input_file("valid_file.csv") == "valid_file.csv"

def test_file_does_not_exist(monkeypatch):
    """
    Test to ensure the function exits with an error if the file does not exist.
    """
    # Mock os.path.exists to always return False
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    with pytest.raises(SystemExit) as exc_info:
        validate_input_file("nonexistent_file.csv")
    assert str(exc_info.value) == "Could not read nonexistent_file.csv"

def test_file_not_readable(monkeypatch):
    """
    Test to ensure the function exits with an error if the file exists but is not readable.
    """
    # Mock os.path.exists to return True, simulating that the file exists
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    # Mock the open function to raise an IOError when trying to open the file
    with patch('builtins.open', mock_open()) as mocked_file:
        mocked_file.side_effect = IOError
        with pytest.raises(SystemExit) as exc_info:
            validate_input_file("unreadable_file.csv")
    assert str(exc_info.value) == "Could not read unreadable_file.csv"

#unit tests for read_csv_file()
def test_successful_file_reading():
    """
    Test that the function reads a well-formatted CSV file correctly.
    """
    # Mock data for a well-formatted CSV
    csv_data = "name,house\nHarry Potter,Gryffindor\nHermione Granger,Gryffindor"
    m = mock_open(read_data=csv_data)
    with patch('builtins.open', m):
        with patch('csv.DictReader') as mock_csv:
            mock_csv.return_value = iter([
                {"name": "Harry Potter", "house": "Gryffindor"},
                {"name": "Hermione Granger", "house": "Gryffindor"}
            ])
            result = read_csv_file("dummy_filename.csv")
            assert result == [
                {"name": "Harry Potter", "house": "Gryffindor"},
                {"name": "Hermione Granger", "house": "Gryffindor"}
            ]

def test_empty_file():
    """
    Test reading from an empty CSV file.
    """
    # Simulate an empty CSV file
    m = mock_open(read_data="")
    with patch('builtins.open', m):
        with patch('csv.DictReader') as mock_csv:
            mock_csv.return_value = iter([])
            result = read_csv_file("empty_file.csv")
            assert result == []

def test_file_format_error():
    """
    Test the function's behavior when the CSV is malformed.
    """
    # Simulate malformed CSV data
    malformed_csv_data = "name house\nHarry Potter Gryffindor"  # Incorrect delimiter
    m = mock_open(read_data=malformed_csv_data)
    with patch('builtins.open', m):
        with patch('csv.DictReader', side_effect=csv.Error) as mock_csv:
            with pytest.raises(csv.Error):
                read_csv_file("malformed_file.csv")

# unit tests for process_data()
def test_normal_input():
    """
    Test processing of standard input where each dictionary contains a 'name' and 'house' key.
    """
    data_dict = [
        {'name': 'Potter, Harry', 'house': 'Gryffindor'},
        {'name': 'Granger, Hermione', 'house': 'Gryffindor'}
    ]
    expected_output = [
        {'first': 'Harry', 'last': 'Potter', 'house': 'Gryffindor'},
        {'first': 'Hermione', 'last': 'Granger', 'house': 'Gryffindor'}
    ]
    assert process_data(data_dict) == expected_output

def test_empty_input():
    """
    Test that an empty list is handled correctly.
    """
    assert process_data([]) == []

def test_incorrect_format():
    """
    Test input where some dictionaries may not have the 'name' key.
    """
    data_dict = [
        {'house': 'Gryffindor'},  # Missing 'name'
        {'name': 'Dumbledore, Albus', 'house': 'Gryffindor'}
    ]
    with pytest.raises(KeyError):
        process_data(data_dict)

def test_additional_keys():
    """
    Test input where dictionaries contain additional keys.
    """
    data_dict = [
        {'name': 'Snape, Severus', 'house': 'Slytherin', 'position': 'Professor'}
    ]
    expected_output = [
        {'first': 'Severus', 'last': 'Snape', 'house': 'Slytherin'}
    ]
    result = process_data(data_dict)
    # Ensure additional keys are not included in the output
    assert all(key in ['first', 'last', 'house'] for d in result for key in d.keys())
    assert result == expected_output

# unit tests for write_to_output_csv()
def test_successful_writing():
    """
    Test that the function writes the provided data to a CSV file correctly.
    """
    transformed_data = [
        {'first': 'Harry', 'last': 'Potter', 'house': 'Gryffindor'},
        {'first': 'Hermione', 'last': 'Granger', 'house': 'Gryffindor'}
    ]
    output_filename = 'test_output.csv'
    m = mock_open()
    with patch('builtins.open', m):
        with patch('csv.DictWriter') as mock_writer:
            writer_instance = mock_writer.return_value
            write_to_output_csv(transformed_data, output_filename)
            mock_writer.assert_called_once_with(m(), fieldnames=['first', 'last', 'house'])
            writer_instance.writeheader.assert_called_once()
            writer_instance.writerow.assert_has_calls([
                call(transformed_data[0]),
                call(transformed_data[1])
            ])
            assert writer_instance.writerow.call_count == 2

def test_file_handling():
    """
    Test that the file is opened once and written to correctly.
    """
    transformed_data = [{'first': 'Harry', 'last': 'Potter', 'house': 'Gryffindor'}]
    output_filename = 'test_output.csv'
    m = mock_open()
    with patch('builtins.open', m) as mocked_file:
        write_to_output_csv(transformed_data, output_filename)
        mocked_file.assert_called_once_with(output_filename, mode='w', newline='')
        mocked_file().write.assert_called()