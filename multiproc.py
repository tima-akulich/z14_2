import time
from multiprocessing import Process, Semaphore, Lock, Event

N = 50000


def factorial(n):
    start = 1
    while n > 0:
        start *= n
        n -= 1
    return start

start = time.time()
factorial(N)
factorial(N)
factorial(N)
print('Without process', time.time() - start)


process1 = Process(target=factorial, args=(N, ))
process2 = Process(target=factorial, args=(N, ))
process3 = Process(target=factorial, args=(N, ))

start = time.time()
process1.start()
process2.start()
process3.start()
process1.join()
process2.join()
process3.join()

print('With process', time.time() - start)