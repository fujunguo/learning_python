# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持
import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello, world! (%s)' % threading.current_thread())
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


# 获取eventloop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
