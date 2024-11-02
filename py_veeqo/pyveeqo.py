from typing import Dict, List, Optional, Callable
from functools import wraps
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

    @classmethod
    def build_endpoint(cls, path_structure: List[str], path_params: Dict[str, str]) -> str:
        """Builds the endpoint url.

        Args:
            *segments (str): url segments.
            **path_params (str): path parameters.

        Returns:
            str: url endpoint.
        """
        endpoint = []
        for part in path_structure:
            if part.startswith("{") and part.endswith("}"):
                key = part[1:-1]
                print(key)
                if key in path_params:
                    print(str(path_params[key]))
                    endpoint.append(str(path_params[key]).strip("/"))
                else:
                    raise ValueError(f"Missing path parameter: {key}")
            else:
                endpoint.append(part.strip("/"))
                    
        return cls._HOST_URL + "/".join(endpoint)

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
                url = cls.build_endpoint(path_structure, path_params)

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

    def _generic_request_handler(self,
                                 http_method: str,
                                 url: str,
                                 params: Dict = None,
                                 data: Dict = None) -> Result:
        """Generic request method.

        Args:
            http_method (str): http method being used e.g. POST or GET.
            url (str): API call url, specific to API being used.
            params (Dict, optional): API query parameters. Defaults to None.
            data (Dict, optional): data if POST. Defaults to None.

        Raises:
            PyVeeqoException: _description_
            PyVeeqoException: _description_
            PyVeeqoException: _description_

        Returns:
            Result: Result object containing status code, message and data.
        """
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
