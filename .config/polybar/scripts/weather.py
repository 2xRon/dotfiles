#!/usr/bin/env python

import json
import urllib
import urllib.parse
import urllib.request
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    zip_code = "Queens County, US"
    with open(dir_path+"/weather.API_KEY") as api_file:
        api_key = api_file.read().strip()

    try:
        data = urllib.parse.urlencode(
            {"q": zip_code, "appid": api_key, "units": "imperial"}
        )
        weather = json.loads(
            urllib.request.urlopen(
                "http://api.openweathermap.org/data/2.5/weather?" + data
            ).read()
        )
        desc = weather["weather"][0]["description"].capitalize()
        icon_key = weather["weather"][0]["main"].capitalize()
        icons = {
            "Thunderstorm": "",
            "Drizzle": "",
            "Rain": "",
            "Snow": "",
            "Mist": "",
            "Smoke": "",
            "Haze": "",
            "Dust": "",
            "Fog": "",
            "Sand": "",
            "Dust": "",
            "Ash": "",
            "Squall": "",
            "Tornado": "",
            "Clear": "",
            "Clouds": "",
        }
        icon = icons.get(icon_key, "")
        temp = int(weather["main"]["temp"])
        humid = int(weather["main"]["humidity"])
        return f"{icon} {desc} {humid} {temp}°F"
    except Exception as e:
        return "" + str(e)


if __name__ == "__main__":
    print(main())
