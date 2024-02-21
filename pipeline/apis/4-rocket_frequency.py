#!/usr/bin/env python3
"""Task 4. How many by rocket?"""
import requests
from collections import defaultdict


def get_launches_per_rocket():
    """Script that displays the number of launches per rocket"""
    launches_per_rocket = defaultdict(int)

    response = requests.get("https://api.spacexdata.com/v3/launches")
    data = response.json()

    for launch in data:
        rocket_name = launch['rocket']['rocket_name']
        launches_per_rocket[rocket_name] += 1

    sorted_rockets = sorted(
        launches_per_rocket.items(), key=lambda x: (-x[1], x[0]))

    for rocket, launches in sorted_rockets:
        print("{}: {}".format(rocket, launches))


if __name__ == '__main__':
    get_launches_per_rocket()
