import os
import markdown
from flask import Flask, jsonify
from flask_restful import Resource, Api
from CafeBase import CafeBase
from webargs import fields
from webargs.flaskparser import use_kwargs

# Set up the Flask API
app = Flask(__name__)
api = Api(app)


# Function to create and manage the CafeBase database
def get_db():
    global base
    if base is None:
        print("API: Initiated Database")
        base = CafeBase()
    return base


# An index page with the readme for the API
@app.route("/cafeapi")
def index():
    with open(os.path.dirname(app.root_path) + '/CafeBackend/README.md') as file:
        content = file.read()
        return markdown.markdown(content)


# Parameters
args_list = {
    'day': fields.Int(
        required=True,
        validate=lambda v: v in range(0, 7),
    ),
}


# Branch of the directory to get queries
class Food(Resource):
    @use_kwargs(args_list, location="query")
    def get(self, day):
        print(f'Incoming Request: day={day}')
        return get_db().day_menu(day)


# Handle the errors
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid Request"])
    if headers:
        return jsonify({'errors': messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


if __name__ == '__main__':
    # Initialize the database
    base = None
    get_db()

    # Add the Food branch to /cafeapi/food
    api.add_resource(Food, '/cafeapi/food')
    print("API: Added food resource")

    # Run the app
    print("API: Initiating App")
    app.run(host='0.0.0.0', port='7777')

    print("API: Exited App")
