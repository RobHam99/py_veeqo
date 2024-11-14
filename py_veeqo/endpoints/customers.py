from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Customers(PyVeeqo):
    """This class implements all the customers api calls.
    """
    _ENDPOINT_KEY = "customers"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("customers",))
    def get_all_customers(self, page_size: int = 12, page: int = 1, query: str = None) -> Result:
        """Get a list of all customers.
        https://developers.veeqo.com/docs#/reference/customers/customer-collection/list-all-customers

        Args:
            page_size (int, optional): Number of items per page. Defaults to 12.
            page (int, optional): Page number. Defaults to 1.
            query (str, optional): Search query. Defaults to None
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="POST", path_structure=("customers",))
    def create_a_customer(self, data: Dict = None, 
                          json: Optional[JSONType] = None) -> Result:
        """Create a new customer.
        https://developers.veeqo.com/docs#/reference/customers/customer-collection/create-a-customer

        Args:
            data (Dict, optional): customer data. Defaults to None.
            json (Optional[JSONType], optional): customer data in json format. Defaults to None.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("customers", "{customer_id}"))
    def view_customer_detail(self, customer_id: int) -> Result:
        """Get details of a specific customer.
        https://developers.veeqo.com/docs#/reference/customers/customer/view-customer-detail

        Args:
            customer_id (int): customer id.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="PUT", path_structure=("customers", "{customer_id}"))
    def update_customer_detail(self, customer_id: int, 
                               data: Dict = None) -> Result:
        """Update details of a specific customer.
        https://developers.veeqo.com/docs#/reference/customers/customer/update-customer-detail

        Args:
            customer_id (int): customer id.
            data (Dict, optional): customer data. Defaults to None.
        """
        pass
