from flask import Flask

app = Flask(__name__)

@app.route('/city', methods=['GET'])
def get_city():
    return 'Hello, World!'


@app.route('/city', methods=['POST'])
def post_city():
    return 'Hello, World!'


@app.route('/_health', methods=['GET'])
def health():
    return 'OK'