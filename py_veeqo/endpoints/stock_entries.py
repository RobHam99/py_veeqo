from typing import Dict
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.models import Result


class StockEntries(PyVeeqo):
    """This class implements all the stock entries api calls.
    """
    _ENDPOINT_KEY = "sellables"

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("sellables", "{sellable_id}", "warehouses", "{warehouse_id}", "stock_entry"))
    def get_stock_entry(self, sellable_id: int,
                        warehouse_id: int) -> Result:
        """Show a specific stock entry for a specific warehouse.
        https://developers.veeqo.com/docs#/reference/stock-entries/stock-entry/show-a-stock-entry

        Args:
            sellable_id (int): Stock entry id.
            warehouse_id (int): Warehouse id.

        Returns:
            Dict: Stock entry data.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="PUT", path_structure=("sellables", "{sellable_id}", "warehouses", "{warehouse_id}", "stock_entry"))
    def update_stock_entry(self, sellable_id: int,
                           warehouse_id: int, data: Dict = None) -> Result:
        """Update a specific stock entry for a specific warehouse.
        https://developers.veeqo.com/docs#/reference/stock-entries/stock-entry/update-a-stock-entry

        Args:
            sellable_id (int): Stock entry id.
            warehouse_id (int): Warehouse id.

        Returns:
            Dict: Stock entry data.
        """
        pass
