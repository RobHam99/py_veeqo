User Guide
===========

The main user interfact for interacting with PyVeeqo is the `endpoints` module. To get started we will use an example from the `products` endpoint:

.. code-block:: python

    from py_veeqo.endpoints import Products

    # Create an instance of the Products class
    products = Products(api_key='your_api_key')

    # Fetch all products
    all_products = products.get_all_products()

    # Print the first product
    print(all_products[0])