from flask import Flask, jsonify, request, json
from flask_restful import Api

from resources.todo import Todo

app = Flask(__name__)
api = Api(app)

@app.route('/update-data', methods=['POST'])
def update():
    info = request.get_json();
    Todo.construct_index("datos")
    return jsonify("ok"), 200

@app.route('/chat', methods=['POST'])
def chat():
    info = request.get_json();
    return jsonify(Todo.chatbot(info[0]['content'])), 200

if __name__ == "__main__":
  app.run()