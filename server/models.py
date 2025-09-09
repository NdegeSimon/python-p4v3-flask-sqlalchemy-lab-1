from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Integer, Float, String
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(Integer, primary_key=True)
    magnitude = db.Column(Float, nullable=False)
    location = db.Column(String(100), nullable=False)
    year = db.Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

    def to_dict(self):
        return {
            "id": self.id,
            "magnitude": self.magnitude,
            "location": self.location,
            "year": self.year,
        }
