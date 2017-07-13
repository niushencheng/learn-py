import os,chardet


def list_files(path):
    return os.listdir(path)


if __name__ == '__main__':
    # with open('/opt/logs/csc-paas/service.log.2017-07-07', mode = 'r', encoding = 'gbk') as fp:
    #     lines = fp.readlines()
    #
    # with open('/opt/logs/csc-paas/service.log.2017-07-07', mode = 'w', encoding = 'utf-8') as fp:
    #     fp.writelines(lines)
    path = '/opt/logs/csc-paas/'
    for f in list_files(path):
        with open(path + f, mode = 'rb') as fp:
            line = fp.read()
        print(chardet.detect(line))

