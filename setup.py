from setuptools import setup, find_packages

setup(
    name='py_veeqo',
    version='0.1.0',
    author='Robert J. Hamilton',
    author_email='hamiltonrobbie@yahoo.co.uk',
    license='MIT',
    description='A python wrapper for the Veeqo API for shipping and inventory management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    url='https://github/com/RobHam99/py_veeqo',
    install_requires=[
        'requests',
    ],
    tests_require=[
        'requests_mock',
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
)