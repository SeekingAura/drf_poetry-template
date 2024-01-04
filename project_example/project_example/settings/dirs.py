import os
from pathlib import Path
from dotenv import (
    find_dotenv,
    load_dotenv,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

load_dotenv(
    dotenv_path=find_dotenv(
        filename=Path(BASE_DIR, ".env-django").__str__(),
    ),
)

# Logs
LOG_DIR = Path(BASE_DIR.parent, "logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_CSV_DIR = Path(LOG_DIR, "reports_csv")
LOG_CSV_DIR.mkdir(parents=True, exist_ok=True)

LOG_SUPERVISOR = Path(LOG_DIR, "supervisor")
LOG_SUPERVISOR.mkdir(parents=True, exist_ok=True)

LOG_CELERY = Path(LOG_DIR, "celery")
LOG_CELERY.mkdir(parents=True, exist_ok=True)

# Supervisor misc
RUN_DIR = Path(BASE_DIR.parent, "run")
RUN_DIR.mkdir(parents=True, exist_ok=True)

RUN_SUPERVISOR_DIR = Path(RUN_DIR, "supervisor")
RUN_SUPERVISOR_DIR.mkdir(parents=True, exist_ok=True)

RUN_CELERY_DIR = Path(RUN_DIR, "celery")
RUN_CELERY_DIR.mkdir(parents=True, exist_ok=True)

# Files export
EXPORT_RESULT_DIR = Path(BASE_DIR.parent, "output")

TEMP_DISK_DIR = Path(BASE_DIR.parent, "temp")
