from datetime import datetime
from Infrastructure import utils

def test_add_package(travel_packages, travel_packages_history):
    package = {
        "start_date"    : datetime.strptime("1/1/2021", '%d/%m/%Y'),
        "end_date"      : datetime.strptime("2/2/2021", '%d/%m/%Y'),
        "destination"   : "Cluj",
        "price"         : 123
    }
    utils.add_to_history(travel_packages, travel_packages_history)
    utils.add_package(travel_packages, package)
    assert package in travel_packages
    package = {
        "start_date"    : datetime.strptime("10/3/2021", '%d/%m/%Y'),
        "end_date"      : datetime.strptime("15/3/2021", '%d/%m/%Y'),
        "destination"   : "Onesti",
        "price"         : 35
    }
    utils.add_to_history(travel_packages, travel_packages_history)
    utils.add_package(travel_packages, package)
    assert package in travel_packages
    package = {
        "start_date"    : datetime.strptime("5/4/2021", '%d/%m/%Y'),
        "end_date"      : datetime.strptime("21/5/2021", '%d/%m/%Y'),
        "destination"   : "Constanta",
        "price"         : 70
    }
    utils.add_to_history(travel_packages, travel_packages_history)
    utils.add_package(travel_packages, package)
    assert package in travel_packages

def test_modify_package(travel_packages, travel_packages_history):
    package = {
        "start_date"    : datetime.strptime("13/3/2021", '%d/%m/%Y'),
        "end_date"      : datetime.strptime("27/3/2021", '%d/%m/%Y'),
        "destination"   : "Bucuresti",
        "price"         : 105
    }
    utils.add_to_history(travel_packages, travel_packages_history)
    utils.modify_package(travel_packages, package, 2)
    assert travel_packages[1] == package

def test_delete(travel_packages, travel_packages_history):
    utils.add_to_history(travel_packages, travel_packages_history)
    utils.delete_package_by_destination(travel_packages, "Cluj")
    for i in range(len(travel_packages)):
        assert travel_packages[i]["destination"] != "Cluj"

def test_search(travel_packages, travel_packages_history):
    package = {
        "start_date"    : datetime.strptime("13/3/2021", '%d/%m/%Y'),
        "end_date"      : datetime.strptime("27/3/2021", '%d/%m/%Y'),
        "destination"   : "Bucuresti",
        "price"         : 105
    }
    assert utils.search_package_destination_price(travel_packages, "Bucuresti", 200) == [package]

def test_report(travel_packages, travel_packages_history):
    assert utils.report_average_price_destination(travel_packages, "Constanta") == 70

def test_filter(travel_packages, travel_packages_history):
    package = {
        "start_date"    : datetime.strptime("5/4/2021", '%d/%m/%Y'),
        "end_date"      : datetime.strptime("21/5/2021", '%d/%m/%Y'),
        "destination"   : "Constanta",
        "price"         : 70
    }
    utils.add_to_history(travel_packages, travel_packages_history)
    utils.filter_month(travel_packages, 3)
    assert travel_packages == [package]

def test_undo(travel_packages, travel_packages_history):
    new_packages = []
    new_packages.append(travel_packages_history[-1])
    travel_packages = utils.undo(travel_packages_history)
    assert travel_packages == new_packages[0]

def test():
    travel_packages = []
    travel_packages_history = []
    test_add_package(travel_packages, travel_packages_history)
    test_modify_package(travel_packages, travel_packages_history)
    test_delete(travel_packages, travel_packages_history)
    test_search(travel_packages, travel_packages_history)
    test_report(travel_packages, travel_packages_history)
    test_filter(travel_packages, travel_packages_history)
    test_undo(travel_packages, travel_packages_history)