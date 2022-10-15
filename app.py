from flask import Flask
from flask_cors import CORS
from database import engine


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def Hello():
    return '<h1>Olá, Sejam bem vindos à CarFord!</h1>'

if __name__ == '__main__':
    app.run(debug=True)