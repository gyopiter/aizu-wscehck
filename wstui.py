import curses

STD12_MAX, STD34_MAX, STD56_MAX, CALL12_MAX, ILAB12_MAX = 46, 52, 50, 34, 49

class wstui: 
    
    def drawroom(self): 
        self.stdscr.clear()
        col = 0
        if self.room == 'std1' or self.room == 'std2': col = 4
        elif self.room == 'std3' or self.room == 'std4': col = 6
        elif self.room == 'std5' or self.room == 'std6': col = 4
        elif self.room == 'ilab1' or self.room == 'ilab2': col = 6
        elif self.room == 'call1' or self.room == 'call2': col = 4

        self.col = col
        
        if self.room != 'ilab1' and self.room != 'ilab2':
            for i in range(1, self.wsmax+1):
                if i == 1: self.stdscr.addstr(2, 28, self.room+'dc'+str(i))
                elif i == self.wsmax: 
                    if col == 4: self.stdscr.addstr(2, 48, self.room+'dc'+str(i))
                    elif col == 6: self.stdscr.addstr(2, 68, self.room+'dc'+str(i))
                else: self.stdscr.addstr(8+4*int((i-2)/col), 8+20*int((i-2)%col), self.room+'dc'+str(i))
        else:
            for i in range(1, self.wsmax+1):
                if i == 1: self.stdscr.addstr(2, 58, self.room+'dc'+str(i))
                else: self.stdscr.addstr(8+4*int((i-2)/col), 8+20*int((i-2)%col), self.room+'dc'+str(i))
        self.stdscr.refresh()
    
    def add_description(self, wsnum, text, num_line=1):
        i = wsnum
        text = str(text)
        if i > self.wsmax or i < 1:
            print('Error: wsnum out of range', file=stderr)
            return False
        if self.room != 'ilab1' and self.room != 'ilab2':
            if i == 1: self.stdscr.addstr(2+num_line, 28, text)
            elif i == self.wsmax: 
                if self.col == 4: self.stdscr.addstr(2+num_line, 48, text)
                elif self.col == 6: self.stdscr.addstr(2+num_line, 68, text)
            else: self.stdscr.addstr(8+num_line+4*int((i-2)/self.col), 8+20*int((i-2)%self.col), text)
        else:
            if i == 1: self.stdscr.addstr(2+num_line, 58, text)
            else: self.stdscr.addstr(8+num_line+4*int((i-2)/self.col), 8+20*int((i-2)%self.col), text)
        self.stdscr.refresh()
        return True
        
    

    def __del__(self):
        self.stdscr.clear()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def __init__(self, room=None):
        self.room = room
        self.col = 0
        self.wsmax = 0
        if room == 'std1' or room == 'std2':
            self.wsmax = STD12_MAX
        elif room == 'std3' or room == 'std4':
            self.wsmax = STD34_MAX
        elif room == 'std5' or room == 'std6':  
            self.wsmax = STD56_MAX
        elif room == 'call1' or room == 'call2':
            self.wsmax = CALL12_MAX
        elif room == 'ilab1' or room == 'ilab2':
            self.wsmax = ILAB12_MAX
        else:
            print('Error: room not recognized', file=stderr)
            exit(1)
        self.stdscr = curses.initscr()    
        curses.noecho()

if __name__ == '__main__':
    tui = wstui('ilab1')
    tui.drawroom()
    for i in range(1, tui.wsmax+1):
        tui.add_description(i, 'hoge'+str(i))
    for i in range(1, tui.wsmax+1):
        tui.add_description(i, 'hogehoge', 2)
    tui.stdscr.getkey()
    del tui
