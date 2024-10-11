from flask import Flask, request
from flask_restful import Api, Resource
from models import add_task, get_tasks, get_task, update_task, delete_task

app = Flask(__name__)
api = Api(app)

class TaskList(Resource):
    def get(self):
        return get_tasks()

    def post(self):
        data = request.get_json()
        title = data['title']
        return add_task(title), 201

class Task(Resource):
    def get(self, task_id):
        task = get_task(task_id)
        return task if task else ("Not found", 404)

    def put(self, task_id):
        data = request.get_json()
        title = data['title']
        done = data['done']
        updated_task = update_task(task_id, title, done)
        return updated_task if updated_task else ("Not found", 404)

    def delete(self, task_id):
        deleted_task = delete_task(task_id)
        return deleted_task if deleted_task else ("Not found", 404)

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
