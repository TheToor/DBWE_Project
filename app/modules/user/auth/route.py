from flask import Blueprint, flash, make_response, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from app.forms.login.UserSignupForm import UserSignupForm
from app.forms.login.UserLoginForm import UserLoginForm
from .controller import AuthenticationController


auth_bp = Blueprint('auth', __name__)
auth_controller = AuthenticationController()
@auth_bp.route('/', methods=['GET'])
@auth_bp.route('/login', methods=['GET'])
def login():
  user_login_form = UserLoginForm()
  return render_template('user/login.html', form=user_login_form)

@auth_bp.route('/login', methods=['POST'])
def login_post():
  user_login_form = UserLoginForm()
  if not user_login_form.validate():
    return redirect(url_for('auth.login'))
  
  user = auth_controller.login(user_login_form.email.data, user_login_form.password.data)
  if user is None:
    flash('Invalid email or password')
    return redirect(url_for('auth.login'))
  else:
    login_user(user, remember=user_login_form.remember_me.data)
    return redirect(url_for('index.index'))
      
@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))

@auth_bp.route('/signup', methods=['GET'])
def signup():
  user_signup_form = UserSignupForm()
  return render_template('user/signup.html', form=user_signup_form)

@auth_bp.route('/signup', methods=['POST'])
def signup_post():
  user_signup_form = UserSignupForm()
  if not user_signup_form.validate():
    return redirect(url_for('auth.signup'))

  if auth_controller.try_create_user(user_signup_form.email.data, user_signup_form.name.data, user_signup_form.password.data):
    return redirect(url_for('auth.login'))
  else:
    flash('Email address already exists')
    return redirect(url_for('auth.signup'))