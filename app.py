from flask import Flask, render_template
import requests
import time
import os
from datetime import date, datetime

app = Flask(__name__, template_folder='templates')

@app.route("/")
def check_hollow_knight_release_date():
    
    # Steam API parameters
    app_id = 1030300 # Hollow Knight app ID

    # Send a request to the Steam Store API to retrieve the app details
    url = f"https://store.steampowered.com/api/appdetails/?appids={app_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"cc": "us", "l": "en"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Extract the release date or determine if it's TBA
    if str(app_id) in data:
        app_data = data[str(app_id)]
        if app_data["success"]:
            game_name = app_data["data"]["name"]
            release_date = app_data["data"].get("release_date", {}).get("date", "To be announced")
        else:
            game_name = "Hollow Knight: Silksong"
            release_date = "To be announced"
    else:
        game_name = "Hollow Knight: Silksong"
        release_date = "To be announced"

    # Compare the release date with the current date
    current_date = date.today().strftime("%Y-%m-%d")

    if release_date == "To be announced":
        timez, message = time.ctime(), f"Today's not the day, {game_name} is still on TBA"
    else:
        # Convert release_date and current_date to datetime objects
        release_date_obj = datetime.strptime(release_date, "%b %d, %Y").date()
        current_date_obj = datetime.strptime(current_date, "%Y-%m-%d").date()

        if release_date_obj <= current_date_obj:
            timez, message = time.ctime(), f"{game_name} has been released on {release_date}"
        else:
            timez, message = time.ctime(), f"{game_name} release date is set for {release_date}."

    return render_template("index.html", message=message, timez=timez)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)