from typing import List, Dict
from py_veeqo.pyveeqo import PyVeeqo


class Products(PyVeeqo):
    """This class implements all the products api calls.
    """
    _ENDPOINT_KEY = "products"

    def get_all_products(self, **kwargs) -> List[Dict]:
        """Get a list of all products in inventory, and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/products/product-collection/list-all-products

        Returns:
            List[Dict]: A list of containing a dict for each product.
        """
        return self.get(endpoint=self._ENDPOINT_KEY, params=kwargs).data

    def get_product_detail(self, product_id: str) -> Dict:
        """Get product details for a specified product id.
        https://developers.veeqo.com/docs#/reference/products/product/view-product-detail

        Args:
            product_id (str): Unique Veeqo id number for a given product.
            NOT to be confused with product SKU.

        Returns:
            Dict: All information on the specified product.
        """
        endpoint = "{}/{}".format(self._ENDPOINT_KEY, product_id)
        return self.get(endpoint=endpoint).data

    def get_product_properties(self, product_id: str,
                               property_id: str) -> Dict:
        """Get information about a specific property for a specific product.
        https://developers.veeqo.com/docs#/reference/products/product-properties/view-properties

        Args:
            product_id (str): Specific product id to query.
            property_id (str): Specific property id for that product.

        Returns:
            Dict: All information on the property for that product.
        """
        endpoint = "{}/{}/product_property_specifics/{}".format(
            self._ENDPOINT_KEY,
            product_id,
            property_id
            )
        return self.get(endpoint=endpoint).data
