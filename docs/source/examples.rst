PyVeeqo Examples
===========

Products
--------

Get a list of all products in our Veeqo account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from py_veeqo.endpoints import Products

    # Create an instance of the Products class
    products = Products(api_key='your_api_key')

    # Fetch all products
    all_products = products.get_all_products()

    # Print the first product
    print(all_products[0])

Get a specific product by ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from py_veeqo.endpoints import Products

    # Create an instance of the Products class
    products = Products(api_key='your_api_key')

    # Fetch a specific product by ID
    product = products.get_product_detail(product_id=your_product_id)

    # Print the product
    print(product)

Orders
------

Get a list of all orders in our Veeqo account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from py_veeqo.endpoints import Orders

    # Create an instance of the Orders class
    orders = Orders(api_key='your_api_key')

    # Fetch all orders
    all_orders = orders.get_all_orders()

    # Print the first order
    print(all_orders[0])

Get a specific order by ID
~~~~~~~~~~~~~~~~~~~~~~~~~~  

.. code-block:: python

    from py_veeqo.endpoints import Orders

    # Create an instance of the Orders class
    orders = Orders(api_key='your_api_key')

    # Fetch a specific order by ID
    order = orders.get_order_detail(order_id=your_order_id)

    # Print the order
    print(order)

Customers
---------

Update a Customer's details
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from py_veeqo.endpoints import Customers

    # Create an instance of the Customers class
    customers = Customers(api_key='your_api_key')

    # Update a customer's details
    updated_customer = customers.update_customer_detail(customer_id=your_customer_id, data={'first_name': 'John', 'last_name': 'Doe'})