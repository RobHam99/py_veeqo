import json


def load_test_data(filename: str = ''):
    """Load the test data from a JSON file."""
    with open(f'tests/test_data/{filename}', 'r') as file:
        return json.load(file)
