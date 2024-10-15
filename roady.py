# benzina sau motorina
# oras plecare oras sosire
# nr de persoane
# consum
import json

from distance import Distance
from gas_price import Gas


class Roady:

    def __init__(self, departure_city: str, destination_city: str,
                 number_of_persons: int, fuel_usage: float,
                 fuel: str = "benzina", path: str = "config.json"):

        with open(path, "r") as f:
            config = json.loads(f.read())

        self.distance = Distance(departure_city, destination_city, config)
        self.gas = Gas(config, fuel)
        self.number_of_persons = number_of_persons
        self.fuel_usage = fuel_usage


    def calculate_price_per_person(self):

        km = int(self.distance.km.split(" ")[0])
        total_liters = km * self.fuel_usage / 100
        total_price = total_liters * self.gas.avg_price
        return total_price / self.number_of_persons


if __name__ == '__main__':
    roady1 = Roady("Bucuresti", "Iasi", 3, 10.0)
    print(roady1.calculate_price_per_person())