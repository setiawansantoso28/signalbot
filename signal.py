from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8897035505:AAFvVklunaCmySKmdfPdw4eMSdByX2OT1BQ"
CHAT_ID = "@santaureatebot"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    text = f"""
📊 SIGNAL TRADING

📌 Symbol: {data.get('symbol')}
📈 Action: {data.get('action')}
💰 Entry: {data.get('entry')}
🛑 SL: {data.get('sl')}
🎯 TP: {data.get('tp')}
📊 RR: {data.get('rr')}
📡 Market: {data.get('market')}
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return {"status": "ok"}

app.run(host="0.0.0.0", port=5000)