import pymongo
from flask import Flask, request, render_template


app = Flask(__name__)
db_client = pymongo.MongoClient('mongodb://3.90.3.145:27017,3.90.3.145:27017,54.173.17.242:27017/?replicaSet=rs0')
db = db_client['chat']


@app.route('/', methods=['POST'])
def get_form():
  aut_user = request.form['User']
	message = request.form['Message']
	collection = db['messages']
	collection.insert_one({'author': aut_user, 'content': message})
	return render_template('index.html', messages=get_messages())

def get_mess():
	collection = db['messages']
	messages = collection.find({}, {'_id': 0})
	return messages


@app.route('/')
def ind_page():
	return render_template('index.html', messages=get_mess())

if __name__ == '__main__':
	app.run(host='0.0.0.0')
