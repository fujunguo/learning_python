# __author__: William Kwok
import json
info = {
	'name':'William',
	'age':20
}
f = open('test.text', 'w')
f.write(json.dumps(info))
f.close()