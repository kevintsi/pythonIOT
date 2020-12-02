from flask import Flask, render_template, jsonify
import os, json

app = Flask(__name__)

hotels = json.load(open("Data/hotels.json"))

@app.route("/", methods=["GET"])
def index():
    """ 
    Get all hotels to display at the home page

    Returns:
        template
    """
    return render_template("index.htm", hotels=hotels)

@app.route("/hotel/<int:id>", methods=["GET"])
def get_hotel_by_id(id):
    """
    Get hotel by given id and display it in a template

    Args:
        id ([int]): Hotel's id

    Returns:
        template
    """
    hotel = None
    for value in hotels:
        if value.get("id") == id:
            hotel = value
            break
    return render_template("hotelDetail.htm", hotel=hotel)

@app.route("/hotel/name/<string:name>", methods=["GET"])
def get_hotel_by_name(name):
    hotels_list = []
    for value in hotels:
        if value.get("name").lower().startswith(name.lower()):
            hotels_list.append(value)
    return jsonify(hotels_list)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))