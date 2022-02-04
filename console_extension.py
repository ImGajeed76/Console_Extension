class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


class Console:
    default_foreground = Colors.LIGHT_WHITE
    foreground_color = None

    def __init__(self, default_foreground: str = Colors.LIGHT_WHITE):
        self.default_foreground = default_foreground

    def print(self, value: any, color: str = None, sep=' ', end=''):
        out = ""
        if self.foreground_color is not None:
            out += self.foreground_color

        if color is not None:
            out += color

        out += str(value)

        if self.foreground_color is None:
            out += self.default_foreground

        print(out, sep=sep, end=end)

    def println(self, value: any, color: str = None, sep=' ', end=' '):
        out = ""
        if self.foreground_color is not None:
            out += self.foreground_color

        if color is not None:
            out += color

        out += str(value)

        if self.foreground_color is None:
            out += self.default_foreground

        print(out, sep=sep, end=end+'\n')

    def print_tabel(self, tabel: list[list[any]]):
        out = ""

        for row in tabel:
            r = "| "
            for val in row:
                r += str(val) + " | "

            out += r + "\n"

        print(out)

    def set_foreground(self, color: str):
        self.foreground_color = color

    def reset_foreground(self):
        self.foreground_color = None
