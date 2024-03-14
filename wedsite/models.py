from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<Product %r>' % self.product_name
    

class BestSeller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<BestSeller %r>' % self.product_name
    
class BestOffers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<Product %r>' % self.product_name
    

class Instagram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_picture = db.Column(db.String(1000), nullable=False)



    def __str__(self):
        return '<Product %r>' % self.product_picture
    

class ProductPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<Product %r>' % self.product_name
    

