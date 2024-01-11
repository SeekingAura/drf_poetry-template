# Django Rest Template with poetry

This is a project template

TODO: create ci/cd

# project_example

# Locally Usage
## Prerequisites
### OS
- Ubuntu 20.04 LTS+
- Windows 10

### Software
- Python 3.10+
- Python pip
- Python venv
- Python Poetry

## Install locally
Run this command at root of project
```shell
poetry install
```

This install the minimum requirements for run project

# Containerized mode
you can omit all pre-requisites and run project with docker containers
- Docker engine 24.0.7+

# Generate docs
## Install project with docs
To run docs generation requires project and docs packages
```shell
poetry install --with docs
```

## Generate docs
On [docs](./docs) folder run
```bash
make html
```
