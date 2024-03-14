from flask import Blueprint, render_template, flash, redirect, request, jsonify
from .models import Product,BestOffers,Instagram, BestSeller, ProductPage
from . import db


views = Blueprint('views', __name__)

API_PUBLISHABLE_KEY = 'YOUR_PUBLISHABLE_KEY'

API_TOKEN = 'YOUR_API_TOKEN'


@views.route('/')
def index():
    items = Product.query.all()
    items_bestSeller = BestSeller.query.all()
    items_bestOffer = BestOffers.query.all()
    items_insta = Instagram.query.all()
    items_product = ProductPage.query.all()
    return render_template("index.html", items = items, 
                           items_bestSeller=items_bestSeller, 
                           items_bestOffer=items_bestOffer, 
                           items_insta = items_insta, 
                           items_product=items_product)


@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/product", methods=['GET', 'POST'])
def product():
    items = ProductPage.query.all()
    return render_template("product.html", items = items)


@views.route("/contact")
def contact():
    return render_template("contact.html")


@views.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



