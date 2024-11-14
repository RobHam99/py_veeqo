from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Shipments(PyVeeqo):
    """This class implements all the shipments api calls.
    """
    _ENDPOINT_KEY = "shipments"

    @PyVeeqo._endpoint_builder(method="POST", path_structure=("shipments",))
    def create_shipment(self, data: Dict = None, 
                        json: Optional[JSONType] = None) -> Result:
        """Create a new shipment.
        https://developers.veeqo.com/docs#/reference/shipments/shipment-collection/create-a-shipment

        Args:
            data (Dict, optional): The data to be sent to the endpoint. Defaults to None.
            json (JSONType, optional): The json data to be sent to the endpoint. Defaults to None.
        """
        pass

    @PyVeeqo._endpoint_builder(method="DELETE", path_structure=("shipments", "{shipment_id}"))
    def delete_shipment(self, shipment_id: int) -> Result:
        """Delete a specific shipment.
        https://developers.veeqo.com/docs#/reference/shipments/shipment/delete

        Args:
            shipment_id (int): The id of the shipment to be deleted.
        """
        pass
