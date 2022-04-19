from datetime import datetime

def read_travel_package():
    package = {
        "start_date"    : datetime.strptime(input("Start date (day/month/year) = "), '%d/%m/%Y'),
        "end_date"      : datetime.strptime(input("End date (day/month/year) = "), '%d/%m/%Y'),
        "destination"   : input("Destination = "),
        "price"         : int(input("Price = "))
    }
    return package
