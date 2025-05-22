from flask import Flask, request, jsonify
import uuid # For generating unique IDs for tasks

app = Flask(__name__)

# In-memory storage for tasks
# In a real application, this would be a database
tasks = []

# Example initial tasks (for testing)
tasks.append({
    'id': str(uuid.uuid4()), # Generate a unique ID
    'title': 'Learn Flask',
    'description': 'Read Flask documentation and tutorials.',
    'done': False
})
tasks.append({
    'id': str(uuid.uuid4()),
    'title': 'Build Calculator',
    'description': 'Complete Project 1 and push to GitHub.',
    'done': True
})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Retrieves all tasks.
    """
    return jsonify(tasks)

@app.route('/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Retrieves a single task by its ID.
    """
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404 # 404 Not Found

@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Adds a new task.
    Requires JSON payload: {"title": "...", "description": "..."}
    """
    if not request.json or not 'title' in request.json:
        return jsonify({'message': 'Bad Request: Missing title or JSON payload'}), 400 # 400 Bad Request

    new_task = {
        'id': str(uuid.uuid4()), # Generate a unique ID
        'title': request.json['title'],
        'description': request.json.get('description', ""), # Description is optional
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201 # 201 Created

@app.route('/tasks/<string:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Updates an existing task by its ID.
    Requires JSON payload with fields to update (title, description, done).
    """
    task_found = None
    for task in tasks:
        if task['id'] == task_id:
            task_found = task
            break

    if not task_found:
        return jsonify({'message': 'Task not found'}), 404

    if not request.json:
        return jsonify({'message': 'Bad Request: Missing JSON payload'}), 400

    # Update fields if they exist in the request JSON
    task_found['title'] = request.json.get('title', task_found['title'])
    task_found['description'] = request.json.get('description', task_found['description'])
    
    # Special handling for boolean 'done' status
    if 'done' in request.json and isinstance(request.json['done'], bool):
        task_found['done'] = request.json['done']
    elif 'done' in request.json: # If 'done' is present but not boolean
        return jsonify({'message': 'Bad Request: "done" must be a boolean'}), 400

    return jsonify(task_found)

@app.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Deletes a task by its ID.
    """
    global tasks # Declare intent to modify the global tasks list
    
    # Find the task by ID
    task_to_delete_index = None
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            task_to_delete_index = i # Store the index
            break
            
    if task_to_delete_index is None: # Use 'is None' for clarity with index 0
        return jsonify({'message': 'Task not found'}), 404
    
    # Remove the task using its index
    del tasks[task_to_delete_index]
    
    return jsonify({'message': 'Task deleted successfully'}), 200 # 200 OK

# To run the app (useful for local development on phone)
if __name__ == '__main__':
    # You might need to change the host if Termux requires a specific IP.
    # '0.0.0.0' makes it accessible from any device on your local network.
    # In Termux, you might only need app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)

