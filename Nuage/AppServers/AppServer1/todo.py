from flask import Flask
from flask import jsonify
from flask import request,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todo'
app.config['MONGO_URI'] = 'mongodb://mongoDB:27017/todo'

mongo = PyMongo(app)

@app.route('/')
def todo():
  return render_template('index.html')


@app.route('/api/todos', methods=['GET'])
def get_all_todos():
  todo = mongo.db.todos
  output = [] 
  for s in todo.find():
    print s['_id']
    output.append({'_id':str(s['_id']),'task' : s['task']})
  return jsonify({'result' : output})


@app.route('/api/todos/<string:_id>', methods=['DELETE'])
def delete_todo(_id):
  todo = mongo.db.todos
  output = []
  if _id:
    print _id
    todo.delete_one({'_id':ObjectId(_id)});
    todo.remove(_id)
    for s in todo.find():
      output.append({'_id':str(s['_id']),'task' : s['task']})
  else:
    error ="No such task"
  return jsonify({'result' : output })

@app.route('/api/todos', methods=['POST'])
def add_todo():
  todo = mongo.db.todos
  task = request.json['text']
  task_id = todo.insert({'task': task})
  new_task = todo.find_one({'_id': task_id })
  output = {'_id':str(task_id),'task' : new_task['task']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)

