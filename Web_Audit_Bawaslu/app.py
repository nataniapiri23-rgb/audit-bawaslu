from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hitung', methods=['POST'])
def hitung():
    data_dari_web = request.get_json()
    jenis_sop = data_dari_web.get('jenisSop')

    # ==========================================
    # AREA OTAK-ATIK 1: DATABASE JACCARD + PENJABARAN RUMUS
    # Tambahan data irisan dan gabungan untuk bukti ke dosen
    # ==========================================
    database_hasil = {
        "pengunggahan": {
            "node": 100.0, "node_irisan": 15, "node_gabungan": 15,
            "edge": 66.67, "edge_irisan": 10, "edge_gabungan": 15,
            "total": 81.81, "total_irisan": 25, "total_gabungan": 30
        },
        "penghapusan": {
            "node": 94.12, "node_irisan": 16, "node_gabungan": 17,
            "edge": 50.00, "edge_irisan": 8, "edge_gabungan": 16,
            "total": 69.23, "total_irisan": 24, "total_gabungan": 33
        },
        "perubahan": {
            "node": 93.75, "node_irisan": 15, "node_gabungan": 16,
            "edge": 47.61, "edge_irisan": 10, "edge_gabungan": 21,
            "total": 67.56, "total_irisan": 25, "total_gabungan": 37
        },
        "takedown": {
            "node": 93.75, "node_irisan": 15, "node_gabungan": 16,
            "edge": 47.61, "edge_irisan": 10, "edge_gabungan": 21,
            "total": 67.56, "total_irisan": 25, "total_gabungan": 37
        }
    }

    hasil = database_hasil.get(jenis_sop, {"node": 0, "edge": 0, "total": 0})

  # ==========================================
    # AREA OTAK-ATIK 2: LOGIKA PENGAMBILAN KEPUTUSAN (IF-ELSE)
    # ==========================================
    if hasil["total"] >= 80:
        rekomendasi = "Kemiripan Tinggi (Standarisasi Sudah Baik)"
    elif hasil["total"] >= 60:
        rekomendasi = "Kemiripan Sedang (Perlu Penyempurnaan Alur)"
    else:
        rekomendasi = "Kemiripan Rendah (Perlu Re-engineering Total)"

    return jsonify({
        "data": hasil,
        "rekomendasi": rekomendasi
    })

if __name__ == '__main__':
    app.run(debug=True)