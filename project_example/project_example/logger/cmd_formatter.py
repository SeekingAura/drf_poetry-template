class CmdFormatter:
    """
    Management for console format colors and styles with ANSI escape chars
    followed by https://pypi.org/project/colorama/
    """

    # ANSI escape chars Colors
    __RED = "\x1b[31m"
    __YELLOW = "\x1b[33m"
    __CYAN = "\x1b[36m"
    __MAGENTA = "\x1b[35m"

    # ANSI escape chars Style
    __BRIGHT = "\x1b[1m"

    # ANSI escape chars Misc
    __RESET_ALL = "\x1b[0m"

    @classmethod
    def reset(cls) -> str:
        return cls.__RESET_ALL

    @classmethod
    def debug(cls) -> str:
        return cls.__MAGENTA

    @classmethod
    def info(cls) -> str:
        return cls.__CYAN

    @classmethod
    def warning(cls) -> str:
        return cls.__YELLOW

    @classmethod
    def error(cls) -> str:
        return cls.__RED

    @classmethod
    def critical(cls) -> str:
        return f"{cls.__BRIGHT}{cls.error}"
