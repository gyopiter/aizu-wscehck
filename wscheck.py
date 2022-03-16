#!/usr/bin/env python3
from threading import get_ident
import paramiko, os.path, time, userconfig, re

STD12_MAX, STD34_MAX, STD56_MAX, CALL12_MAX, ILAB12_MAX = 46, 52, 50, 34, 49
IDENTITY = userconfig.IDENTITY
USER = userconfig.USER

class wscheck:
    def askroom(self):
        room_select = input(
            '   === ROOM? ===   \n'\
            'std1:  1   std2:  2\n'\
            'std3:  3   std4:  4\n'\
            'std5:  5   std6:  6\n'\
            'ilab1: 7   ilab2: 8\n'\
            'call1: 9   call2: 0\n'\
            '   ===       ===   \n>> ')  
        room = ['call2', 'std1', 'std2', 'std3', 'std4', 'std5', 'std6', 'ilab1', 'ilab2', 'call1'] 
        room_select = int(room_select)
        if room_select == 1 or 2: num_workstation = STD12_MAX
        elif room_select == 3 or 4: num_workstation = STD34_MAX
        elif room_select == 5 or 6: num_workstation = STD56_MAX
        elif room_select == 7 or 8: num_workstation = ILAB12_MAX
        else: num_workstation = CALL12_MAX 
        return room[room_select], num_workstation
    
    def sshinit(self):
        self.user_list = {}
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect('sshgate.u-aizu.ac.jp', username=USER, key_filename=os.path.expanduser(IDENTITY))
        stdin, stdout, stderr = self.ssh.exec_command('getent passwd')
        for line in stdout: self.user_list[str(line.split(':')[0])] = str(line.split(':')[4])

    def get_userid(self, room, desktop):
        command = f"ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null {room}dc{desktop} -i ~/.ssh/id_rsa 'ps aux'"
        stdin, stdout, stderr = self.ssh.exec_command(command)
        id = None
        for line in stdout:
            if re.search('^[smd][0-9]{7}', line) != None:
                if room == 'std1' or room == 'std2' or room == 'std3' or room == 'std4':
                    if re.search('/usr/libexec/Xorg', line) != None:
                        id = line.split()[0]
                        break
                else:
                    if re.search('/Applications/Avid/Avid', line) != None:
                        id = line.split()[0]
                        break
        return str(id)

    def get_id2name(self, stdid):
        if stdid in self.user_list: 
            return self.user_list[stdid] 
        return None

    def __init__(self):
        self.sshinit()


if __name__ == '__main__':
    wschek = wscheck()
    room, num_workstation = wschek.askroom()
    for i in range(1, num_workstation+1):
        userid = wschek.get_userid(room, i)
        if userid != None:
            print(f"{room}dc{i} : {userid}")
        else:
            print(f"{room}dc{i} : None")
        print(wschek.get_id2name(userid))
    