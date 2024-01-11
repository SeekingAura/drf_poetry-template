import logging
import logging.config
from typing import Optional


class FilterLogLevelSep(logging.Filter):
    _filter_levels: list[str]

    def __init__(
        self,
        name: str = "",
        filter_levels: Optional[list[str]] = None,
    ):
        super(FilterLogLevelSep, self).__init__(name=name)
        self._filter_levels = filter_levels or list()

    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelname in self._filter_levels:
            return True
        return False
