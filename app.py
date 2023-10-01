"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from secret import secret_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = secret_key
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# ********* API routes ********** #

@app.route('/api/cupcakes')
def show_all_cupcakes():
    """returns json object of all cupcakes."""

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<cupcake_id>')
def show_single_cupcake(cupcake_id):
    """returns json object of single cupcake instance"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def add_new_cupcake():
    """sends request to add new cupcake."""

    new_cupcake = Cupcake(
            flavor= request.json.get('flavor'),
            size= request.json.get('size'),
            rating= request.json.get('rating'),
            image = request.json.get('image')
        )
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """updates particular cupcake given cupcake_id"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """deletes cupcake from db. Returns deleted status"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")

# ********* UI routes ******** #

@app.route('/')
def show_home():
    """renders static page for requesting API info and posting new cupcakes."""

    return render_template("main.html")