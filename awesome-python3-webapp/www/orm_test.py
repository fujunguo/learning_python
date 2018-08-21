import orm
from models import User, Blog, Comment
import asyncio


async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='password', db='awesome')
    u = User(name='test', email='test@example.com', passwd='1234567890', image='about.blank', id='123')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

# MySQL命令行查询语句
# SELECT * FROM users WHERE id = 1234;
