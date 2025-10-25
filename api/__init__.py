from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.config.from_object()

    from api.pairs import bp as pairs_bp
    app.register_blueprint(pairs_bp)

    return app
