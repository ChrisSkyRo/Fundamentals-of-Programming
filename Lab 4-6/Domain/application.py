from datetime import datetime
from UserInterface import inputs
from UserInterface import outputs
from Infrastructure import utils
from Infrastructure import testing

def start():
    testing.test()
    travel_packages = []
    travel_packages_history = []
    outputs.print_start()
    while True:
        command = input().split()
        if len(command) == 0:
            outputs.invalid_input()
        else:
            if command[0] == "help":
                outputs.print_help()
            elif command[0] == "add":
                package = inputs.read_travel_package()
                utils.add_to_history(travel_packages, travel_packages_history)
                utils.add_package(travel_packages, package)
                outputs.print_packages(travel_packages)
            elif command[0] == "modify":
                if len(command) > 1 and command[1].isnumeric():
                    index = int(command[1])
                    if utils.can_modify_package(travel_packages, index):
                        package = inputs.read_travel_package()
                        utils.add_to_history(travel_packages, travel_packages_history)
                        utils.modify_package(travel_packages, package, index)
                        outputs.print_packages(travel_packages)
                    else:
                        outputs.index_out_of_range()
                else:
                    outputs.invalid_input()
            elif command[0] == "delete":
                if len(command) > 2:
                    if command[1] == "destination":
                        utils.add_to_history(travel_packages, travel_packages_history)
                        utils.delete_package_by_destination(travel_packages, command[2])
                    elif command[1] == "duration" and command[2].isnumeric():
                        utils.add_to_history(travel_packages, travel_packages_history)
                        utils.delete_package_below_days(travel_packages, int(command[2]))
                    elif command[1] == "price" and utils.is_price_valid(command[2]):
                        utils.add_to_history(travel_packages, travel_packages_history)
                        utils.delete_package_above_price(travel_packages, float(price))
                    else:
                        outputs.invalid_input()
                else:
                    outputs.invalid_input()
            elif command[0] == "search":
                if len(command) > 2:
                    if command[1] == "interval" and len(command) > 3 and utils.is_date_valid(command[2]) and utils.is_date_valid(command[3]):
                        outputs.print_packages(utils.search_package_in_interval(travel_packages, datetime.strptime(command[2], '%d/%m/%Y'), datetime.strptime(command[3], '%d/%m/%Y')))
                    elif command[1] == "destination" and len(command) > 3 and utils.is_price_valid(command[3]):
                        outputs.print_packages(utils.search_package_destination_price(travel_packages, command[2], command[3]))
                    elif command[1] == "end" and len(command) > 2 and utils.is_date_valid(command[2]):
                        outputs.print_packages(utils.search_package_end_date(travel_packages, command[2]))
                    else:
                        outputs.invalid_input()
                else:
                    outputs.invalid_input()
            elif command[0] == "report":
                if len(command) > 1:
                    if command[1] == "destination" and len(command) > 2:
                        outputs.print_packages(utils.report_destination(travel_packages, command[2]))
                    elif command[1] == "interval" and len(command) > 3 and utils.is_date_valid(command[2]) and utils.is_date_valid(command[3]):
                        unsorted_packages = utils.search_package_destination_price(travel_packages, command[2], command[3])
                        outputs.print_packages(utils.sort_packages(unsorted_packages))
                    elif command[1] == "average" and len(command) > 2:
                        outputs.print_packages(utils.report_average_price_destination(travel_packages, command[2]))
                    else:
                        outputs.invalid_input()
                else:
                    outputs.invalid_input()
            elif command[0] == "filter":
                if len(command) > 2:
                    if command[1] == "destination" and len(command) > 3 and utils.is_price_valid(command[3]):
                        utils.add_to_history(travel_packages, travel_packages_history)
                        utils.filter_destination_price(travel_packages, command[2], command[3])
                    elif command[1] == "month" and command[2].isnumeric() and int(command[2]) > 0 and int(command[2]) < 13:
                        utils.add_to_history(travel_packages, travel_packages_history)
                        utils.filter_month(travel_packages, command[2])
                    else:
                       outputs.invalid_input()
                else:
                    outputs.invalid_input()
            elif command[0] == "undo":
                if len(travel_packages_history) > 0:
                    travel_packages = utils.undo(travel_packages_history)
                    outputs.print_packages(travel_packages)
                else:
                    outputs.print_cant_undo()
            elif command[0] == "exit":
                return
            else:
                outputs.invalid_input()
