PyVeeqo Examples
===========

Products Endpoint
-----------------

.. code-block:: python

    from py_veeqo.endpoints import Products

    # Create an instance of the Products class
    products = Products(api_key='your_api_key')

    # Fetch all products
    all_products = products.get_all_products()

    # Print the first product
    print(all_products[0])

Orders Endpoint
-----------------

.. code-block:: python

    from py_veeqo.endpoints import Orders

    # Create an instance of the Orders class
    orders = Orders(api_key='your_api_key')

    # Fetch all orders
    all_orders = orders.get_all_orders()

    # Print the first order
    print(all_orders[0])