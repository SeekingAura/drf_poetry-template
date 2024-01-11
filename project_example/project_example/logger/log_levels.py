from django.db import models
import logging


class LogLevels(models.IntegerChoices):
    """
    Log levels managed on django project with default integer values from
    :mod:`logging <python310:logging>`
    """

    CRITICAL = logging.CRITICAL
    """
    Level critical, most high level value for worst system. A serious error,
    indicating that the program itself may be unable to continue running.

    followed by: :mod:`logging` documentation
    """
    ERROR = logging.ERROR
    """
    Level error, Due to a more serious problem, the software has not been able
    to perform some function.

    followed by: :mod:`logging` documentation
    """
    WARNING = logging.WARNING
    """
    An indication that something unexpected happened, or that a problem might
    occur in the near future (e.g. 'disk space low'). The software is still
    working as expected.

    followed by: :mod:`logging` documentation
    """
    INFO = logging.INFO
    """
    Confirmation that things are working as expected.

    followed by: :mod:`logging` documentation
    """
    DEBUG = logging.DEBUG
    """
    Detailed information, typically only of interest to a developer trying to
    diagnose a problem.

    followed by: :mod:`logging` documentation
    """
    NOTSET = logging.NOTSET
    """
    When set on a logger, indicates that ancestor loggers are to be consulted
    to determine the effective level. If that still resolves to `NOTSET`, then
    all events are logged. When set on a handler, all events are handled.

    followed by: :mod:`logging` documentation
    """

    @classmethod
    def get_known_levels(cls) -> set[str]:
        """
        Get known log levels for project

        :return: set of common known log levels, level NOTSET is excluded
        :rtype: set[str]
        """
        known_levels = set(cls.__members__.keys())
        known_levels.remove(cls.NOTSET.name)
        return known_levels
