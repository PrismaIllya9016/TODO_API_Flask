from flask import Flask, jsonify, request
import json 
app = Flask(__name__) 


todos = [
    { "label": "My first task", "done": False },
]


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos), 200 

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print(todos)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 201  

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if len(todos)==0: 
        return 'No hay tareas para borrar'  
    if position>=len(todos):
        return 'No existe'
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)