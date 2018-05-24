# Heuristieken
Rebecca de Feijter, Jesse Haenen, Julia Jelgerhuis <br />
Case: Space Freight <br />
http://heuristieken.nl/wiki/index.php?title=Space_Freight

## Main goal
Ship parcels to the International Space Station (ISS) using 6 different types of spacecrafts.
Divide the parcels over the different ships to make it as cost efficient as possible.

## Structure of repository
Our repository consists of the following files and folders:
* main.py: this file will run the program based on the entered command-line arguments, by calling all other files
  and functions.
* Data: here you can find csv's containing our cargolists and features of the spaceships, as well as a script 
  for loading those csv's.
* Classes: this folder contains the data structure that is the foundation of our program. Two classes - namely 
  Parcels and Spaceships - are used, as well as a class including all useful features of a suggested distribution of
  parcels over the ships; the Inventory class.
* Algorithms: this is where our handwritten algorithms reside, currently those are a random algorithm, a combinatorial greedy/random
  algorithm, and a hill climber algorithm.
* Scripts: the algorithms are supported by a series of files in this folder: graph.py supports a concise 
  visualisation of the outcome of the algorithms, visual.html is used for a more elaborate visualisation, helpers.py 
  contains several smaller functions, generateships.py & shiploader.py are used to create a varying fleet of ships.
* Calculations: calculations of for example the upper and lower bound of our score function (costs) are stored here.
* Other: other files, like our to do list + division of tasks.


# Use of program
For data visualisation installing matplotlib is required (pip install matplotlib).
**Input**
Usage: main.py [-h] [-c] [-s] [-p] [a] [-hc] [-i]

Calculate the optimal organisation of a cargolist in spaceships

optional arguments:
  -h, --help            show this help message and exit
  -c, -cargo            choose a cargolist: 1, 2, 3 (int)
  -s, -ships            more than 4 ships: yes or no (string)
  -p, -politics         political constraints: yes or no (string)
  -a, -algorithms       which algorithm: greedy or random (string)
  -hc, -hillclimber     hillclimber: yes or no (string)
  -i, -iterations       how many iterations (int)

*Cargo* specifies which cargolist will be used to fill the ships. The *cargo* argument must be 1, 2 or 3. The default value for *cargo* is 1. 
*Ships* will determine whether a fixed amount of 4 ships will be used or whether an infinite amount of other ships can be purchased. The argument for *ships* is the string 'yes' or 'no'. The default value for *ships* is 'no'. 
*Politics* will specify if there are any political constraints to keep in consideration when running the code. This argument is only relevant when purchasing more ships than 4, so when argument *ships* is 'yes'. The *politics* argument takes the string 'yes' or 'no'. Default value for *politics* is 'no'. 
*Algorithms* will decide which algorithm is used to pack the ships as efficient as possible. The two options are a greedy algorithm and a random algorithm. *Algorithms* takes a string as argument: 'greedy' or 'random'. Default value for *algorithms* is greedy.
*Hillclimber* specifies whether the extra hillclimber algorithm will be used in addition to the algorithms specified by *algorithms*. It takes the string 'yes' or 'no' as argument. Default value for *hillclimber* is 'no'.
*Iterations* will determine how many times the algorithms are run. It takes an integer as argument, with a default value of 5.

**Output**
The output of the program will be mainly visualised in a Flask-based html server. The output will show the best solution provided. When the *ships* argument is 'no', progress bars will show how full all 4 ships are based on mass and volume. A table for all ships will be provided, showing which parcels are in the ships. A total result table will show how many parcels in total are packed and what the costs are for this solution. When *ships* argument is 'yes', only the two tables are provided. 

In addition to the web-based visualisation, a graph computed by matplotlib will show the distribution of the solutions in a histogram.

# Structure of main.py
- determine and check command-line arguments
- import csv's and create class (Parcel, Spaceship, Inventory) objects (-> csv's, dataloader.py & classes.py)
- call algorithm of choice (-> randomalgorithm.py/ greedyratio.py/ hillclimber.py)
- process outcome of algorithm and find best solution
- output information about best solution and visualisation
