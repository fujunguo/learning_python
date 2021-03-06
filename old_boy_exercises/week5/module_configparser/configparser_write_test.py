# __author__: William Kwok
# cofigparser 模块用于修改和生成配置文件
import configparser

config = configparser.ConfigParser()
# print(type(config))
"""生成一个ini配置文件"""
config["DEFAULT"] = {'ServerAliveInterval': '45',
					 'Compression': 'yes',
					 'CompressionLevel': '9'
					 }

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'

config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
	config.write(configfile)


