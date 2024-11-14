from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class BulkTagging(PyVeeqo):
    """This class implements all the bulk_tagging api calls.
    """
    _ENDPOINT_KEY = "bulk_tagging"

    @PyVeeqo._endpoint_builder(method="POST", path_structure=("bulk_tagging",))
    def tag_orders(self, data: Dict = None,
                   json: Optional[JSONType] = None) -> Result:
        """Bulk tag orders.
        https://developers.veeqo.com/docs#/reference/bulk-tagging/bulk-tagging/tagging-orders

        Args:
            data (Dict): The data to be sent to the endpoint.
            json (Optional[JSONType]): The json data to be sent to the
            endpoint.
        """
        pass

    @PyVeeqo._endpoint_builder(method="POST", path_structure=("bulk_tagging",))
    def tag_products(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Bulk tag products.
        https://developers.veeqo.com/docs#/reference/bulk-tagging/bulk-tagging/tagging-products

        Args:
            data (Dict): The data to be sent to the endpoint.
            json (Optional[JSONType]): The json data to be sent to the
            endpoint.
        """
        pass

    @PyVeeqo._endpoint_builder(method="DELETE", path_structure=("bulk_tagging",))
    def untagging_orders(self, data: Dict = None) -> Result:
        """Bulk untagging orders.
        https://developers.veeqo.com/docs#/reference/bulk-tagging/bulk-tagging/untagging-orders

        Args:
            data (Dict): The data to be sent to the endpoint.
        """
        pass
