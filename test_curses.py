import curses
from curses import wrapper
from textwrap import wrap

def main(stdscr):
    stdscr.clear()
    for i in range(50): stdscr.addstr(i, 0, str(i))
    for i in range(44):
        stdscr.addstr(8+4*int(i/6), 8+20*int(i%6), "std1dc"+str(i+2))
    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)