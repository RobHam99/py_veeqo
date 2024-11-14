from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Warehouses(PyVeeqo):
    """This class implements all the warehouses api calls.
    """
    _ENDPOINT_KEY = "warehouses"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("warehouses",))
    def get_all_warehouses(self, page_size: int = 12, page: int = 1) -> Result:
        """Get a list of all warehouses.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse-collection/list-all-warehouses

        Args:
            page_size (int, optional): Number of items per page. Defaults to 12.
            page (int, optional): Page number. Defaults to 1.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="POST", path_structure=("warehouses",))
    def create_a_warehouse(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Create a new warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse-collection/create-a-warehouse

        Args:
            data (Dict, optional): _description_. Defaults to None.
            json (Optional[JSONType], optional): _description_. Defaults to None.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("warehouses", "{warehouse_id}"))
    def view_warehouse_detail(self, warehouse_id: int) -> Result:
        """Get details of a specific warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse/view-warehouse-detail

        Args:
            warehouse_id (int): The id of the warehouse.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="PUT", path_structure=("warehouses", "{warehouse_id}"))    
    def update_warehouse_detail(self, warehouse_id: int, data: Dict = None) -> Result:
        """Update details of a specific warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse/update-warehouse-detail

        Args:
            warehouse_id (int): The id of the warehouse.
            data (Dict, optional): _description_. Defaults to None.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="DELETE", path_structure=("warehouses", "{warehouse_id}"))
    def delete_warehouse(self, warehouse_id: int) -> Result:
        """Delete a specific warehouse.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse/delete

        Args:
            warehouse_id (int): The id of the warehouse.
        """
        pass
