from flask import Blueprint, render_template, request, redirect, url_for, session
from . import db
import stripe

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/pro-license')
def pro_license():
    return render_template('pro_license.html')

@main.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    stripe.api_key = current_app.config['STRIPE_SECRET_KEY']
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Pro License',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('main.index', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('main.index', _external=True),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return str(e)

@main.route('/success')
def success():
    return render_template('success.html')

@main.route('/cancel')
def cancel():
    return render_template('cancel.html')
