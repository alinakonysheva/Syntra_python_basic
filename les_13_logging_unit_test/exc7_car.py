import json
from car_v3 import create_car


def main():
    car = create_car(1, '308sw', 2, 0.00)
    print("mijn wagen: ".format(car))
    print(json.dumps(car.to_json()))

    



if __name__ == '__main__':
    main()