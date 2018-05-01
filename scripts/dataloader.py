#!/usr/bin/python

import csv
from classes import classes

def load_data(ship_data, cargo_data):
    """Loads a csv file as an ordered dict.

    Usage: 
    loaded_data = load_data('csv_data.csv')
    """

    ship_counter = 0
    parcel_counter = 0

    # open the csv file containing information about ships
    with open(ship_data) as csv_data:
        reader = csv.DictReader(csv_data)
        data_space = [r for r in reader]
    
    # create a list to hold spaceship objects
    list_space = []

    # create spaceship objects and append to the list
    for ship in data_space:
        spaceship = classes.Spaceship(ship_counter, ship["mass"], ship["payload mass"], ship["payload volume"], ship["base cost"], ship["ftw"])
        spaceship.current_weight = 0
        spaceship.current_volume = 0
        ship_counter += 1
        list_space.append(spaceship)

    # open the csv file containing cargo list
    with open(cargo_data) as parcel_data:
        reader = csv.DictReader(parcel_data)
        data_parcel = [r for r in reader]
    
    # create a list to hold all the parcel objects
    list_parcel = []

    # create parcel objects and append to the list
    for unit in data_parcel:
        parcel = classes.Parcel(parcel_counter, unit["weight (kg)"], unit["volume (m^3)"])
        parcel_counter += 1
        list_parcel.append(parcel)

    # store both lists
    data = [list_space, list_parcel]
    
    return data
