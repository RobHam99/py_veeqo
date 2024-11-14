from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.models import Result


class PurchaseOrders(PyVeeqo):
    """This class implements all the purchase orders api calls.
    """
    _ENDPOINT_KEY = "purchase_orders"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("purchase_orders",))
    def get_all_purchase_orders(
        self,
        page_size: int = 12,
        page: int = 1,
        show_complete: bool = False) -> Result:
        """Get a list of all purchase orders, and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/purchase-orders/purchase-order-collection/list-all-purchase-orders

        Args:
            page_size (int, optional): The number of purchase orders to return. Defaults to 12.
            page (int, optional): The page number to return. Defaults to 1.
            show_complete (bool, optional): Whether to show completed purchase orders. Defaults to False.
        """
        pass
