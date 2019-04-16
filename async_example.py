import asyncio
import time
import random
import requests

loop = asyncio.get_event_loop()


async def print_text(text):
    print(text)

loop.run_until_complete(print_text("Hello world"))

async def db_request():
    await asyncio.sleep(3)
    return [random.randint(1, 10) for _ in range(10)]


async def foo_1(text):
    print(f"{text}. Action 1")
    db_data = await db_request()
    print(f"{text}. Action 2", db_data)

# tasks = [foo_1("Foo 1"), foo_1("Foo 2")]
# wait_task = asyncio.wait(tasks)
# loop.run_until_complete(wait_task)


def task(pid):
    time.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


async def task_coro(pid):
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    tasks = [task_coro(i) for i in range(1, 10)]
    await asyncio.wait(tasks)


# synchronous()

loop.run_until_complete(asynchronous())


