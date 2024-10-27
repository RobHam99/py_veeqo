from typing import Dict
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.models import Result


class StockEntries(PyVeeqo):
    """This class implements all the stock entries api calls.
    """
    _ENDPOINT_KEY = "sellables"

    def get_stock_entry(self, sellable_id: int,
                        warehouse_id: int) -> Dict:
        """Show a specific stock entry for a specific warehouse.
        https://developers.veeqo.com/docs#/reference/stock-entries/stock-entry/show-a-stock-entry

        Args:
            sellable_id (int): Stock entry id.
            warehouse_id (int): Warehouse id.

        Returns:
            Dict: Stock entry data.
        """
        endpoint = urljoin(self._ENDPOINT_KEY + "/", sellable_id)
        endpoint = urljoin(
            endpoint + "/warehouses/",
            warehouse_id + "/stock_entry"
            )
        return self.get(endpoint=endpoint).data

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
        endpoint = urljoin(self._ENDPOINT_KEY + "/", sellable_id)
        endpoint = urljoin(
            endpoint + "/warehouses/",
            warehouse_id + "/stock_entry"
            )
        return self.put(endpoint=endpoint, data=data)
