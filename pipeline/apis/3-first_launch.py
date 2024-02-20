#!/usr/bin/env python3
"""Task 3. First launch"""
import requests
from datetime import datetime


def get_launch_info():
    """Displays the first launch  from the SpaceX API."""
    response = requests.get("https://api.spacexdata.com/v5/launches/")
    data = response.json()

    # Get the required information
    launch_name = data['name']
    date = datetime.fromtimestamp(
        data['date_unix']).strftime('%Y-%m-%d %H:%M:%S')
    rocket_response = requests.get(
        "https://api.spacexdata.com/v5/rockets/{}".format(data['rocket']))
    rocket_name = rocket_response.json()['name']
    launchpad_response = requests.get(
        "https://api.spacexdata.com/v5/launchpads/{}".format(
            data['launchpad']))
    launchpad_data = launchpad_response.json()
    launchpad_name = launchpad_data['name']
    launchpad_locality = launchpad_data['locality']

    # Print the information in the specified format
    print("{} ({}) {} - {} ({})".format(
        launch_name, date, rocket_name, launchpad_name, launchpad_locality))


if __name__ == '__main__':
    get_launch_info()
