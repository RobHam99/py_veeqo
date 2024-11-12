PyVeeqo
========
.. image:: https://readthedocs.org/projects/py-veeqo/badge/?version=latest
   :target: https://py-veeqo.readthedocs.io/en/latest/?badge=latest

A Python wrapper for the Veeqo ecommerce API.

.. note::
   This project is currently under development.

Installation
------------

To install, run the following command:

.. code-block:: bash
    $ pip install pyveeqo

Usage
-----

`PyVeeqo` can be used to extract company information as follows:

.. code-block:: python
    from py_veeqo.endpoints import Products

    pv = Products(api_key=your_veeqo_api_key)

    orders = pv.get_all_orders()

Examples
--------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   examples

Tests
-----

.. toctree::
   :maxdepth: 1
   :titlesonly:

   tests

Documentation
-------------

The code documentation can be found at `Read the Docs <https://py-veeqo.readthedocs.io/en/latest/>`_.

Contributing
------------

Interested in contributing? Check out the contributing guidelines.
Please note that this project is released with a Code of Conduct.
By contributing to this project, you agree to abide by its terms.

License
-------

`PyVeeqo` was created by Robert J. Hamilton. It is licensed under the terms
of the MIT license.

Leave a star :star2:
--------------------

.. note::
   Please star if you like this package!
