import time
from threading import Thread


def some_task(n):
    start = 1
    while n > 0:
        start *= n
        n -= 1
    time.sleep(3)

start = time.time()
some_task(100)
some_task(100)

print('wef',  time.time() - start)

thread1 = Thread(target=some_task, args=(100, ))
thread2 = Thread(target=some_task, args=(100, ))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('sdsdffssfd', time.time() - start)