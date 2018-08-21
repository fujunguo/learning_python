from xml.parsers.expat import ParserCreate
from urllib import request


# class DefaultSaxHandler(object):
#
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
#
# xml = r'''<?xml version='1.0'?>
# <ol>
#     <li><a href='/python'>Python</a></li>
#     <li><a href='/ruby'>Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)


# 利用SAX编写程序解析Yahoo的XML格式的天气预报
class WeatherSaxHandler(object):
    def Location(self, name, attrs):
        if name == 'yweather:location':
            print(attrs)
            self.location = attrs['country']
            print(self.location)


def parseXml(xml_str):
    print(xml_str)
    handler1 = WeatherSaxHandler()
    parser1 = ParserCreate()
    parser1.StartElementHandler = handler1.Location
    parser1.Parse(xml_str)
    return {
        'city': handler1.location
    }


URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()


result = parseXml(data.decode('utf-8'))
# print(result)
assert result['city'] == 'China'
print('OK.')
