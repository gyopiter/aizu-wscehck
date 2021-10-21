#!/usr/bin/env python3
import paramiko, os.path, time, userconfig

STD12_MAX, STD34_MAX, STD56_MAX, CALL12_MAX, ILAB12_MAX = 46, 52, 50, 34, 49
IDENTITY = userconfig.IDENTITY
USER = userconfig.USER

def askroom():
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

if __name__ == '__main__':
    userList = {}
    room, numOfDesktop = askroom()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('sshgate.u-aizu.ac.jp', username=USER, key_filename=os.path.expanduser(IDENTITY))
    stdin, stdout, stderr = ssh.exec_command('getent passwd')
    for line in stdout: userList[line.split(':')[0]] = line.split(':')[4] 
    for i in range(1, numOfDesktop+1):
        print(f'\n\n===== LOGIN {room}dc{i} =====')

        command = "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null %s@%sdc%d -i ~/.ssh/id_rsa 'ps aux'"\
            "| grep -E '^[sm][0-9]{7}'"\
            "| grep -v %s"\
            % (USER, room, i, USER)

        stdin, stdout, stderr = ssh.exec_command(command)
        for line in stdout: print(line.split()[0], userList[line.split()[0]], line.split()[10]) 
        time.sleep(0.8)
    ssh.close()