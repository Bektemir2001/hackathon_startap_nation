from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from api.v1 import bp as routes_bp

app.register_blueprint(routes_bp, url_prefix='/api/v1')



if __name__ == '__main__':
    app.run(debug=True)
