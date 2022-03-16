from curses import wrapper
import wscheck

def main(stdscr):
    ws = wscheck.wscheck()

    stdscr.clear()
    for i in range(1, 51):
        if i == 1: stdscr.addstr(2, 28, 'std5dc'+str(i))
        elif i == 50: stdscr.addstr(2, 48, 'std5dc'+str(i))
        else: stdscr.addstr(8+4*int((i-2)/4), 8+20*int((i-2)%4), "std5dc"+str(i))

    stdscr.refresh()

    for i in range(1, 51):
        if i == 1: stdscr.addstr(3, 28, ws.get_userid('std5', i))
        elif i == 50: stdscr.addstr(3, 48, ws.get_userid('std5', i))
        else: stdscr.addstr(9+4*int((i-2)/4), 8+20*int((i-2)%4), ws.get_userid('std5', i))
        stdscr.refresh()

    input()

if __name__ == "__main__":
    wrapper(main)