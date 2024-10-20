from flask import Flask, jsonify, request

app = Flask(__name__)

clients = [
    {"id": 1, "name": "Client A", "balance": 1000},
    {"id": 2, "name": "Client B", "balance": 1500}
]

@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(clients), 200

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    client = next((c for c in clients if c['id'] == id), None)
    return jsonify(client) if client else ('', 404)

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.json
    new_client = {"id": len(clients) + 1, "name": data['name'], "balance": data['balance']}
    clients.append(new_client)
    return jsonify(new_client), 201

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    client = next((c for c in clients if c['id'] == id), None)
    if not client:
        return '', 404
    data = request.json
    client.update(data)
    return jsonify(client), 200

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    global clients
    clients = [c for c in clients if c['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)