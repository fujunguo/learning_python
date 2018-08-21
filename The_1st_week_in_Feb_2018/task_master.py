import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，
# 使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，
# 因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


# 同时，序列化不支持匿名函数，需将函数拉出来定义
def start_server():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
# 绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
# 启动Queue()
    manager.start()
# 获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
# 放几个任务进去：
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
# 从result队列对去结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
# 关闭queue
    manager.shutdown()
    print('master exit')


if __name__ == '__main__':
    start_server()
