from typing import List, Dict
from .pyveeqo import PyVeeqo


class PurchaseOrders(PyVeeqo):
    """This class implements all the purchase orders api calls.
    """
    _ENDPOINT_KEY = "purchase_orders"

    def get_all_purchase_orders(self, **kwargs) -> List[Dict]:
        """Get a list of all purchase orders, and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/purchase-orders/purchase-order-collection/list-all-purchase-orders

        Returns:
            List[Dict]: A list of containing a dict for each purchase order.
        """
        return self.get(endpoint=self._ENDPOINT_KEY, params=kwargs).data
