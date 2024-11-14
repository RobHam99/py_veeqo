from typing import Dict
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.models import Result


class Company(PyVeeqo):
    """This class implements all the company api calls.
    """
    _ENDPOINT_KEY = "current_company"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("current_company",))
    def get_company(self) -> Result:
        """Get current company details
        https://developers.veeqo.com/docs#/reference/company/company/view-company-detail
        """
        pass

    @PyVeeqo._endpoint_builder(method="PUT", path_structure=("current_company",))
    def update_company_detail(self, data: Dict = None) -> Result:
        """Update the company details.
        https://developers.veeqo.com/docs#/reference/warehouses/update-company-detail

        Args:
            data (Dict, optional): Company details to update. Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass
