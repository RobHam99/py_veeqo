# PyVeeqo
[![Documentation Status](https://readthedocs.org/projects/py-veeqo/badge/?version=latest)](https://py-veeqo.readthedocs.io/en/latest/?badge=latest) [![Percentage of issues still open](http://isitmaintained.com/badge/open/RobHam99/py_veeqo.svg)](http://isitmaintained.com/project/RobHam99/py_veeqo "Percentage of issues still open") [![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RobHam99/py_veeqo.svg)](http://isitmaintained.com/project/RobHam99/py_veeqo "Average time to resolve an issue")

A Python wrapper for the Veeqo ecommerce API.

> [!NOTE]  
> This project is currently under development. 

## Installation

```bash
$ pip install pyveeqo
```

## Usage

`PyVeeqo` can be used to extract company information as follows:

```python
from py_veeqo.endpoints import Products

pv = Products(api_key=your_veeqo_api_key)

orders = pv.get_all_orders()
```

You can verify whether the installation was successful by running the following command in your terminal:

```bash
$ python -c "import py_veeqo; print(py_veeqo.__version__)"
```

Alternatively, create and run a python file containing the same code:

```python
import py_veeqo

print(py_veeqo.__version__)
```

## Documentation

The PyVeeqo documentation can be found [here](https://py-veeqo.readthedocs.io/en/latest/). The documentation contains information about each Veeqo endpoint and the various queries the user can make. 

### Examples

The documentation also contains some example code to help the user better understand the possible operations in the Veeqo API. These examples can be found [here](https://py-veeqo.readthedocs.io/en/latest/examples.html).

## Tests

Tests can be run using the following command:

```bash
$ python -m unittest -v tests.test_pyveeqo.TestPyVeeqo
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`PyVeeqo` was created by Robert J. Hamilton. It is licensed under the terms
of the MIT license.

## Leave a star :star2:
> [!NOTE]
> Please star if you like this package!