from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Orders(PyVeeqo):
    """This class implements all the orders api calls.
    """
    _ENDPOINT_KEY = "orders"

    @PyVeeqo._endpoint_builder(method="GET")
    def get_all_orders(
        self,
        since_id: int = None,
        created_at_min: str = None,
        updated_at_min: str = None,
        page_size: int = 12,
        page: int = 1,
        query: str = None,
        status: str = None,
        tags: str = None,
        allocated_at: int = None) -> Result:
        """Get a list of all historical orders and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/orders/order-collection/list-all-orders

        Args:
            since_id (int, optional): Return orders with id greater than this
            value. Defaults to None.
            created_at_min (str, optional): Return orders created after this
            date. Defaults to None.
            updated_at_min (str, optional): Return orders updated after this
            date. Defaults to None.
            page_size (int, optional): Number of orders per page. Defaults to 12.
            page (int, optional): Page number. Defaults to 1.
            query (str, optional): Search query. Defaults to None.
            status (str, optional): Order status. Defaults to None.
            tags (str, optional): Order tags. Defaults to None.
            allocated_at (int, optional): Return orders allocated at this time.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="GET")
    def get_order_detail(self, order_id: int) -> Result:
        """Get order details for a specified order id.
        https://developers.veeqo.com/docs#/reference/orders/order/view-an-order-detail

        Args:
            order_id (str): Unique Veeqo id number for a given order.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._ENDPOINT_KEY + f"/{order_id}"

    @PyVeeqo._endpoint_builder(method="GET")
    def get_order_returns(self, order_id: int) -> Result:
        """Show returns for a given order.
        https://developers.veeqo.com/docs#/reference/returns/returns/show-returns-on-order

        Args:
            order_id (str): Unique Veeqo id number for a given order.

        Returns:
            Result: Result object containing status code, message and data.
        """
        return self._ENDPOINT_KEY + f"/{order_id}/returns"

    @PyVeeqo._endpoint_builder(method="POST")
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
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="POST")
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
        return self._ENDPOINT_KEY + f"/{order_id}/notes"

    @PyVeeqo._endpoint_builder(method="POST")
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
        return self._ENDPOINT_KEY + f"/{order_id}/allocations"

    @PyVeeqo._endpoint_builder(method="PUT")
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
        return self._ENDPOINT_KEY + f"/{order_id}"

    @PyVeeqo._endpoint_builder(method="PUT")
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
        return self._ENDPOINT_KEY + f"/{order_id}/allocations/{allocation_id}"

    @PyVeeqo._endpoint_builder(method="DELETE")
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
        return self._ENDPOINT_KEY + f"/{order_id}/allocations/{allocation_id}"


    @PyVeeqo._endpoint_builder(method="PUT")
    def update_allocation_package(self, allocation_id: int,  data: Dict = None,
                         json: Optional[JSONType] = None) -> Result:
        """create a package for a specific sales-order allocation, specified by the unique Veeqo allocation_id.
        https://developers.veeqo.com/api/operations/update-allocation-package/

        Args:
            allocation_id (int): Veeqo unique allocation identifier.
            allocation_package: obj

        Returns:
            Result: Result object containing status code, message and data of allocation_package details.
        """
        return self._ENDPOINT_KEY + f"/allocations/{allocation_id}/allocation_package"