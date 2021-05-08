from flask_sqlalchemy import SQLAlchemy

sqldb = SQLAlchemy()

class Article(sqldb.Model):
    
    __tablename__ = 'articulo'
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    name = sqldb.Column(sqldb.String(96), unique=False)
    email = sqldb.Column(sqldb.String(96), unique=False)