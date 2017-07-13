import subprocess, re

if __name__ == '__main__':
    p = subprocess.Popen(['git', 'status'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    lines = p.stdout.readlines()
    for line in lines:
        print(line.decode('utf-8'))
