from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
   { "label": "Despertar", "done": False },
    { "label": "Hacer ejercicio", "done": False },
    { "label": "Leer", "done": False },
    { "label": "Estudiar", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    tareas = jsonify(todos)
    return tareas

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    if position < 0 or position >= len(todos):
        return jsonify({ "error": "Invalid position" }), 400
    
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)