from flask import Flask
from interfaces.routes.main import main
import os

app = Flask(
    __name__,
    static_folder='static',
    template_folder=os.path.join("interfaces", "templates")
)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
