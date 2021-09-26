# data from https://github.com/osamayy/azkar-db

from random import randint
from csv import reader
from flask import Flask

f = open('azkar.csv', 'r')
content = list(reader(f))
f.close()

content = content[1:]

app = Flask(__name__)

# generate from 0 to len(content) - 1

@app.route('/')
def index():
	random_int = randint(0, len(content)-1)	
	gen = {
		'category' : content[random_int][0],
		'zekr' : content[random_int][1],
		'description': content[random_int][2],
		'count': content[random_int][3],
		'reference': content[random_int][4]
	}
	return gen


if __name__ == '__main__':
    app.run()
