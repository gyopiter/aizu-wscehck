from genericpath import exists
import wstui, wscheck

try:
    ws = wscheck.wscheck()
    room, wsnum = ws.askroom()
    tui = wstui.wstui(room)
    tui.drawroom()
    for i in range(1, wsnum+1):
        id = ws.get_userid(room, i)
        tui.add_description(i, id, num_line=1)
        tui.add_description(i, ws.get_id2name(id), num_line=2)
    tui.stdscr.getkey()
finally:
    del tui