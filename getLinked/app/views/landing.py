from flask import Blueprint, flash, redirect, render_template, request, session, url_for

landing = Blueprint("landing", __name__)

@landing.route("/")
def landing_page():
    return render_template("_landing.html")

@landing.route("/register")
def register_page():
    return render_template("_register.html")

@landing.route("/contact")
def contact_page():
    return render_template("_contact.html")