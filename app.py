from flask import Flask
from database import db
from routes import incident_routes

# Application factory
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(incident_routes)

    # Home route
    @app.route('/')
    def home():
        return 'Incident Reporting API is running! 🚀'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)