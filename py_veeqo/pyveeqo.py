"""Main module for the PyVeeqo package. Handles API calling."""
from typing import Dict, List, Callable
from functools import wraps
import os
from json import JSONDecodeError
import requests
import requests.packages
from py_veeqo.exceptions import PyVeeqoException
from py_veeqo.models import Result
from py_veeqo.types import JSONType


class PyVeeqo:
    """Rest adapter for the Veeqo api.
    """
    base_url = "https://api.veeqo.com/"

    def __init__(self, api_key: str = None):
        """Constructor for PyVeeqo

        Args:
            api_key (str, optional): public api key supplied by user.
            Defaults to ''.
            ssl_verify (bool, optional): If having issues with SSL/TLS
            cert validation, can set to False. Defaults to True.
        """
        if api_key is None:
            api_key = os.environ.get('PYVEEQO_API_KEY')
        if not api_key or not isinstance(api_key, str):
            raise ValueError('The PyVeeqo API key must be provided '
                            'either through the key parameter or '
                            'through the environment variable '
                            'PYVEEQO_API_KEY. Apply for a free '
                            'Veeqo API key: '
                            'https://help.veeqo.com/en/articles/3826041-api-key')
        self._api_key = api_key
        self._ssl_verify = True

    @classmethod
    def _build_endpoint(cls, endpoint: str) -> str:
        """Builds the endpoint url.

        Args:
            endpoint (str): endpoint to be built.

        Returns:
            str: full api url.
        """
        if endpoint[0] == "/":
            return cls.base_url + endpoint
        elif endpoint[-1] == "/":
            return cls.base_url + "/".join(endpoint[:-1])
        return cls.base_url + "/".join(endpoint)

    @classmethod
    def _endpoint_builder(cls, method: str) -> Callable:
        """Decorator to dynamically build api endpoints and call the 
        main request handler.

        Args:
            method (str): _description_

        Returns:
            Callable: _description_
        """

        def decorator(func: Callable) -> Callable:

            @wraps(func)
            def wrapper(self, *args, **kwargs):
                
                # Get the endpoint from the function
                endpoint = func(self, *args, **kwargs)
                
                # Build the full url
                url = cls._build_endpoint(endpoint)

                # Based on method, extract data, params and json

                data = kwargs.get("data")
                params = kwargs.get("params")
                json = kwargs.get("json")

                return self._generic_request_handler(
                    http_method=method,
                    url=url,
                    params=params,
                    data=data,
                    json=json
                    )

            return wrapper
        return decorator

    def _generic_request_handler(
        self,
        http_method: str,
        url: str,
        params: Dict = None,
        data: Dict = None,
        json: JSONType = None) -> Result:
        """Generic request method.

        Args:
            http_method (str): http method being used e.g. POST or GET.
            url (str): API call url, specific to API being used.
            params (Dict, optional): API query parameters. Defaults to None.
            data (Dict, optional): data if POST. Defaults to None.

        Raises:
            PyVeeqoException: failed request.
            PyVeeqoException: error decoding JSON.
            PyVeeqoException: api call failure.

        Returns:
            Result: Result object containing status code, message and data.
        """

        # Validate that mutually exclusive parameters are not used together
        if data and json:
            raise ValueError("Cannot use both 'data' and 'json' in the same request.")
        headers = {'x-api-key': self._api_key}
        try:
            response = requests.request(
                method=http_method,
                url=url,
                verify=self._ssl_verify,
                headers=headers,
                params=params,
                data=data,
                json=json
            )
        except requests.exceptions.RequestException as error:
            raise PyVeeqoException("Request Failed") from error

        data_out = None
        if response.status_code != 204:
            # Deserialize JSON output to Python object
            try:
                data_out = response.json()
            except (ValueError, JSONDecodeError) as error:
                raise PyVeeqoException("Bad JSON in response") from error

        if response.ok:
            return Result(
                response.status_code,
                message=response.reason,
                data=data_out
                )
        raise PyVeeqoException(f"{response.status_code}: {response.reason}")


class TestApi(PyVeeqo):
    """Rest adapter for the Veeqo API with test url.
    -> FOR TESTING ONLY
    """
    base_url = "https://private-anon-ab721c1a44-veeqo.apiary-mock.com/"
