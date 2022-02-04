from console_extension import Console, Colors

tabel = [
    ["1et", "2", "3", "4", "1", "2", "3","1", "2", "3"],
    ["1", "2", "3"],
    ["1", "2", "3", "4", "1", "2", "3","1", "2", "3"],
]

c = Console()
c.set_foreground(Colors.BLUE)
c.print_tabel(tabel)
