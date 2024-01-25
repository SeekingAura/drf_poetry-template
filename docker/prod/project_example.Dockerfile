FROM python:3.10.13-alpine3.18 as step-installed

# Poetry requisites
RUN apk add --no-cache gcc libc-dev libpq-dev python3-dev

# Create app user
RUN adduser -D app_user
USER app_user
WORKDIR /home/app_user/app

COPY --chown=app_user:app_user [ \
  "./poetry.toml", \
  "./pyproject.toml", \
  "./setup.cfg", \
  "/home/app_user/app/" \
]

# Set PATH to local installed user
ENV PATH="/home/app_user/.local/bin:${PATH}"

# Set APP_ROOT var
ENV APP_ROOT="/home/app_user/app"

# Set DJANGO_APP_NAME var
ENV DJANGO_APP_NAME="project_example"

# Install poetry on system
RUN pip install poetry --user

RUN poetry install

# Add venv script
USER root
# Create docker entrypoint
RUN mkdir -p /docker/scripts

COPY [ \
  "./docker/scripts/entrypoint-python_venv.sh", \
  "/docker/scripts/" \
]

RUN chmod -R a+x /docker/scripts

ENTRYPOINT [ "/docker/scripts/entrypoint-python_venv.sh" ]

USER app_user

FROM step-installed as step-project_run

# Project
COPY --chown=app_user:app_user [ \
  "./project_example", \
  "/home/app_user/app/project_example" \
]

# supervisor
COPY --chown=app_user:app_user [ \
  "./supervisor", \
  "/home/app_user/app/supervisor" \
]

RUN chmod -R a+x /home/app_user/app/supervisor/scripts

# No commands still container up after creation
CMD ["tail", "-f", "/dev/null"]