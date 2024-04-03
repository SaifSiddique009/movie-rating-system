from flask import Blueprint, render_template

# Setup blueprint for views
auth = Blueprint('auth', __name__)

# Login route
@auth.route('/login', methods = ['GET', 'POST'])
def login():
  return render_template("login.html", boolean = False)

# Sign-up route
@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
  return render_template("sign_up.html", boolean = False)
  
# Log out route
@auth.route('/logout')
def logout():
  return "<p>Log Out</p>"