from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur mon application de migration cloud !",
        "status": "Opérationnelle",
        "timestamp": datetime.now().isoformat(),
        "division": "Corporate Functions Technology",
        "Author": "Moreau"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)