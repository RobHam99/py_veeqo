from typing import Dict, Optional
from py_veeqo.pyveeqo import PyVeeqo
from py_veeqo.types import JSONType
from py_veeqo.models import Result


class Products(PyVeeqo):
    """This class implements all the products api calls.
    """
    _ENDPOINT_KEY = "products"

    @PyVeeqo._endpoint_builder(method="GET", path_structure=("products",))
    def get_all_products(
        self,
        since_id: int = None,
        warehouse_id: int = None,
        created_at_min: str = None,
        updated_at_min: str = None,
        page_size: int = 12,
        page: int = 1,
        query: str = None) -> Result:
        """Get a list of all products in inventory, and their corresponding
        information.
        https://developers.veeqo.com/docs#/reference/products/product-collection/list-all-products

        Args:
            since_id (int, optional): Get products since a specific id.
            Defaults to None.
            warehouse_id (int, optional): Get products from a specific warehouse.
            Defaults to None.
            created_at_min (str, optional): Get products created after a specific
            date. Defaults to None.
            updated_at_min (str, optional): Get products updated after a specific
            date. Defaults to None.
            page_size (int, optional): Number of products to return per page.
            Defaults to 12.
            page (int, optional): Page number to return. Defaults to 1.
            query (str, optional): Search query to filter products. Defaults to None.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("products", "{product_id}"))
    def get_product_detail(self, product_id: int) -> Result:
        """Get product details for a specified product id.
        https://developers.veeqo.com/docs#/reference/products/product/view-product-detail

        Args:
            product_id (str): Unique Veeqo id number for a given product.
            NOT to be confused with product SKU.

        Returns:
            Dict: All information on the specified product.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="GET", path_structure=("products", "{product_id}", "product_property_specifics"))
    def get_product_properties(self, product_id: int,
                               property_id: str) -> Result:
        """Get information about a specific property for a specific product.
        https://developers.veeqo.com/docs#/reference/products/product-properties/view-properties

        Args:
            product_id (str): Specific product id to query.
            property_id (str): Specific property id for that product.

        Returns:
            Dict: All information on the property for that product.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="POST", path_structure=("products",))
    def create_new_product(self, data: Dict = None,
                           json: Optional[JSONType] = None) -> Result:
        """Create a new product by passing information in either data or json
        format.
        https://developers.veeqo.com/docs#/reference/products/product-collection/create-a-new-product

        Args:
            data (Dict, optional): Product data in dict format.
            Defaults to None.
            json (Optional[JSONType], optional): Product data in json format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="POST", path_structure=("product_properties",))
    def create_new_property(self, data: Dict = None,
                            json: Optional[JSONType] = None) -> Result:
        """Create a new property by passing information in either data or json
        format.
        https://developers.veeqo.com/docs#/reference/products/create-properties/create-a-new-property

        Args:
            data (Dict, optional): Product data in dict format.
            Defaults to None.
            json (Optional[JSONType], optional): Product data in json format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="PUT", path_structure=("products", "{product_id}"))
    def update_product_detail(self, product_id: int,
                              data: Dict = None) -> Result:
        """Update the details of a product, specified by it's unique
        Veeqo identifier.
        https://developers.veeqo.com/docs#/reference/products/product/update-product-detail

        Args:
            product_id (int): Veeqo unique product identifier.
            data (Dict, optional): Product data in dict format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass
     
    @PyVeeqo._endpoint_builder(
        method="PUT", path_structure=("products", "{product_id}", "properties", "{property_id}"))
    def update_property_detail(self, product_id: int, property_id: int,
                               data: Dict = None) -> Result:
        """Update the details of a product, specified by it's unique
        Veeqo identifier.
        https://developers.veeqo.com/docs#/reference/products/product-properties/update-property-detail

        Args:
            product_id (int): Veeqo unique product identifier.
            property_id (int): Veeqo unique property identifier.
            data (Dict, optional): Product data in dict format.
            Defaults to None.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="DELETE", path_structure=("products", "{product_id}"))
    def delete_product(self, product_id: int) -> Result:
        """Delete a product by specifying it's unique Veeqo identifier.
        https://developers.veeqo.com/docs#/reference/products/product/delete

        Args:
            product_id (int): Unique Veeqo product identifier.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass

    @PyVeeqo._endpoint_builder(
        method="DELETE", path_structure=("products", "{product_id}", "product_property_specifics", "{property_id}"))
    def delete_product_property(self, product_id: int,
                                property_id: int) -> Result:
        """Delete a product by specifying it's unique Veeqo identifier.

        Args:
            product_id (int): Unique Veeqo product identifier.
            property_id (int): Unique Veeqo property identifier.

        Returns:
            Result: Result object containing status code, message and data.
        """
        pass
