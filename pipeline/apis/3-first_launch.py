#!/usr/bin/env python3
"""Task 3. First launch"""
import requests
from datetime import datetime


def get_launch_info():
    """Displays the first launch  from the SpaceX API."""
    response = requests.get("https://api.spacexdata.com/v4/launches")
    data = response.json()

    # Sort the launches by date
    sorted_launches = sorted(data, key=lambda x: x['date_unix'])

    # Get the first launch
    first_launch = sorted_launches[0]

    launch_name = first_launch['name']
    date = datetime.fromtimestamp(
        first_launch['date_unix']).strftime('%Y-%m-%d %H:%M:%S')
    rocket_response = requests.get(
        "https://api.spacexdata.com/v4/rockets/" + first_launch['rocket'])
    rocket_name = rocket_response.json()['name']
    launchpad_response = requests.get(
        "https://api.spacexdata.com/v4/launchpads/" + first_launch[
            'launchpad'])
    launchpad_data = launchpad_response.json()
    launchpad_name = launchpad_data['name']
    launchpad_locality = launchpad_data['locality']

    print("{} ({}) {} - {} ({})".format(
        launch_name, date, rocket_name, launchpad_name, launchpad_locality))


if __name__ == '__main__':
    get_launch_info()
