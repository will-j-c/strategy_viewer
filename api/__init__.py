from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    # app.config.from_object()

    from api.pairs import bp as pairs_bp
    app.register_blueprint(pairs_bp)

    return app
