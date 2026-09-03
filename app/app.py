from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola desde aqui"
app.run(host="0.0.0.0", port=5000)