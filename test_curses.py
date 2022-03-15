from curses import wrapper
import wscheck

def main(stdscr):
    ws = wscheck.wscheck()

    stdscr.clear()
    for i in range(1, 53):
        if i == 1: stdscr.addstr(2, 38, 'std3dc'+str(i))
        elif i == 52: stdscr.addstr(2, 78, 'std3dc'+str(i)) 
        else: stdscr.addstr(8+4*int((i-2)/6), 8+20*int((i-2)%6), "std3dc"+str(i))

    stdscr.refresh()
    for i in range(1, 53):
        if i == 1: stdscr.addstr(3, 38, ws.get_userid('std3', i))
        elif i == 52: stdscr.addstr(3, 78, ws.get_userid('std3', i))
        else: stdscr.addstr(9+4*int((i-2)/6), 8+20*int((i-2)%6), ws.get_userid('std3', i)+'\nYeay')
        stdscr.refresh()

    input()

if __name__ == "__main__":
    wrapper(main)