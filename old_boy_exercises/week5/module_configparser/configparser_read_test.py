# __author__: William Kwok
import configparser

"""读取一个 ini 配置文件"""
config = configparser.ConfigParser()
config.read('example.ini')

print(config.defaults())
print(config.sections())
print(config['bitbucket.org']['user'])
