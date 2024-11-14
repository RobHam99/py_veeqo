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
    _PROD_URL = "https://api.veeqo.com/"
    _MOCK_URL = "https://private-anon-ab721c1a44-veeqo.apiary-mock.com/"

    def __init__(self, api_key: str = None, test: bool = False):
        """Constructor for PyVeeqo

        Args:
            api_key (str, optional): public api key supplied by user.
            Defaults to ''.
            ssl_verify (bool, optional): If having issues with SSL/TLS
            cert validation, can set to False. Defaults to True.
        """
        if not test:
            self.base_url = self._PROD_URL
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
        else:
            self._api_key = None
            self.base_url = self._MOCK_URL

        self._ssl_verify = True

    def _build_endpoint(self, path_structure: List[str], path_params: Dict[str, str]) -> str:
        """Builds the endpoint url.

        Args:
            path_structure: structure of the endpoint path.
            **path_params (Dict): path parameters.

        Returns:
            str: url endpoint.
        """
        endpoint = []
        for part in path_structure:
            if part.startswith("{") and part.endswith("}"):
                key = part[1:-1]
                if key in path_params:
                    endpoint.append(str(path_params[key]).strip("/"))
                else:
                    raise ValueError(f"Missing path parameter: {key}")
            elif part.startswith("{") or part.endswith("}"):
                raise ValueError("Path parameter not formatted correctly")
            else:
                endpoint.append(part.strip("/"))

        return self.base_url + "/".join(endpoint)

    @classmethod
    def _endpoint_builder(cls, method: str, path_structure: List[str]) -> Callable:
        """Decorator to dynamically build api endpoints and call the 
        main request handler.

        Args:
            method (str): _description_
            path_structure (List[str]): _description_

        Returns:
            Callable: _description_
        """

        def decorator(func: Callable) -> Callable:
            
            @wraps(func)
            def wrapper(*args, **kwargs):

                # Get the path parameters from the function arguments
                path_params = {part[1:-1]: kwargs[part[1:-1]] for part in path_structure if part.startswith('{') and part.endswith('}')}

                # Construct endpoint url    
                url = cls._build_endpoint(path_structure, path_params)

                data = kwargs.get("data")
                params = kwargs.get("params")
                json = kwargs.get("json")

                return cls._generic_request_handler(
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

        # Deserialize JSON output to Python object
        try:
            data_out = response.json()
            print(data_out)
        except (ValueError, JSONDecodeError) as error:
            raise PyVeeqoException("Bad JSON in response") from error

        if response.ok:
            return Result(
                response.status_code,
                message=response.reason,
                data=data_out
                )
        raise PyVeeqoException(f"{response.status_code}: {response.reason}")
