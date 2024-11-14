from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Suppliers(PyVeeqo):
    """This class implements all the suppliers api calls.
    """
    _ENDPOINT_KEY = "suppliers"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("suppliers",))
    def list_all_suppliers(self, page_size: int = 12, page: int = 1) -> Result:
        """Get a list of all suppliers.
        https://developers.veeqo.com/docs#/reference/suppliers/supplier-collection/list-all-suppliers

        Args:
            page_size (int, optional): Number of suppliers per page. Defaults to 12.
            page (int, optional): Page number. Defaults to 1.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="POST", path_structure=("suppliers", "{supplier_id}"))
    def create_new_supplier(self, data: Dict = None, json: Optional[JSONType] = None) -> Result:
        """Create a new supplier.
        https://developers.veeqo.com/docs#/reference/suppliers/supplier-collection/create-a-new-supplier

        Args:
            data (Dict, optional): Supplier data. Defaults to None.
            json (Optional[JSONType], optional): Supplier data. Defaults to None.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("suppliers", "{supplier_id}"))
    def view_supplier_detail(self, supplier_id: int) -> Result:
        """Get details of a specific supplier.
        https://developers.veeqo.com/docs#/reference/suppliers/supplier/view-a-supplier-detail

        Args:
            supplier_id (int): Supplier id.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="PUT", path_structure=("suppliers", "{supplier_id}"))
    def update_supplier_detail(self, supplier_id: int, 
                               data: Dict = None) -> Result:
        """Update details of a specific supplier.
        https://developers.veeqo.com/docs#/reference/suppliers/supplier/update-supplier-detail

        Args:
            supplier_id (int): Supplier id.
            data (Dict, optional): Supplier data. Defaults to None
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="DELETE", path_structure=("suppliers", "{supplier_id}"))
    def delete_supplier(self, supplier_id: int) -> Result:
        """Delete a specific supplier.
        https://developers.veeqo.com/docs#/reference/suppliers/supplier/delete

        Args:
            supplier_id (int): Supplier id.
        """
        pass
