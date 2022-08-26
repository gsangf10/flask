from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views, user_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp)

    return app