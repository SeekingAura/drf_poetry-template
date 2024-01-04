import logging
import logging.config


class FilterLogLevelSep(logging.Filter):
    def __init__(self, filter_levels=None):
        super(FilterLogLevelSep, self).__init__()
        self._filter_levels = filter_levels

    #
    def filter(self, record):
        if record.levelname in self._filter_levels:
            return True
        return False
