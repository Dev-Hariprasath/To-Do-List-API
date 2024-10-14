from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/todo_db"  # Update with your MongoDB connection string
mongo = PyMongo(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the To-Do List API!"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = mongo.db.task.find()  # Ensure the collection name is 'task'
    return jsonify([
        {"id": str(task["_id"]), "title": task["title"], "status": task["status"]}
        for task in tasks
    ]), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()

    # Check if title is provided in the request
    if not new_task or 'title' not in new_task:
        return jsonify({"message": "Task title is required"}), 400

    new_task['status'] = False  # Default status
    result = mongo.db.task.insert_one(new_task)  # Ensure the collection name is 'task'

    # Return the created task with ID
    return jsonify({
        "id": str(result.inserted_id),
        "title": new_task["title"],
        "status": new_task["status"]
    }), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    task = mongo.db.task.find_one({"_id": ObjectId(task_id)})  # Ensure the collection name is 'task'

    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    data = request.get_json()
    updated_task = {
        "title": data.get('title', task["title"]),
        "status": data.get('status', task["status"]),
    }

    mongo.db.task.update_one({"_id": ObjectId(task_id)}, {"$set": updated_task})  # Ensure the collection name is 'task'

    return jsonify({"id": task_id, **updated_task}), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = mongo.db.task.delete_one({"_id": ObjectId(task_id)})  # Ensure the collection name is 'task'

    if result.deleted_count == 0:
        return jsonify({'message': 'Task not found'}), 404

    return jsonify({'message': 'Task deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
