import subprocess, os

if __name__ == '__main__':
    p = subprocess.Popen(['locate', 'matplotlib'], stdin = subprocess.PIPE, stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
    lines = p.stdout.readlines()
    for line in lines:
        line = line.decode('utf-8')
        os.system('echo "fdsjkl" | sudo -S rm -rf ' + line)
