from typing import Dict, Optional
from json import JSONDecodeError
import requests
import requests.packages
from py_veeqo.exceptions import PyVeeqoException
from py_veeqo.models import Result
from py_veeqo.types import JSONType


class PyVeeqo:
    """Rest adapter for the Veeqo api.
    """
    _HOST_URL = "https://api.veeqo.com/"

    def __init__(self, api_key: str = ''):
        """Constructor for PyVeeqo

        Args:
            api_key (str, optional): public api key supplied by user.
            Defaults to ''.
            ssl_verify (bool, optional): If having issues with SSL/TLS
            cert validation, can set to False. Defaults to True.
        """
        self._api_key = api_key
        self._ssl_verify = True

    def _generic_request_handler(self,
                                 http_method: str,
                                 endpoint: str,
                                 params: Dict = None,
                                 data: Dict = None) -> Result:
        """Generic request method.

        Args:
            http_method (str): http method being used e.g. POST or GET.
            endpoint (str): API endpoint, specific to API being used.
            params (Dict, optional): API query parameters. Defaults to None.
            data (Dict, optional): data if POST. Defaults to None.

        Raises:
            PyVeeqoException: _description_
            PyVeeqoException: _description_
            PyVeeqoException: _description_

        Returns:
            Result: Result object containing status code, message and data.
        """
        url = self._HOST_URL + endpoint
        headers = {'x-api-key': self._api_key}
        try:
            response = requests.request(
                method=http_method,
                url=url,
                verify=self._ssl_verify,
                headers=headers,
                params=params,
                json=data
                )
        except requests.exceptions.RequestException as error:
            raise PyVeeqoException("Request Failed") from error

        # Deserialize JSON output to Python object
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as error:
            raise PyVeeqoException("Bad JSON in response") from error

        is_success = response.ok
        if is_success:
            return Result(
                response.status_code,
                message=response.reason,
                data=data_out
                )
        raise PyVeeqoException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, params: Dict = None) -> Result:
        """HTTP GET request.

        Args:
            endpoint (str): API endpoint, specific to user.
            params (Dict, optional): API query params. Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._generic_request_handler(
            http_method='GET',
            endpoint=endpoint,
            params=params
        )

    def post(self, endpoint: str, data: Dict = None,
             json: Optional[JSONType] = None) -> Result:
        """HTTP POST request.

        Args:
            endpoint (str): API endpoint, specific to user.
            params (Dict, optional): API query params. Defaults to None.
            data (Dict, optional): POST data. Defaults to None.
            json(JSONType, optional): Json data, alternative to data arg.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._generic_request_handler(
            http_method='POST',
            endpoint=endpoint,
            data=data,
            json=json
        )

    def delete(self, endpoint: str) -> Result:
        """HTTP DELETE request.

        Args:
            endpoint (str): API endpoint, specific to user.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._generic_request_handler(
            http_method='DELETE',
            endpoint=endpoint,
        )

    def put(self, endpoint: str, data: Dict = None) -> Result:
        """HTTP PUT request.

        Args:
            endpoint (str): API endpoint, specific to user.
            data (Dict, optional): Data to update. Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._generic_request_handler(
            http_method='PUT',
            endpoint=endpoint,
            data=data
        )
