from flask import Flask

app = Flask(__name__)

@app.route('/emisor')
def holamundo():
    return 'El emisor'

@app.route('/receptor')
def receptor():
    return 'El receptor'

if __name__ == '__main__':
    app.run(port=8443)