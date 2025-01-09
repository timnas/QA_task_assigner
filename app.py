from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/send-skype-message', methods=['POST'])
def send_skype_message():
    try:
        # Run the send_skype_message.py script
        result = subprocess.run(["python", "send_skype_message.py"], capture_output=True, text=True, check=True)
        return jsonify({"status": "success", "output": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "error": e.stderr}), 500

if __name__ == '__main__':
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
