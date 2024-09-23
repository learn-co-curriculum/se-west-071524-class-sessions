import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata, engine_options={"echo": True})


class TimestampMixin:
    create_at = db.Column(db.DateTime, server_default=db.func.now())
    update_at = db.Column(db.DateTime, onupdate=db.func.now())


OPERATION_SIZES = ["small", "medium", "large", "family", "corporate"]


class Producer(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "producers"

    id = db.Column(db.Integer, primary_key=True)
    founding_year = db.Column(db.Integer)
    name = db.Column(db.String)
    region = db.Column(db.String)
    operation_size = db.Column(db.String)
    image = db.Column(db.String)

    serialize_rules = ("-create_at", "-update_at")

    @validates("name")
    def name_required(self, key, name):
        if not name:
            raise ValueError("Must provide a name")
        return name

    @validates("founding_year")
    def founding_yr_range(self, key, year):
        if not 1900 < year < datetime.datetime.now().year:
            raise ValueError("Year must be between 1900 and present")
        return year

    @validates("operation_size")
    def op_size_type(self, key, operation):
        if operation not in OPERATION_SIZES:
            raise ValueError(
                'Operation must be one of "small", "medium", "large", "family", "corporate"'
            )
        return operation

    def __repr__(self):
        return f"<Producer {self.id}>"


class Cheese(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "cheeses"

    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String)
    is_raw_milk = db.Column(db.Boolean)
    production_date = db.Column(db.DateTime)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    producer_id = db.Column(db.Integer, db.ForeignKey("producers.id"))

    @validates
    def production_in_past(self, key, date):
        if not date < datetime.datetime.now():
            raise ValueError("Cheeses must be produced before today")
        return date

    @validates
    def price_range(self, key, price):
        if not 1.00 <= price <= 45.00:
            raise ValueError("Price must be between 1.00 and 45.00")
        return price

    def __repr__(self):
        return f"<Cheese {self.id}>"
