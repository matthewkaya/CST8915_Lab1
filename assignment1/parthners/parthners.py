from flask import Flask, jsonify, request

app = Flask(__name__)

partners = [
    {"id": 1, "name": "Partner X", "client_id": 1},
    {"id": 2, "name": "Partner Y", "client_id": 2}
]

@app.route('/partners', methods=['GET'])
def get_partners():
    return jsonify(partners), 200

@app.route('/partners/<int:id>', methods=['GET'])
def get_partner(id):
    partner = next((p for p in partners if p['id'] == id), None)
    return jsonify(partner) if partner else ('', 404)

@app.route('/partners', methods=['POST'])
def add_partner():
    data = request.json
    new_partner = {"id": len(partners) + 1, "name": data['name'], "client_id": data['client_id']}
    partners.append(new_partner)
    return jsonify(new_partner), 201

@app.route('/partners/<int:id>', methods=['PUT'])
def update_partner(id):
    partner = next((p for p in partners if p['id'] == id), None)
    if not partner:
        return '', 404
    data = request.json
    partner.update(data)
    return jsonify(partner), 200

@app.route('/partners/<int:id>', methods=['DELETE'])
def delete_partner(id):
    global partners
    partners = [p for p in partners if p['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)