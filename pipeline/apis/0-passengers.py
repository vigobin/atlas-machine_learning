#!/usr/bin/env python3
"""Can I join?"""
import requests


def availableShips(passengerCount):
    """By using the Swapi API, create a method that returns the list of ships
        that can hold a given number of passengers:
    Don’t forget the pagination.
    If no ship available, return an empty list."""
    ships = []
    page = 1

    while True:
        response = requests.get(
            f"https://swapi-api.hbtn.io/api/starships/?page={page}")
        data = response.json()

        # Check each ship
        for ship in data['results']:
            if ship['passengers'] not in ['unknown', 'n/a']:
                if int(ship['passengers'].replace(',', '')) >= passengerCount:
                    ships.append(ship['name'])

        if data['next'] is not None:
            page += 1
        else:
            break

    return ships
