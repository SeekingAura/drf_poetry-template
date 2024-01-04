from django.db import models
import logging


class LogLevels(models.IntegerChoices):
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET

    @classmethod
    def get_known_levels(cls) -> set[str]:
        known_levels = set(cls.__members__.keys())
        known_levels.remove(cls.NOTSET.name)
        return known_levels
