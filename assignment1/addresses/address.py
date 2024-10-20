from flask import Flask, jsonify, request

app = Flask(__name__)

addresses = [
    {"id": 1, "street": "123 Main St", "city": "Istanbul", "client_id": 1},
    {"id": 2, "street": "456 Side St", "city": "Ankara", "client_id": 2}
]

@app.route('/addresses', methods=['GET'])
def get_addresses():
    return jsonify(addresses), 200

@app.route('/addresses/<int:id>', methods=['GET'])
def get_address(id):
    address = next((a for a in addresses if a['id'] == id), None)
    return jsonify(address) if address else ('', 404)

@app.route('/addresses', methods=['POST'])
def add_address():
    data = request.json
    new_address = {"id": len(addresses) + 1, "street": data['street'], "city": data['city'], "client_id": data['client_id']}
    addresses.append(new_address)
    return jsonify(new_address), 201

@app.route('/addresses/<int:id>', methods=['PUT'])
def update_address(id):
    address = next((a for a in addresses if a['id'] == id), None)
    if not address:
        return '', 404
    data = request.json
    address.update(data)
    return jsonify(address), 200

@app.route('/addresses/<int:id>', methods=['DELETE'])
def delete_address(id):
    global addresses
    addresses = [a for a in addresses if a['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)