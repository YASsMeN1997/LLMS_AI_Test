from src.car_description import parse_car_description

def main():
    # Example description input
    description = "Blue Ford Fusion produced in 2015 featuring a 2.0-liter engine. The vehicle has low mileage with only 40,000 miles on the odometer."

    # Get the car details in JSON format
    car_details = parse_car_description(description)

    # Print the output JSON
    print(car_details)

if __name__ == "_main_":
    main()




