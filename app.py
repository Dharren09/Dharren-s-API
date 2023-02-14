from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/age")
def age():
    # Code to retrieve Dharren's age
    age = 25
    return jsonify({"age": age})


@app.route("/best_friend")
def best_friend():
    # Code for retrieving Dharren's Bestfriend's name
    Best_Friend = "Jey"
    return jsonify({"best_friend": best_friend})


@app.route("/car")
def car():
    # Code to retrieve Dharren's favorite car
    car = "Jeep Wrangler 2023"
    return jsonify({"car": car})


@app.route("/baby")
def baby():
    # Code to retrieve Dharren's Baby name
    baby = "Elior Neriah Truth Kwagala"
    return jsonify({"baby": baby})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
