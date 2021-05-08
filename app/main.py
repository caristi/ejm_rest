from flask import Flask
from config import config
from app.articulo.Article import db

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    return app

enviroment = config['development']

app = create_app(enviroment)