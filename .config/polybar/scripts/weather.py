#!/usr/bin/env python

import json
import requests
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    lat = 40.659478
    long = -73.606784
    api_key = open(dir_path+"/weather.API_KEY").read().strip()

    try:
        response = requests.get(
           f"https://api.darksky.net/forecast/{api_key}/{lat},{long}"
        )
        response.raise_for_status()
        weather = response.json()["currently"]
        desc = weather["summary"]
        humid = int(100*weather["humidity"])
        temp = int(weather["temperature"])
        icons = {
            "clear-day":"",
            "clear-night":"",
            "partly-cloudy-day":"杖",
            "partly-cloudy-night":"",
            "cloudy":"",
            "rain":"",
            "showers-day":"",
            "showers-night":"",
            "sleet":"",
            "rain-snow":"",
            "rain-snow-showers-day":"ﭽ",
            "rain-snow-showers-night":"ﭽ",
            "snow":"",
            "snow-showers-day":"",
            "snow-showers-night":"",
            "wind":"",
            "fog":"",
            "thunder":"",
            "thunder-rain":"",
            "thunder-showers-day":"",
            "thunder-showers-night":"",
            "hail":"晴",
        }
        icon = icons.get(weather["icon"].lower(), f"[{weather['icon']}]")
        return f"{icon} {desc} {humid} {temp}°F"
    except requests.exceptions.HTTPError as errh:
        return "HTTP Response Error"
    except requests.exceptions.ConnectionError as errc:
        return "No connection"
    except requests.exceptions.Timeout as errt:
        return "Timeout error"
    except requests.exceptions.RequestException as err:
        return "Other Error"


if __name__ == "__main__":
    print(main())
