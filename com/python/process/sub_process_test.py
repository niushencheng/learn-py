import subprocess

if __name__ == '__main__':
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'www.baidu.com\nexit\n')
    print(output.decode('utf-8'))
