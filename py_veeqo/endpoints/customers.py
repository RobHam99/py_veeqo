from typing import List, Dict, Optional
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Customers(PyVeeqo):
    """This class implements all the customers api calls.
    """
    _ENDPOINT_KEY = "customers"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("customers",))
    def get_all_customers(self, **kwargs) -> Result:
        """Get a list of all customers.
        https://developers.veeqo.com/docs#/reference/customers/customer-collection/list-all-customers
        """

    @PyVeeqo._endpoint_builder(
            method="POST",
            path_structure=("customers",))
    def create_a_customer(self, data: Dict = None, 
                          json: Optional[JSONType] = None) -> Result:
        """Create a new customer.
        https://developers.veeqo.com/docs#/reference/customers/customer-collection/create-a-customer
        """

    @PyVeeqo._endpoint_builder(
            method="GET",
            path_structure=("customers", "{customer_id}"))
    def view_customer_detail(self, customer_id: int) -> Result:
        """Get details of a specific customer.
        https://developers.veeqo.com/docs#/reference/customers/customer/view-customer-detail
        """

    @PyVeeqo._endpoint_builder(
            method="PUT",
            path_structure=("customers", "{customer_id}"))
    def update_customer_detail(self, customer_id: int, 
                               data: Dict = None) -> Result:
        """Update details of a specific customer.
        https://developers.veeqo.com/docs#/reference/customers/customer/update-customer-detail
        """