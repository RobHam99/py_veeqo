from typing import List, Dict
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.models import Result


class PurchaseOrders(PyVeeqo):
    """This class implements all the purchase orders api calls.
    """
    _ENDPOINT_KEY = "purchase_orders"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("purchase_orders",))
    def get_all_purchase_orders(self, **kwargs) -> Result:
        """Get a list of all purchase orders, and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/purchase-orders/purchase-order-collection/list-all-purchase-orders

        Returns:
            List[Dict]: A list of containing a dict for each purchase order.
        """
