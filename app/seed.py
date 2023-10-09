# seed.py

from app import app, db
from models import Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        # Create Heroes
        hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
        hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
        hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

        # Create Powers
        power1 = Power(name="super strength", description="gives the wielder super-human strengths")
        power2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")

        # Create HeroPowers
        hero_power1 = HeroPower(strength="Strong", hero=hero1, power=power1)
        hero_power2 = HeroPower(strength="Average", hero=hero1, power=power2)
        hero_power3 = HeroPower(strength="Weak", hero=hero2, power=power1)

        # Add data to the database
        db.session.add_all([hero1, hero2, hero3, power1, power2, hero_power1, hero_power2, hero_power3])
        db.session.commit()

        print("Data has been seeded.")
