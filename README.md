# PyVeeqo
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

## Examples

## Tests

## Documentation
The code documentation can be found at 

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`pycounts` was created by Tomas Beuzen. It is licensed under the terms
of the MIT license.

## Leave a star :star2:
> [!NOTE]
> Please star if you like this package!