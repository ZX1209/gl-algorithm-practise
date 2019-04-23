import threading

threads = []

def shadow(num):
    print('产生了第{}个分身...'.format(num))

for i in range(1, 100):
    threads.append(threading.Thread(target=shadow, args=(i,)))
    threads[-1].start()

for t in threads:
    t.join()
