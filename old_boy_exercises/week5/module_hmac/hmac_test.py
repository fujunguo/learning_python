# __author__: William Kwok
# hmac 内部对我们创建 key 和内容再进行处理，
# 然后再加密,安全性更高
import hmac

h = hmac.new('天王盖地虎'.encode('utf-8'), '宝塔镇河妖'.encode('utf-8'))
print(h.hexdigest())
