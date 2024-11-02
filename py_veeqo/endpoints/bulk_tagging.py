from typing import List, Dict, Optional
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result

class BulkTagging(PyVeeqo):
    """This class implements all the bulk_tagging api calls.
    """
    _ENDPOINT_KEY = "bulk_tagging"

    @PyVeeqo._endpoint_builder(method="POST", path_structure=("bulk_tagging",))
    def tagging_orders(self, data: Dict = None, 
                     json: Optional[JSONType] = None) -> Result:
        """Bulk tagging orders.
        https://developers.veeqo.com/docs#/reference/bulk-tagging/bulk-tagging/tagging-orders
        """

    @PyVeeqo._endpoint_builder(method="POST", path_structure=("bulk_tagging",))
    def tagging_products(self, data: Dict = None, 
                     json: Optional[JSONType] = None) -> Result:
        """Bulk tagging products.
        https://developers.veeqo.com/docs#/reference/bulk-tagging/bulk-tagging/tagging-products
        """

    @PyVeeqo._endpoint_builder(method="DELETE", path_structure=("bulk_tagging",))
    def untagging_orders(self, data: Dict = None) -> Result:
        """Bulk untagging orders.
        https://developers.veeqo.com/docs#/reference/bulk-tagging/bulk-tagging/untagging-orders
        """