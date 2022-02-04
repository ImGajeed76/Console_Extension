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


def create_table_line_break(y: int, row_before: str, row_after: str, max_y: int):
    if len(row_before) > len(row_after):
        length = len(row_before) - 1
        row_after += " " * (len(row_before) - len(row_after))
    else:
        length = len(row_after) - 1
        row_before += " " * (len(row_after) - len(row_before))

    lb = ""
    for i in range(length):
        if i == 0 and y == 0:
            lb += "┌"
        elif i == len(row_after) - 2 and y == 0:
            lb += "┐"
        elif i == len(row_after) - 2 and row_before[i] == " ":
            lb += "┐"
        elif i == 0 and y == max_y:
            lb += "└"
        elif i == len(row_after) - 2 and y == max_y:
            lb += "┘"
        elif i == len(row_after) - 2 and row_after[i] == " ":
            lb += "┘"
        elif row_after[i] == "|" and y == 0:
            lb += "┬"
        elif row_after[i] == "|" and row_before[i] == " ":
            lb += "┬"
        elif row_before[i] == "|" and y == max_y:
            lb += "┴"
        elif row_before[i] == "|" and row_after[i] == " ":
            lb += "┴"
        elif row_after[i] == "|" and i == 0:
            lb += "├"
        elif row_after[i] == "|" and i == len(row_after) - 2:
            lb += "┤"
        elif row_after[i] == "|" and row_before[i] == "|":
            lb += "┼"
        else:
            lb += "-"

    return lb


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

        print(out, sep=sep, end=end + '\n')

    def print_tabel(self, tabel: list[list[any]]):
        out = ""
        row_before = ""

        for k in range(len(tabel)):
            vals = ""
            vals += "| "
            for val in tabel[k]:
                vals += str(val) + " | "

            lb = create_table_line_break(k, row_before, vals, len(tabel))

            out += lb + "\n" + vals + "\n"
            row_before = vals

        lb = create_table_line_break(len(tabel), row_before, "", len(tabel))

        out += lb

        print(out)

    def set_foreground(self, color: str):
        self.foreground_color = color

    def reset_foreground(self):
        self.foreground_color = None
