from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

WEATHER_API_KEY = "a98ed90b5ec17d90c279bfefb58f1ad6"
UNSPLASH_ACCESS_KEY = "9GNAL6pCKkvtc4ku74VuSrZf0ioz8C_6FqGyEUyNlL0"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def get_weather():
    data = request.json
    city = data.get("city")
    unit = data.get("unit", "metric")

    # Fetch weather
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units={unit}"
    weather_response = requests.get(weather_url).json()

    if weather_response.get("cod") != 200:
        return jsonify({"error": "City not found"}), 404

    # Fetch background image
    image_url = f"https://api.unsplash.com/photos/random?query={city}&client_id={UNSPLASH_ACCESS_KEY}"
    image_response = requests.get(image_url).json()
    bg_url = image_response.get("urls", {}).get("regular", "")

    return jsonify({
        "city": weather_response["name"],
        "temperature": weather_response["main"]["temp"],
        "description": weather_response["weather"][0]["description"],
        "bg_url": bg_url
    })

if __name__ == "__main__":
    app.run(debug=True)
