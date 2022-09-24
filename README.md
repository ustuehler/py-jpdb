# py-jpdb
An Python 3 package providing an experimental client for the [jpdb](https://jpdb.io/) service.

## Dependencies

### Development

- [Python 3](https://docs.python.org/3/)

Optionally:

- [direnv](https://direnv.net/)

### Runtime

- [Python 3](https://docs.python.org/3/)
- [Active jpdb account](https://jpdb.io/login)

## Installation

Put the following line in `requirements.txt` or pass it as an argument to [pip](https://pip.pypa.io/en/stable/)'s `install` command:

```
git+ssh://git@github.com/ustuehler/py-jpdb@main
```

However, you _should_ specify the [latest release](https://github.com/ustuehler/py-jpdb/releases/latest) version instead of `main` and upgrade manually as needed.

## Usage

```python
from jpdb import JPDB
import os

username = os.environ['JPDB_USERNAME']
password = os.environ['JPDB_PASSWORD']

jpdb = JPDB(username, password)

# Ensure that credentials are valid (optional)
jpdb.login()

# Do something useful, for example:
print(jpdb.due_items)
```

## Features

- Validation of login credentials (username & password)
- Get the total number of due items (vocabulary and Kanji cards combined)

## Roadmap

- Experimental functionality implemented by scraping the web interface
- Official API client once jpdb publishes their API documentation

## Development

To start an interactive Python interpreter with the [jpdb](src/jpdb) package
already imported:

```bash
python3 -m venv .venv
source ./.venv/bin/activate

export PYTHONPATH="$PWD/src"
export PYTHONSTARTUP="$PWD/.pythonrc"

python
```

## Testing

To execute all unit and integration tests:

```bash
python3 -m venv .venv
source ./.venv/bin/activate

export PYTHONPATH="$PWD/src"
export PYTHONSTARTUP="$PWD/.pythonrc"

env JPDB_USERNAME=yourname \
    JPDB_PASSWORD=secret \
    python -m unittest
```

## Changes

All notable changes in this project will be documented in the file
[CHANGELOG.md](CHANGELOG.md).

## License

[//]: # (TODO: select a license, audit, and publish the package on PyPi)

[Copyright &copy; 2022 Uwe Stuehler (UNLICENSED)](LICENSE)
