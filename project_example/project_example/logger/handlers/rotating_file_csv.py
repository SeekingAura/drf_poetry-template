import os
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import (
    Any,
    Optional,
)


class RotatingFileCSV(RotatingFileHandler):
    """
    Logger for custom csv files that works like a Logger RotatingFileHandler,
    every rotation will have the header, every rollover usually happen before
    to emit
    """

    def __init__(
        self,
        filename: "Path",
        mode: str = "a",
        maxBytes: int = 0,
        backupCount: int = 0,
        encoding: Optional[str] = None,
        delay: bool = False,
        errors: Optional[str] = None,
        csv_vars: tuple[str, ...] = tuple(),
        sep: str = ",",
        *args: list[Any],
        **kwargs: dict[str, Any],
    ):
        """
        Constructor method

        :param filename: File where logger will emit
        :type filename: Path
        :param mode: mode that the file will opened at emit, append mode is
        required for log rotating files, defaults to "a"
        :type mode: str, optional
        :param maxBytes: max bytes that the file will have before to rotation\
        or rollover, value 0 rollover never occurs, defaults to 0
        :type maxBytes: int, optional
        :param backupCount: max of rotation files to persist, value 0 rollover\
        never occurs, defaults to 0
        :type backupCount: int, optional
        :param encoding: encoding of rotation file, defaults to None
        :type encoding: Optional[str], optional
        :param delay: perform a delay to emit process, defaults to False
        :type delay: bool, optional
        :param errors: _description_, defaults to None
        :type errors: Optional[str], optional
        :param csv_vars: tuple of csv vars that will used how headers of\
        every rotated file, the same order must be follow when log is emitted,\
        defaults to tuple()
        :type csv_vars: tuple[str, ...], optional
        :param sep: char separator on csv file, this value is used at join\
        process of :param:`csv_vars`, this char must be same on all log emits,\
        defaults to ","
        :type sep: str, optional
        """
        super().__init__(
            filename,
            mode,
            maxBytes,
            backupCount,
            encoding,
            delay,
            errors,
            *args,
            **kwargs,
        )
        self.csv_header: str = f"{sep.join(csv_vars)}\n"
        if not filename.exists() or os.path.getsize(filename) == 0:
            self.stream.write(self.csv_header)

    def doRollover(self):
        """
        At every rollover write csv header separated with separator then emit
        """
        super().doRollover()
        if self.mode == "w" or self.stream is None:  # type: ignore[UnnecessaryComparison]
            self.stream = self._open()
        self.stream.write(self.csv_header)
