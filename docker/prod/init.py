#!/usr/bin/env python
"""
Init dirs for bind volumes expected docker environment in a general case,
run with user that will run docker service
"""
from pathlib import Path


# Case for run at root of project
# BASE_DIR: Path = Path(__file__).resolve().parent

# Case for run at docker/up_type
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

DIR_MODE = 0o777
FILE_MODE = 0o666

# Docker compose location, example case docker/prod
COMPOSE_DIR: Path = Path(BASE_DIR, "docker", "prod")

# apps container names
APPS_CONTAINER = (
    "app_api",
    "app_beat",
    "app_worker",
)

# Logs
LOG_DIR = Path(BASE_DIR, "logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

for app_i in APPS_CONTAINER:
    LOG_APP_I_DIR = Path(LOG_DIR, app_i)
    LOG_APP_I_DIR.mkdir(parents=True, exist_ok=True)

# run dir
RUN_DIR = Path(BASE_DIR, "run")
RUN_DIR.mkdir(parents=True, exist_ok=True)

for app_i in APPS_CONTAINER:
    RUN_APP_I_DIR = Path(RUN_DIR, app_i)
    RUN_APP_I_DIR.mkdir(parents=True, exist_ok=True)

# Output dir
OUTPUT_DIR = Path(BASE_DIR, "output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for app_i in APPS_CONTAINER:
    OUTPUT_APP_I_DIR = Path(OUTPUT_DIR, app_i)
    OUTPUT_APP_I_DIR.mkdir(parents=True, exist_ok=True)

# TEMP DIR
TEMP_DIR = Path(BASE_DIR, "temp")
TEMP_DIR.mkdir(parents=True, exist_ok=True)

for app_i in APPS_CONTAINER:
    TEMP_APP_I_DIR = Path(TEMP_DIR, app_i)
    TEMP_APP_I_DIR.mkdir(parents=True, exist_ok=True)

# DB bind
DB_POSTGRES_DIR = Path(BASE_DIR, "postgres")
DB_POSTGRES_DIR.mkdir(parents=True, exist_ok=True)

# init sql files
DB_POSTGRES_INIT_FILE = Path(COMPOSE_DIR, "project_example-init.sql")
DB_POSTGRES_INIT_FILE.touch(exist_ok=True)

# Uwsgi - Custom case
UWSGI_DIR = Path(COMPOSE_DIR, "uwsgi")
UWSGI_DIR.mkdir(parents=True, exist_ok=True)

UWSGI_FILE = Path(UWSGI_DIR, "uwsgi.ini")
UWSGI_FILE.touch(exist_ok=True)

# Proxy
PROXY_DIR = Path(BASE_DIR, "proxy")
PROXY_DIR.mkdir(parents=True, exist_ok=True)

PROXY_CONF_DIR = Path(PROXY_DIR, "conf.d")
PROXY_CONF_DIR.mkdir(parents=True, exist_ok=True)

PROXY_SSL_DIR = Path(PROXY_DIR, "ssl")
PROXY_SSL_DIR.mkdir(parents=True, exist_ok=True)

# env files, this will use type of docker up for env files
# Base file location docker/prod/.env-postgres-template
ENV_POSTGRES_FILE = Path(COMPOSE_DIR, ".env-postgres")
ENV_POSTGRES_FILE.touch(exist_ok=True)

# Base file location supervisor/.env-supervisor-template
ENV_SUPERVISOR_FILE = Path(COMPOSE_DIR, ".env-supervisor")
ENV_SUPERVISOR_FILE.touch(exist_ok=True)

# Base file location project_example/.env-django-template
ENV_DJANGO_FILE = Path(COMPOSE_DIR, ".env-django")
ENV_DJANGO_FILE.touch(exist_ok=True)
