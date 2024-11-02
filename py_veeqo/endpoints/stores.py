from typing import List, Dict, Optional
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Stores(PyVeeqo):
    """This class implements all the stores (channels) api calls.
    """
    _ENDPOINT_KEY = "channels"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("channels",))
    def get_all_stores(self, **kwargs) -> Result:
        """Get a list of all stores (channels).
        https://developers.veeqo.com/docs#/reference/customers/customer/list-all-stores
        """

    @PyVeeqo._endpoint_builder(
            method="POST",
            path_structure=("channels",))
    def create_a_store(self, data: Dict = None, 
                       json: Optional[JSONType] = None) -> Result:
        """Create a new store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store-collection/create-a-store
        """

    @PyVeeqo._endpoint_builder(
            method="GET",
            path_structure=("channels", "{channel_id}"))
    def view_store_detail(self, channel_id: int) -> Result:
        """Get details of a specific store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store/view-store-detail
        """

    @PyVeeqo._endpoint_builder(
            method="PUT",
            path_structure=("channels", "{channel_id}"))
    def update_store_detail(self, channel_id: int, 
                            data: Dict = None) -> Result:
        """Update details of a specific store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store/update-store-detail
        """

    @PyVeeqo._endpoint_builder(
            method="DELETE",
            path_structure=("channels", "{channel_id}"))
    def delete_store(self, channel_id: int) -> Result:
        """Delete a specific store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store/delete
        """
