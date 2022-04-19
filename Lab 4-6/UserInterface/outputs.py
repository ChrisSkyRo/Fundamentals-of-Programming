def print_start():
    print("Welcome to FP Tourism Agency. Type \"help\" for a list of commands.")

def print_help():
    print("help - shows the list of commands")
    print("add - adds a new travel package")
    print("modify <index> - modifies an existent travel package")
    print("delete destination <name> - deletes all travel packages for a given destination")
    print("delete duration <days> - deletes all travel packages for with a shorter duration than <days>")
    print("delete price <price> - deletes all travel packages for with a higher price than <price>")
    print("search interval <start_date> <end_date> - shows all the packages in the specified interval of time")
    print("search destination <destination> <price> - shows all the packages with the given and the price less than <price>")
    print("search end <end_date> - shows all the packages with the end date equal to <end_date>")
    print("report destination <destination> - shows the packages with the given destination")
    print("report interval <start_date> <end_date> - shows all the packages in the specified interval of time ordered ascending by price")
    print("report average <destination> - shows the average price for a given destination")
    print("filter destination <destination> <price> - deletes the packages with a destination different from <destionation> and a price greater than <price>")
    print("filter month <month> - deletes the packages that include the given month (as a integer number 1-12)")
    print("undo - undoes the last operation that modified the list of packages")
    print("exit - closes the app")

def invalid_input():
    print("Invalid command. Please enter \"help\" for a list of commands.")

def invalid_price():
    print("Invalid price. Enter a float or \"help\" for a list of commands.")

def index_out_of_range():
    print("Index is out of range.")

def print_travel_package(travel_packages, index):
    print(index+1, "\t", travel_packages[index]["destination"], "\t", travel_packages[index]["price"], "\t", travel_packages[index]["start_date"], "\t", travel_packages[index]["end_date"])

def print_packages(travel_packages):
    print("no.\tDestination\tPrice\tStart date\tEnd date")
    for i in range(len(travel_packages)):
        print_travel_package(travel_packages, i)

def print_cant_undo():
    print("We can't perform undo anymore.")