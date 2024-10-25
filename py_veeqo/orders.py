from typing import List, Dict
from py_veeqo.pyveeqo import PyVeeqo


class Orders(PyVeeqo):
    """This class implements all the orders api calls.
    """
    _ENDPOINT_KEY = "orders"

    def get_all_orders(self, **kwargs) -> List[Dict]:
        """Get a list of all historical orders and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/orders/order-collection/list-all-orders
        Returns:
            List[Dict]: A list of containing a dict for each order.
        """
        return self.get(endpoint=self._ENDPOINT_KEY, params=kwargs).data

    def get_order_detail(self, order_id: int) -> Dict:
        """Get order details for a specified order id.
        https://developers.veeqo.com/docs#/reference/orders/order/view-an-order-detail

        Args:
            order_id (str): Unique Veeqo id number for a given order.

        Returns:
            Dict: All information on the specified order.
        """
        endpoint = self._ENDPOINT_KEY + "/" + order_id
        return self.get(endpoint=endpoint).data
