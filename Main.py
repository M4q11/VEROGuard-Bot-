import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "VEROGuard Backend is active!"})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "online": True, 
        "bot": "VEROGuard",
        "app_id": "1440164384566673610"
    })

@app.route('/api/command', methods=['POST'])
def command():
    data = request.json or {}
    user_id = request.headers.get("X-Discord-User-Id", "Unknown User")
    action = data.get("action", "ping")
    
    return jsonify({
        "success": True,
        "message": f"VEROGuard processed action: {action}",
        "executor": user_id
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
