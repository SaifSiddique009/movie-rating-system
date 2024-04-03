from flask import Flask 

def create_app():
  app = Flask(__name__)
  # SECRET_KEY
  app.config['SECRET_KEY'] = 'FSDFSDFSsdfsdfsd sfsdfSDFS'

  # Import different routes
  from .views import views
  from .auth import auth 

  # Registering the blueprints
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix= '/')
  return app 
