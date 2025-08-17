from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Warehouses(PyVeeqo):
    """This class implements all the warehouses api calls.
    """
    _ENDPOINT_KEY = "warehouses"

    @PyVeeqo._endpoint_builder(method="GET")
    def get_all_warehouses(self, page_size: int = 12, page: int = 1, external_id: str = None) -> Result:
        """Get a list of all warehouses.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse-collection/list-all-warehouses

        Args:
            page_size (int, optional): Number of items per page. Defaults to 12.
            page (int, optional): Page number. Defaults to 1.
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="POST")
    def create_a_warehouse(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Create a new warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse-collection/create-a-warehouse

        Args:
            data (Dict, optional): _description_. Defaults to None.
            json (Optional[JSONType], optional): _description_. Defaults to None.
        """
        return self._ENDPOINT_KEY

    @PyVeeqo._endpoint_builder(method="GET")
    def view_warehouse_detail(self, warehouse_id: int) -> Result:
        """Get details of a specific warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse/view-warehouse-detail

        Args:
            warehouse_id (int): The id of the warehouse.
        """
        return self._ENDPOINT_KEY + f"/{warehouse_id}"

    @PyVeeqo._endpoint_builder(method="PUT")    
    def update_warehouse_detail(self, warehouse_id: int, data: Dict = None) -> Result:
        """Update details of a specific warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse/update-warehouse-detail

        Args:
            warehouse_id (int): The id of the warehouse.
            data (Dict, optional): _description_. Defaults to None.
        """
        return self._ENDPOINT_KEY + f"/{warehouse_id}"

    @PyVeeqo._endpoint_builder(method="DELETE")
    def delete_warehouse(self, warehouse_id: int) -> Result:
        """Delete a specific warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse/delete

        Args:
            warehouse_id (int): The id of the warehouse.
        """
        return self._ENDPOINT_KEY + f"/{warehouse_id}"
