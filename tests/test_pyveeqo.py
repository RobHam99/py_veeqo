import requests
import unittest
from json import JSONDecodeError
from unittest.mock import patch, MagicMock
from py_veeqo.pyveeqo import TestApi, PyVeeqo
from py_veeqo.models import Result
from py_veeqo.exceptions import PyVeeqoException
from .utils import load_test_data


class TestPyVeeqo(unittest.TestCase):

    def test_key_none(self):
        """Raise an error when a key has not been given.
        """
        try:
            PyVeeqo()
            self.fail('A None api key must raise an error')
        except ValueError:
            self.assertTrue(True)

    @patch('py_veeqo.pyveeqo.PyVeeqo._generic_request_handler')
    def test_generic_request_handler(self, mock_request):
        """Test the generic request handler is working.
        """
        test_data = load_test_data(
            filename='generic_request_handler_data.json')
        base_url = test_data["base_url"]
        tests = test_data["tests"]

        api = TestApi(api_key='test')

        num_tests = len(tests)
        for i, test in enumerate(tests):
            print(f"\nRunning Test {i+1}/{num_tests}: ", test["test_name"])

            mock_result = Result(
                status_code=test["status_code"],
                message=test["message"],
                data=test["result"]
                )
            mock_request.return_value = mock_result

            result = api._generic_request_handler(
                http_method=test["method"],
                url=base_url + test["url"],
                params=test["params"],
                data=test["data"],
                json=test["json"]
            )
            print(result.message)
            self.assertIsInstance(result, Result)
            self.assertEqual(result.status_code, int(test["status_code"]))
            self.assertEqual(result.message, test["message"])
            self.assertEqual(result.data, test["result"])

    def test_build_endpoint(self):
        """Test endpoint strings are constructed correctly.
        """
        test_data = load_test_data("build_endpoint_data.json")
        tests = test_data["tests"]
        test_base_url = test_data["base_url"]

        api = TestApi(api_key='test')

        for test in tests:
            result = api._build_endpoint(
                path_structure=test["path_structure"],
                path_params=test["path_params"]
                )
            self.assertIsInstance(result, str)
            self.assertEqual(result, test_base_url + test["result"])

    def test_missing_path_param(self):
        """Test that an error is raised when a path parameter is missing."""
        api = TestApi(api_key='test')
        with self.assertRaises(ValueError):
            # 'order_id' is missing in the path_params
            api._build_endpoint(
                path_structure=["orders", "{order_id}"],
                path_params={}
                )

    def test_invalid_path_structure(self):
        """Test that an error is raised when the path structure is invalid."""
        api = TestApi(api_key='test')
        test_data = load_test_data("invalid_path_data.json")["tests"]
        for test in test_data:
            with self.assertRaises(ValueError):
                api._build_endpoint(
                    path_structure=test["path_structure"],
                    path_params=test["path_params"]
                    )

    @patch('requests.request')
    def test_invalid_json_response(self, mock_request):
        """Test that an error is raised when the response is invalid."""
        # Mock a response with invalid JSON
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_request.return_value = mock_response

        api = TestApi(api_key='test')
        with self.assertRaises(PyVeeqoException):
            api._generic_request_handler(http_method="GET", url="fake_url")

    @patch('requests.request')
    def test_api_request_timeout(self, mock_request):
        """Test that an error is raised when the request times out."""
        # Mock a timeout exception
        mock_request.side_effect = requests.exceptions.Timeout

        api = TestApi(api_key='test')
        with self.assertRaises(PyVeeqoException):
            api._generic_request_handler(http_method="GET", url="fake_url")

    @patch('requests.request')
    def test_client_error_4xx(self, mock_request):
        # Mock a 404 response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.ok = False
        mock_response.reason = "Not Found"
        mock_response.json.return_value = {"message": "Resource not found"}
        mock_request.return_value = mock_response

        api = TestApi(api_key='test')
        with self.assertRaises(PyVeeqoException):
            api._generic_request_handler(http_method="GET", url="fake_url")

    @patch('requests.request')
    def test_server_error_5xx(self, mock_request):
        # Mock a 500 Internal Server Error response
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.ok = False
        mock_response.reason = "Internal Server Error"
        mock_response.json.return_value = {"message": "Server error occurred"}
        mock_request.return_value = mock_response

        api = TestApi(api_key='test')
        with self.assertRaises(PyVeeqoException):
            api._generic_request_handler(http_method="GET", url="fake_url")

    @patch('requests.request')
    def test_unsupported_http_method(self, mock_request):
        # Mock an unsupported HTTP method
        mock_request.side_effect = ValueError("Unsupported HTTP method")

        api = TestApi(api_key='test')
        with self.assertRaises(ValueError):
            api._generic_request_handler(http_method="FOO", url="fake_url")
            
    @patch('requests.request')
    def test_no_data_for_post_request(self, mock_request):
        # Mock a POST request with no data
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.ok = False 
        mock_request.return_value = mock_response

        api = TestApi(api_key='test')
        with self.assertRaises(PyVeeqoException):
            api._generic_request_handler(http_method="POST", url="fake_url")

    @patch('requests.request')
    def test_invalid_response_format(self, mock_request):
        # Mock a response that does not follow the expected format
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.reason = "OK"
        mock_response.text = '{ "name": "John Doe", "age": 30 '  # Invalid JSON (missing closing brace)
        mock_response.json.side_effect = JSONDecodeError("Expecting ',' delimiter", mock_response.text, 35)
        mock_request.return_value = mock_response

        api = TestApi(api_key='test')
        with self.assertRaises(PyVeeqoException):
            api._generic_request_handler(http_method="GET", url="fake_url")


if __name__ == '__main__':
    unittest.main()
