#!/usr/bin/python

import sys
import datetime
from algorithms import randomalgorithm, greedyratio
from data import dataloader
from classes import classes
from scripts import graph, helpers
from copy import copy, deepcopy

from flask import Flask, render_template, Response, jsonify
import time

# necessary for this script: pip install matplotlib
# future ref: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

app = Flask(__name__, template_folder="visualisation")


@app.route("/")
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py integer")
        sys.exit(1)

    # load data
    ship_data = "data/spacecrafts.csv"
    cargo_data = "data/CargoList1.csv"
    inventory = dataloader.load_data(ship_data, cargo_data)

    # if only 4 ships needed:
    # print("2x dict space inkorten")
    # print(inventory.dict_space)
    # inventory.dict_space = inventory.dict_space[:4]
    # print(inventory.dict_space)

    print('{}: Start random algorithm...'.format(datetime.datetime.now().strftime("%H:%M:%S")))

    costs_list = []
    parcel_amount_list = []

    repetitions = int(sys.argv[1])

    # hier een ifje om te splitsen per algoritme obv command-line arguments

    solutions = greedyratio.greedy_ratio(inventory, repetitions)
    # solutions = randomalgorithm.random_algorithm(inventory, repetitions)

    # collect all parcel amounts in list and determine highest
    for solution in solutions:
        # print(type(solution.total_costs))
        parcel_amount_list.append(solution.parcel_amount)
    max_parcel_amount = max(parcel_amount_list)

    # continue with solutions with max parcel amount
    parcel_checked_solutions = []
    for solution in solutions:
        if solution.parcel_amount is max_parcel_amount:
            parcel_checked_solutions.append(deepcopy(solution))

    # collect all costs of remaining solutions in list and determine lowest
    for solution in parcel_checked_solutions:
        costs_list.append(solution.total_costs)
    # print(len(costs_list), costs_list)
    min_costs = min(costs_list)
    # print("mcl", min_costs, type(min_costs))

    # save solution(s) with lowest cost
    best_solutions = []
    for solution in parcel_checked_solutions:
        if solution.total_costs is min_costs:
            best_solutions.append(deepcopy(solution))

    print('{}: Finished running {} times.'.format(datetime.datetime.now().strftime("%H:%M:%S"), sys.argv[1]))

    print("Maximum amount of parcels in ship: {}".format(max_parcel_amount))
    print("Corresponding costs: {}". format(min_costs))

    # visualize which ships contain which parcels in best solution(s)
    for solution in best_solutions:
        solution_statement = helpers.visualizeParcelsPerShip(solution)
        for element in solution_statement:
            print(element)

        d = {}
        for i in range(4):
            current_weight = solution.dict_space[i].current_weight
            current_volume = solution.dict_space[i].current_volume

            max_weight = solution.dict_space[i].max_weight
            max_volume = solution.dict_space[i].max_volume

            weight = current_weight / max_weight * 100
            volume = current_volume / max_volume * 100

            weight_send = format(weight, '.2f')
            volume_send = format(volume, '.2f')

            d["weight" + str(i)] = weight_send
            d["volume" + str(i)] = volume_send
            d["total_amount" + str(i)] = len(solution_statement[i]["content"])
            d["parcels" + str(i)] = solution_statement[i]["content"]

    # plot parcel amounts of all found solutions in histogram
    graph.barchart([solution.parcel_amount for solution in solutions])

    return render_template("visual.html", d=d)

if __name__ == "__main__":
    app.run(debug=True)
