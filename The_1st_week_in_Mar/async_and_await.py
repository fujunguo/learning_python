import asyncio
import threading

# 为了简化并更好地标识异步IO，从Python3.5开始
# 引入了新的语法async和await，可以
# 让coroutine的代码更简洁易读


# 将@asyncio.coroutine替换async
async def hello():
    print('Hello, World! -> %s' % threading.current_thread())
    # 将yield from替换为await
    r = await asyncio.sleep(1)
    print('Hello again! -> %s' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
