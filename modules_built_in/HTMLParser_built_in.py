from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('Start tag: <%s>, %s' % (tag, attrs))

    def handle_endtag(self, tag):
        print('End tag:</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('Startendtag: <%s/>' % tag)

    def handle_data(self, data):
        print('Data: %s' % data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&#:' % name)

    def handle_charref(self, name):
        print('&#%s' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


