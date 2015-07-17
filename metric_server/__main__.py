import sys
import socket
import logging
from Queue import Queue
from threading import Thread
import pymysql.cursors


port = 13373
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
counter = 0
logging.basicConfig(
    filename="/tmp/metric_server.log",
    level=logging.DEBUG
)

connection = pymysql.connect(
    host='localhost',
    user='',
    passwd='',
    db='',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


def do_stuff(f):
    while True:
        try:
            line = f.get()
            d = line.split(':')
            try:
                routes = d[0].split('.')
                ts = d[1].split('|')[0]
                pre_data = {}
                for route in routes:
                    path = route.split('%')
                    value = str(path[1])
                    pre_data[path[0]] = value
                pre_data['ts'] = int(float(ts))
                do_write_sql(pre_data)
            except KeyboardInterrupt:
                e = sys.exc_info()
                print(e)
            f.task_done()
        except KeyboardInterrupt:
            e = sys.exc_info()
            print(e)


def do_write_sql(d):
    print(d)


if __name__ == '__main__':
    q = Queue(maxsize=0)
    num_threads = 1

    for i in range(num_threads):
        worker = Thread(target=do_stuff, args=(q,))
        worker.setDaemon(True)
        worker.start()

    while True:
        data, addr = s.recvfrom(1024)
        counter += 1
        if data:
            q.put(data)

    q.join()
