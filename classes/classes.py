class Spaceship():
    """Spaceship object with properties from CSV file."""
    def __init__(self, ship_id, mass, max_weigth, max_volume, base_cost, ftw):
        self.ship_id = ship_id
        self.mass = mass
        self.max_weigth = max_weigth
        self.max_volume = max_volume
        self.base_cost = base_cost
        self.ftw = ftw

    def __str__(self):
<<<<<<< HEAD
        return "Spaceship name: {}.\nAgency: {}.\nMW: {}.\nMV: {}.\nBC: {}.\nF2W: {}.".format(self.name, self.agency, self.max_weigth, self.max_volume, self.base_cost, self.ftw)

with open("spacecrafts.csv") as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]
=======
        return "Spaceship id: {}.\nMW: {}.\nMV: {}.\nBC: {}.\nF2W: {}.".format(self.ship_id, self.max_weigth, self.max_volume, self.base_cost, self.ftw)

class Parcel():
    """Parcel object with properties from CSV file."""
    def __init__(self, id, weight, volume, ratio, location=0):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.ratio = ratio
        self.location = location
>>>>>>> 639b949248cf82ab2babdec89b64fee653effbd9

    def __str__(self):
        return "ID: {}.\nWeight: {}.\nVolume: {}.\nRatio: {}.\nLocation: {}.".format(self.id, self.weight, self.volume, self.ratio, self.location)

<<<<<<< HEAD
# class Parcel():
#     """Parcel object with properties from CSV file."""
#     def __init__(self, weight, volume, location=0, id):
#         self.weight = weight
#         self.volume = volume
#         self.ratio = ratio
#         self.location = location
#         self.id = id
#
class Inventory():
    """Inventory."""
    def __init__(self, arg):
        self.arg = arg
    def calculate_fuel_weight():
        fuel_weight = (self.mass + self.max_weight) * self.ftw / (1-self.ftw)
    def calculate_fuel_costs():
        fuel_cost = self.base_cost + roundup(fuel_weight * 100) * 5
        
=======
# class Inventory():
#     """Inventory."""
#     def __init__(self, arg):
#         self.arg = arg
#         self.name = dataSpace[0]["name"], dataSpace[1]["name"], dataSpace[2]["name"], dataSpace[3]["name"]
#     def calculate_fuel_weight():
#         fuel_weight = (self.mass + self.max_weight) * self.ftw / (1-self.ftw)
#     def calculate_fuel_costs():
#         fuel_cost = self.base_cost + roundup(fuel_weight * 100) * 5
>>>>>>> 639b949248cf82ab2babdec89b64fee653effbd9
