from typing import List, Dict, Optional
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


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
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        return self.get(endpoint=endpoint).data

    def get_order_returns(self, order_id: int) -> Dict:
        """Show returns for a given order.
        https://developers.veeqo.com/docs#/reference/returns/returns/show-returns-on-order

        Returns:
            List[Dict]: A list of containing a dict for each purchase order.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        endpoint = urljoin(endpoint + "/", "returns")
        return self.get(endpoint=endpoint).data

    def create_new_order(self, data: Dict = None,
                         json: Optional[JSONType] = None) -> Result:
        """Create a new order by passing information in either data or json
        format.
        https://developers.veeqo.com/docs#/reference/orders/order-collection/create-a-new-order

        Args:
            data (Dict, optional): Order data in dict format.
            Defaults to None.
            json (Optional[JSONType], optional): Order data in json format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self.post(
            endpoint=self._ENDPOINT_KEY,
            data=data,
            json=json
            )

    def create_new_order_note(self, order_id: int, data: Dict = None,
                              json: Optional[JSONType] = None) -> Result:
        """Create a new order note by passing information in either data or
        json format.
        https://developers.veeqo.com/docs#/reference/orders/order-notes/create-a-new-order-note

        Args:
            order_id (int): Veeqo unique order identifier.
            data (Dict, optional): Order data in dict format.
            Defaults to None.
            json (Optional[JSONType], optional): Order data in json format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        endpoint = urljoin(endpoint + "/", "notes")
        return self.post(
            endpoint=self._ENDPOINT_KEY,
            data=data,
            json=json
            )

    def create_new_allocation(self, order_id: int, data: Dict = None,
                              json: Optional[JSONType] = None) -> Result:
        """Allocate new stock to an order by passing information in either
        data or json format.
        https://developers.veeqo.com/docs#/reference/allocations/allocation-collection/create-a-new-allocation

        Args:
            order_id (int): Veeqo unique order identifier.
            data (Dict, optional): Order data in dict format.
            Defaults to None.
            json (Optional[JSONType], optional): Order data in json format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        endpoint = urljoin(endpoint + "/", "allocations")
        return self.post(
            endpoint=self._ENDPOINT_KEY,
            data=data,
            json=json
            )

    def update_order_detail(self, order_id: int, data: Dict = None) -> Result:
        """Update the details of an order, specified by it's unique
        Veeqo identifier.
        https://developers.veeqo.com/docs#/reference/orders/order/update-order-detail

        Args:
            order_id (int): Veeqo unique order identifier.
            data (Dict, optional): Order data in dict format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        return self.put(
            endpoint=endpoint,
            data=data
            )

    def update_allocation_detail(self, order_id: int, allocation_id: int,
                                 data: Dict = None) -> Result:
        """Update the details of an order allocation, specified by the unique
        Veeqo identifiers for the order and specific allocation.
        https://developers.veeqo.com/docs#/reference/allocations/allocation/update-allocation-detail
        Args:
            order_id (int): Veeqo unique order identifier.
            allocation_id (int): Veeqo unique allocation identifier.
            data (Dict, optional): Order data in dict format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        endpoint = urljoin(endpoint + "/allocations/", allocation_id)
        return self.put(
            endpoint=endpoint,
            data=data
            )

    def delete_allocation(self, order_id: int, allocation_id: int) -> Result:
        """Delete a specific order allocation, specified by the unique
        Veeqo identifiers for the order and specific allocation.
        https://developers.veeqo.com/docs#/reference/allocations/allocation/delete

        Args:
            order_id (int): Veeqo unique order identifier.
            allocation_id (int): Veeqo unique allocation identifier.

        Returns:
            Result: Result object containing status code, message and data.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", order_id)
        endpoint = urljoin(endpoint + "/allocations/", allocation_id)
        return self.delete(endpoint=endpoint)
