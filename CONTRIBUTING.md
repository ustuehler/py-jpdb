# Contributing Guide

For now, this is a personal project and I don't have any plans to support it,
at least not until there's an official API documentation available for jpdb.

## Getting started with local development

These instructions assume that [Python 3](https://docs.python.org/3/) is
installed in your system and available in the shell's command search path as
`python3`.

Once you have cloned this repository, create and activate a temporary virtual
environment, and then install the required dependencies as follows:

```
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

[Register](https://jpdb.io/register) a jpdb user account, unless you already
have one, and then provide its username and password as environment variables:

```
export JPDB_USERNAME='your_username'
export JPDB_PASSWORD='your_password'
```

You can then start Python via `python -i .pythonrc` to explore the functionality
and documentation of this package interactively.

## Running unit and integration tests locally

Ensure that the temporary virtual environment created for local development is
active, and then execute the command `python -m unittest`.
