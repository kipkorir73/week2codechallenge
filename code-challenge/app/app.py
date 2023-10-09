from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def homepage():
    return 'Welcome to the Superheroes API!'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.serialize())
    return jsonify({"message": "Hero not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.serialize() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.serialize())
    return jsonify({"message": "Power not found"}), 404

@app.route('/', methods=['POST'])
def create_hero_power():
    data = request.json
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero:
        return jsonify({"message": "Hero not found"}), 404
    if not power:
        return jsonify({"message": "Power not found"}), 404

    hero_power = HeroPower(hero=hero, power=power, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero.serialize()), 201

if __name__ == '__main__':
    app.run(port=5555)
