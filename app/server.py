from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import request
import os

file_path = os.path.abspath(os.getcwd())+"\Articles.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
db = SQLAlchemy(app)
CORS(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(96), unique=False)
    email = db.Column(db.String(96), unique=False)
    

@app.route("/")
def server_info():
    return jsonify({
        "server":"Mi aplicacion"
    })
    
@app.route("/articles/",methods=["POST"])
def new_article():
    
    json = request.get_json()
    email = json.get("email")
    name = json.get("name")
    new_article = Article()
    new_article.name = name
    new_article.email = email
    
    db.session.add(new_article)
    db.session.commit()
    
    return jsonify({"id":new_article.id}),201
    
@app.route("/article/<id>")
def get_article(id):
    article= Article.query.filter_by(id = id).first()
    
    return jsonify({"id": article.id,
                    "name": article.name,
                    "email": article.email
                   } 
                  )

@app.route("/articles/")
def list_articles():
    articles = Article.query.all()
    
    return jsonify([ {"id": x.id,
                      "name": x.name,
                      "email": x.email,
                     } 
                     for x in articles
                   ]
                  )


@app.route("/article/<id>", methods=["PUT"])
def update_article(id):
    
    article = Article.query.filter_by(id=id).first()
    
    if article is None:
        return jsonify({'message':'El articulo no existe'}),404
    
    json  = request.get_json(force=True)
    
    article.name = json.get("name")
    article.email = json.get("email")
    
    db.session.add(article)
    db.session.commit()
    
    return jsonify({"id": article.id,
                    "name": article.name,
                    "email": article.email
                   } )
    
if __name__ == "__main__":
    db.create_all()
    app.run(port=3000,host="0.0.0.0")