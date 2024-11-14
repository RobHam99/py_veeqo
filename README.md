# PyVeeqo
[![Documentation Status](https://readthedocs.org/projects/py-veeqo/badge/?version=latest)](https://py-veeqo.readthedocs.io/en/latest/?badge=latest) [![Percentage of issues still open](http://isitmaintained.com/badge/open/RobHam99/py_veeqo.svg)](http://isitmaintained.com/project/RobHam99/py_veeqo "Percentage of issues still open") [![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RobHam99/py_veeqo.svg)](http://isitmaintained.com/project/RobHam99/py_veeqo "Average time to resolve an issue")

> [!NOTE]  
> This project is currently in Alpha testing. 

PyVeeqo is a python wrapper for the [Veeqo ecommerce API](https://developers.veeqo.com/docs). This is a low-level and lightweight wrapper, designed with two main objectives:

1. To faciliate easier access to the Veeqo API, for entry level users, who only know basic Python.
2. To enable faster software development for businesses already utilising the Veeqo API.

The Veeqo API currently has 15 different accessible endpoints ranging from `Products` to `Bulk Tagging`, with each endpoint containing multiple different functions, such as the ability to product a list of all products, or bulk delete order tags. PyVeeqo contains robust and easy-to-use implementations for all 15 endpoints.

**Please consider giving this repository a star if you like it!** It would be nice to know someone has found it useful other than myself.

## Installation

```bash
$ pip install pyveeqo
```

## Usage

`PyVeeqo` can be used to extract company information as follows:

```python
from py_veeqo.endpoints.products import Products
from py_veeqo.endpoints.customers import Customers
from py_veeqo.endpoints.orders import Orders
# Try out some other endpoints such as StockEntries!

orders = Orders(api_key=your_veeqo_api_key)

all_orders = orders.get_all_orders()
```

## Documentation

The PyVeeqo documentation can be found [here](https://py-veeqo.readthedocs.io/en/latest/). The documentation contains information about each Veeqo endpoint and the various queries the user can make. 

### Examples

The documentation also contains some example code to help the user better understand the possible operations in the Veeqo API. These examples can be found [here](https://py-veeqo.readthedocs.io/en/latest/examples.html).

### API

Full details of each of the available endpoints and their respective functions can be found [here](https://py-veeqo.readthedocs.io/en/latest/api.html)

## Tests

Tests can be run using the following command:

```bash
$ python -m unittest -v tests/test_pyveeqo.py
```

## Contributing

Please get in touch if you would like to contribute, or wish to give feedback on the codebase. I'm always open to learning and collaborating!

## License

`PyVeeqo` was created by Robert J. Hamilton. It is licensed under the terms
of the MIT license.

## Leave a star :star2:
> [!NOTE]
> Please star if you like this package!