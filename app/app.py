from flask import Flask

AWS_ACCESS_KEY_ID= ${{ secrets.AWS_ACCESS_KEY_ID }}

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Fortress Flask App"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)