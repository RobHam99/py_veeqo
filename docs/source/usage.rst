User Guide
===========


The main user interfact for interacting with PyVeeqo is the ``endpoints`` module. The `Veeqo API <https://developers.veeqo.com/docs>`_ contains a number (currently 15) of `endpoints <https://py-veeqo.readthedocs.io/en/latest/api.html>`_, which developers can leverage to access data from different areas of their business.

To get started we will use an example from the ``products`` endpoint:

.. code-block:: python

    from py_veeqo.endpoints import Products

    # Create an instance of the Products class
    products = Products(api_key='your_api_key')

    # Fetch all products
    all_products = products.get_all_products()

    # Print the first product
    print(all_products[0])

First we import the ``Products`` class from the ``endpoints`` module. We then create an instance of the ``Products`` class, passing in our Veeqo API key. We then call the ``get_all_products`` method to fetch all products from the Veeqo API and store them in the ``all_products`` variable. Finally, we print the first product in the list.

This is just a simple example to get you started. The PyVeeqo library provides a number of other endpoints and methods that you can use to interact with the Veeqo API. For more information, please refer to the `API Reference <https://py-veeqo.readthedocs.io/en/latest/api.html>`_.