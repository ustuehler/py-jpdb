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

## Features

- Validation of login credentials (username & password)

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

## License

[//]: # (TODO: select a license, audit, and publish the package on PyPi)

[Copyright &copy; 2022 Uwe Stuehler (UNLICENSED)](LICENSE)
