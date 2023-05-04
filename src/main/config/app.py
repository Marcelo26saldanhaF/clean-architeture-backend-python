from flask import Flask
from src.main.routes import api_routes_bp



app=Flask(__name__)

#register blueprint
app.register_blueprint(api_routes_bp)



