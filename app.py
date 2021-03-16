from flask import Flask , jsonify , request
from data import final_dict
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({"data":final_dict,"message":"success"}),200
if __name__ == "__main__":
    app.run()
