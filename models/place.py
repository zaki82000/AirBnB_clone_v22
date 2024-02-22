#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Float, Integer, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey(
        "places.id"), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey(
        "amenities.id"), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ Place class """

    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
            "Review", cascade="all, delete", backref="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Get all reviews in the current place"""
            from models import storage
            review_output = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_output.append(review)
            return review_output

        @property
        def amenities(self):
            """getter"""
            from models import storage
            amenity_output = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_output.append(amenity)
            return amenity_output

        @amenities.setter
        def amenities(self, amenity):
            """Amenity Setter"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)