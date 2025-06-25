import subprocess

user_input = 'E:\\HGL && ping -n 4 google.com'
subprocess.run(["cmd.exe", "/c", "dir", user_input], shell=False)
