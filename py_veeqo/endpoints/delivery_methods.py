from typing import List, Dict, Optional
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class DeliveryMethods(PyVeeqo):
    """This class implements all the delivery methods api calls.
    """
    _ENDPOINT_KEY = "delivery_methods"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("delivery_methods",))
    def get_all_delivery_methods(self, **kwargs) -> Result:
        """Get a list of all delivery methods.
        https://developers.veeqo.com/docs#/reference/stores/store/list-all-delivery-methods
        """

    @PyVeeqo._endpoint_builder(
            method="POST",
            path_structure=("delivery_methods",))
    def create_a_delivery_method(self, data: Dict = None, 
                                 json: Optional[JSONType] = None) -> Result:
        """Create a new delivery method.
        https://developers.veeqo.com/docs#/reference/delivery-methods/delivery-methods-collection/create-a-delivery-method
        """

    @PyVeeqo._endpoint_builder(
            method="GET",
            path_structure=("delivery_methods", "{delivery_method_id}"))
    def view_delivery_method_detail(self, delivery_method_id: int) -> Result:
        """Get details of a specific delivery method.
        https://developers.veeqo.com/docs#/reference/delivery-methods/delivery-method/view-delivery-method-detail
        """

    @PyVeeqo._endpoint_builder(
            method="PUT",
            path_structure=("delivery_methods", "{delivery_method_id}"))
    def update_delivery_method_detail(self, delivery_method_id: int, 
                                     data: Dict = None) -> Result:
        """Update details of a specific delivery method.
        https://developers.veeqo.com/docs#/reference/delivery-methods/delivery-method/update-delivery-method-detail
        """

    @PyVeeqo._endpoint_builder(
            method="DELETE",
            path_structure=("delivery_methods", "{delivery_method_id}"))
    def delete_delivery_method(self, delivery_method_id: int) -> Result:
        """Delete a specific delivery method.
        https://developers.veeqo.com/docs#/reference/delivery-methods/delivery-method/delete
        """
