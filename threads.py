import time
from threading import Thread, Event, Semaphore, Lock


def print_text(text, count):
    for _ in range(count):
        print(text)
        time.sleep(0.1)

# print_text('A', 5)
# print_text('B', 5)
#
# thread1 = Thread(target=print_text, args=('A', 10))
# thread2 = Thread(target=print_text, args=('B', 10))
#
# thread1.start()
# thread2.start()


def factorial(n):
    start = 1
    while n > 0:
        start *= n
        n -= 1
    return start

# NUMBER = 10000
# start = time.time()
# factorial(NUMBER)
# factorial(NUMBER)
# print('Without threads', time.time() - start)
#
# thread1 = Thread(target=factorial, args=(NUMBER, ))
# thread2 = Thread(target=factorial, args=(NUMBER, ))
#
# start = time.time()
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print('With threads', time.time() - start)

sem = Semaphore(1)
lock = Lock()


def print_text_events(text, count, event_wait, event_set):
    for _ in range(count):
        # event_wait.wait()
        # event_wait.clear()
        with sem:
            print(text)
            # event_set.set()
            time.sleep(0.5)

event1 = Event()
event2 = Event()

thread1 = Thread(target=print_text_events, args=('A', 10, event1, event2))
thread2 = Thread(target=print_text_events, args=('B', 10, event2, event1))
thread3 = Thread(target=print_text_events, args=('C', 10, event2, event1))

# event1.set()

#
thread1.start()
thread3.start()
thread2.start()


