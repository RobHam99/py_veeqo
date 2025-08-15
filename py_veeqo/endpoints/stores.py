from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Stores(PyVeeqo):
    """This class implements all the stores (channels) api calls.
    """
    _ENDPOINT_KEY = "channels"

    @PyVeeqo._endpoint_builder(method="GET")
    def get_all_stores(self, page_size: int = 12, page: int = 1) -> Result:
        """Get a list of all stores (channels).
        https://developers.veeqo.com/docs#/reference/customers/customer/list-all-stores

        Args:
            page_size (int, optional): Number of items per page. Defaults to 12.
            page (int, optional): Page number. Defaults to
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="POST")
    def create_a_store(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Create a new store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store-collection/create-a-store

        Args:
            data (Dict, optional): _description_. Defaults to None.
            json (Optional[JSONType], optional): _description_. Defaults to None.
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="GET")
    def view_store_detail(self, channel_id: int) -> Result:
        """Get details of a specific store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store/view-store-detail

        Args:
            channel_id (int): The id of the store (channel).
        """
        return self._ENDPOINT_KEY + f"/{channel_id}"

    @PyVeeqo._endpoint_builder(method="PUT")
    def update_store_detail(self, channel_id: int, data: Dict = None) -> Result:
        """Update details of a specific store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store/update-store-detail
        """
        return self._ENDPOINT_KEY + f"/{channel_id}"
        

    @PyVeeqo._endpoint_builder(method="DELETE")
    def delete_store(self, channel_id: int) -> Result:
        """Delete a specific store (channel).
        https://developers.veeqo.com/docs#/reference/stores/store/delete

        Args:
            channel_id (int): The id of the store (channel).
        """
        return self._ENDPOINT_KEY + f"/{channel_id}"
