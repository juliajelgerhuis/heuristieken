import matplotlib.pyplot as plt
import os


def barchart(results):
    print(results)
    # os.remove("static/graph.png")

    # plot solutions in histogram
    plt.hist(results, color="red", align="right")
    plt.title = ("Solutions")
    plt.xlabel = ("Frequency")
    plt.ylabel = ("Amount of parcels")
    plt.savefig('static/graph.png')  
    plt.close()  