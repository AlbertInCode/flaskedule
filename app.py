from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes import main

app = Flask(__name__)
app.register_blueprint(main.main)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
