from py_veeqo.products import Products

# Test Code
api = Products()

# Correctly calling the build_endpoint method
path_structure = ["products", "{product_id}", "product_property_specifics", "{property_id}"]
path_params = {
    "product_id": 1234,
    "property_id": 5678
}

# Generate the URL using the path structure and parameters
url = Products.build_endpoint(path_structure, path_params=path_params)

print(url)  # Outputs: https: