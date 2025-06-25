import subprocess

user_input = "E:\\HGL && ping -n 4 google.com"
result = subprocess.run(["cmd.exe","/c dir " + user_input], shell=False,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)