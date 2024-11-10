import unittest
from unittest.mock import patch
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.models import Result
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
        mock_result = Result(
            status_code=200,
            message="Success",
            data=test_data
            )
        mock_request.return_value = mock_result

        api = PyVeeqo(test=True)

        result = api._generic_request_handler(
            http_method="GET",
            url=api.base_url + "orders",
            params=None,
            data=None,
            json=None
        )

        self.assertIsInstance(result, Result)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.message, 'Success')
        self.assertEqual(result.data, test_data)

    def test_build_endpoint(self):
        """Test endpoint strings are constructed correctly.
        """
        test_data = load_test_data("build_endpoint_data.json")
        tests = test_data["tests"]
        test_base_url = test_data["base_url"]

        api = PyVeeqo(api_key='dummy')

        for test in tests:
            result = api._build_endpoint(
                path_structure=test["path_structure"],
                path_params=test["path_params"]
                )
            self.assertIsInstance(result, str)
            self.assertEqual(result, test_base_url + test["result"])


if __name__ == '__main__':
    unittest.main()
