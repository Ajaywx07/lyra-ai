import os
from flask import Flask, request, jsonify
import requests

GEMINI_API_KEY = "AIzaSyBxtjU1ka0y0tcTAVEgTpgyWcGdF2Qfp1o"
app = Flask(__name__)

@app.route('/generate_reply', methods=['POST'])
def generate_reply():
    try:
        data = request.get_json()
        sender = data.get('sender', 'Unknown')
        message = data.get('message', '')
        instruction = data.get('instruction', 'Normal chat')

        prompt = f"Sender: {sender}\nMessage: {message}\nInstruction: {instruction}\nReply naturally as Lyra."

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        
        response = requests.post(url, json=payload)
        ai_reply = response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
        
        return jsonify({"status": "success", "reply": ai_reply})
    except Exception as e:
        return jsonify({"status": "error", "reply": "Hi, I'm Lyra. Ajay is busy right now."}), 500

if __name__ == '__main__':
    # Cloud servers port environment variable se lete hain
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)