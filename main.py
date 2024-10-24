from flask import Flask
from safe_food import get_data, get_data2
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})

@app.route('/api/data', methods=['GET'])
def get_data_route():
    print("Received a request to /api/data")
    return get_data()  

@app.route('/api/data2', methods=['GET'])
def get_data2_route():
    print("Received a request to /api/data2")
    return get_data2()  

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
#     get_data2_route()
