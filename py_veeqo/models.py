"""Data models for PyVeeqo."""
from typing import List, Dict


class Result:
    """Store the results from a HTTP response.
    """
    def __init__(self, status_code: int, message: str = '',
                 data: List[Dict] = None):
        """Result returned from PyVeeqo adapter.

        Args:
            status_code (int): HTTP status code.
            message (str, optional): Human readable result. Defaults to ''.
            data (List[Dict], optional): Resulting data from query.
            Defaults to None.
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []
