from src import db

class CityName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"City Name{self.city_name}"