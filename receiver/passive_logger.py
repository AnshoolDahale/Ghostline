# receiver/passive_logger.py
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def log():
    print("[+] Got DoH Query:", request.args)
    return "", 200

app.run(host="0.0.0.0", port=8080)
