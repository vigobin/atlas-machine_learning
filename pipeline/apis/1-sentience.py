#!/usr/bin/env python3
"""Task 1. Where I am?"""
import requests


def sentientPlanets():
    """Create a method that returns the list of names of the home planets of
        all sentient species.
        sentient type is either in the classification or designation
            attributes."""
    planets = []
    page = 1

    while True:
        response = requests.get(
            "https://swapi-api.hbtn.io/api/species/?page={}".format(page))
        data = response.json()

        for species in data['results']:
            if 'sentient' in species[
                'classification'].lower() or 'sentient' in species[
                    'designation'].lower():
                if species['homeworld'] is not None:
                    planet_response = requests.get(species['homeworld'])
                    planet_data = planet_response.json()

                    planets.append(planet_data['name'])

        if data['next'] is not None:
            page += 1
        else:
            break

    return planets
