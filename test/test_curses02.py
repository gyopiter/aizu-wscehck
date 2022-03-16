from curses import wrapper
import wscheck

def main(stdscr):
    ws = wscheck.wscheck()

    stdscr.clear()
    for i in range(1, 47):
        if i == 1: stdscr.addstr(2, 28, 'std1dc'+str(i))
        elif i == 46: stdscr.addstr(2, 48, 'std1dc'+str(i))
        else: stdscr.addstr(8+4*int((i-2)/4), 8+20*int((i-2)%4), "std1dc"+str(i))

    stdscr.refresh()

    for i in range(1, 47):
        if i == 1: stdscr.addstr(3, 28, ws.get_userid('std1', i))
        elif i == 46: stdscr.addstr(3, 48, ws.get_userid('std1', i))
        else: stdscr.addstr(9+4*int((i-2)/4), 8+20*int((i-2)%4), ws.get_userid('std1', i))
        stdscr.refresh()

    input()

if __name__ == "__main__":
    wrapper(main)