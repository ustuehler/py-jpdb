# py-jpdb

A Python 3 package providing a _very_ limited and experimental client for [jpdb](https://jpdb.io/), a powerful Japanese dictionary and all-in-one learning system.

## Features

- Validation of login credentials (`JPDB.login`)
- Get the total number of due items (`JPDB.due_items`)
- Export the entire review history (`JPDB.reviews`)

## Installation with pip

```
pip install git+https://github.com/ustuehler/py-jpdb
```

## Usage

You need an active user account on jpdb in order to use this client, and you
must [register](https://jpdb.io/register) with username and password instead of
using the "Sign in with Google" option.

Example:

```python
import os
from jpdb import JPDB

# Get the username and password from somewhere (NB: OAuth is not supported)
username = os.environ['JPDB_USERNAME']
password = os.environ['JPDB_PASSWORD']

# Create a jpdb client instance
jpdb = JPDB(username, password)

# Ensure that credentials are valid (optional)
jpdb.login()

# Do something useful
print(jpdb.due_items)
```

For other possible usages, please see the implementation of the `JPDB` class in
[jpdb/\_\_init\_\_.py](jpdb/__init__.py).

## Changes

All notable changes to this project will be documented in the file
[CHANGELOG.md](CHANGELOG.md).

## Contributing

See the [Contributing Guide](CONTRIBUTING.md) for instructions on how to set up
a local environment for development and testing.

## License

[MIT](LICENSE)
