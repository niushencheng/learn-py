from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write... %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put value to queue... %s' % value)
        q.put(value)
        s = random.random()
        print('sleep %s' % s)
        time.sleep(s)


def read(q):
    print('Process to read... %s' % os.getpid())
    while True:
        value = q.get()
        print('get value from queue %s' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # pr 是死循环，所以不能等待pr的join，需要通过terminate强制杀死pr
    pr.terminate()
