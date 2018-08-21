def consumer():
    r = ''
    while True:
        # 将带回的值赋值给n
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK!'


def produce(c):
    # 启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 用生成器的内部方法send进入生成器，并带回一个值
        r = c.send(n)
        print('[PRODUCER] Consuming return: %s' % r)
    c.close()


c = consumer()
produce(c)
