# dummy function for car body identification
import random

def car_identification():
    car_body_types = ["sedan", "SUV", "coupe", "hatchback", "convertible", "pickup"]
    body_type = random.choice(car_body_types)
    return body_type