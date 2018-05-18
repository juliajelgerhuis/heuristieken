import random
from algorithms import helpers
import time

# create random solutions
def random_algorithm(inventory):
    """Randomly fills spaceships with a cargo list.
    The first argument holds a list of spaceship objects,
    the second argument holds a list of parcel objects.

    Usage:
    randomalgorithm.random_algorithm(loaded_data[0], loaded_data[1])
    randomalgorithm.random_algorithm(inventory)
    """

    # zorgen dat random elke keer met de lege inventory begint
    dict_parcel = inventory.dict_parcel
    dict_space = inventory.dict_space
    ship_counter = 1
    parcel_amount = 0
    parcel_weight_max = inventory.maxParcelWeightVolume()[0]
    parcel_volume_max = inventory.maxParcelWeightVolume()[1]

    # make shuffled list
    shuffled_list = random.sample(range(100), k=100)

    # start weight and volume at zero and set to not full
    dict_space = [helpers.reset(element) for element in dict_space]

    # set location of parcels to zero
    dict_parcel = [helpers.resetParcel(element) for element in dict_parcel]

    # add parcel until limits are reached (until all ships are full)
    while (dict_space[0].full is False or dict_space[1].full is False or dict_space[2].full is False or dict_space[3].full is False):

        # only continue with ships that are not full
        while dict_space[ship_counter - 1].full is True:
            if ship_counter is 4:
                ship_counter = 1
            else:
                ship_counter += 1


        # pick random parcel
        add_ID = shuffled_list.pop()
        # print("parcel number: ", end="")
        # print(add_ID)

        # add parcel to ship
        # checken: ID -1 op alle plekken kloppend?
        dict_parcel[add_ID - 1].location = ship_counter

        # update spaceships current weight and volume
        dict_space[ship_counter - 1].current_weight += dict_parcel[add_ID - 1].weight
        dict_space[ship_counter - 1].current_volume += dict_parcel[add_ID - 1].volume

        # count parcels per solution
        parcel_amount += 1

        # note when ship is almost full
        if (dict_space[ship_counter - 1].current_weight >= dict_space[ship_counter - 1].max_weight - parcel_weight_max or
                    dict_space[ship_counter - 1].current_volume >= dict_space[ship_counter - 1].max_volume - parcel_volume_max):

            for parcel_id in shuffled_list:

                if (dict_space[ship_counter - 1].current_weight + dict_parcel[parcel_id - 1].weight <= dict_space[ship_counter - 1].max_weight and \
                    dict_space[ship_counter - 1].current_volume + dict_parcel[parcel_id - 1].volume <= dict_space[ship_counter - 1].max_volume):

                    dict_space[ship_counter - 1].current_weight += dict_parcel[parcel_id - 1].weight
                    dict_space[ship_counter - 1].current_volume += dict_parcel[parcel_id - 1].volume

                    shuffled_list.remove(parcel_id)

                    dict_parcel[parcel_id - 1].location = ship_counter

                    parcel_amount += 1

                else:
                    continue

            dict_space[ship_counter - 1].full = True

        # time.sleep(1)
        # yield dict_space[ship_counter].current_weight

    print(helpers.visualizeParcelsPerShip(inventory))

    # return inventory ipv hieronder

    return {"parcel_amount": parcel_amount, "weight1": dict_space[0].current_weight, \
                "weight2": dict_space[1].current_weight, "weight3": dict_space[2].current_weight, \
                    "weight4": dict_space[3].current_weight}
