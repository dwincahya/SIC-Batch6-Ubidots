from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Inisialisasi Flask
app = Flask(__name__)

# Koneksi ke MongoDB Atlas
client = MongoClient("mongodb+srv://juanditoyeftapriatama:jyp120707@cluster0.rmdy1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["sensor_data"]
collection = db["readings"]

# Route untuk menerima data dari ESP32
@app.route('/api/sensor', methods=['POST'])
def receive_data():
    data = request.json
    data["timestamp"] = datetime.utcnow()  # Tambahkan waktu saat data diterima
    collection.insert_one(data)
    return jsonify({"status": "Data berhasil disimpan"}), 200

# Route untuk cek data masuk
@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200

# Jalankan server Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
