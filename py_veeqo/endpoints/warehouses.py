from typing import List, Dict, Optional
from urllib.parse import urljoin
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Warehouses(PyVeeqo):
    """This class implements all the warehouses api calls.
    """
    _ENDPOINT_KEY = "warehouses"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("warehouses",))
    def get_all_warehouses(self, **kwargs) -> Result:
        """Get a list of all warehouses.
        https://developers.veeqo.com/docs#/reference/warehouses/warehouse-collection/list-all-warehouses
        """

    @PyVeeqo._endpoint_builder(
            method="POST",
            path_structure=("warehouses",))
    def create_a_warehouse(self, data: Dict = None, 
                           json: Optional[JSONType] = None) -> Result:
        """Create a new warehouse.
        https://developers.veeqo.com/docs
        """

    @PyVeeqo._endpoint_builder(
            method="GET",
            path_structure=("warehouses", "{warehouse_id}"))
    def view_warehouse_detail(self, warehouse_id: int) -> Result:
        """Get details of a specific warehouse.
        https://developers.veeqo.com/docs
        """


    @PyVeeqo._endpoint_builder(
            method="PUT",
            path_structure=("warehouses", "{warehouse_id}"))    
    def update_warehouse_detail(self, warehouse_id: int, 
                                data: Dict = None) -> Result:
        """Update details of a specific warehouse.
        https://developers.veeqo.com/docs
        """
    

    @PyVeeqo._endpoint_builder(
            method="DELETE",
            path_structure=("warehouses", "{warehouse_id}"))
    def delete_warehouse(self, warehouse_id: int) -> Result:
        """Delete a specific warehouse.
        https://developers.veeqo.com/docs
        """

