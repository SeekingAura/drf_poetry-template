import logging
import logging.config
from typing import Optional


class FilterLogLevelSep(logging.Filter):
    """
    Limit log output to log levels located at
    :attr:`FilterLogLevelSep._filter_levels`

    :param _filter_levels: levels name in full caps that are allowed to emit\
    log
    :type _filter_levels: list[str], list of levels in str uppercase
    """

    _filter_levels: list[str]
    """
    levels name in full caps that are allowed to emit log
    """

    def __init__(
        self,
        name: str = "",
        filter_levels: Optional[list[str]] = None,
    ):
        """
        Initialize filter Log level separator

        :param name: name of filter, required on related object\
        :class:`logging.Filter`, defaults to ""
        :type name: str, optional
        :param filter_levels: levels name in full caps that are allowed to\
        emit log, defaults to empty list through value None
        :type filter_levels: Optional[list[str]], optional
        """
        super(FilterLogLevelSep, self).__init__(name=name)
        self._filter_levels = filter_levels or list()

    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelname in self._filter_levels:
            return True
        return False
