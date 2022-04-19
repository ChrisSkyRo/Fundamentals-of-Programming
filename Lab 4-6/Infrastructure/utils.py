from datetime import datetime

def add_to_history(travel_packages, travel_packages_history):
    copy = travel_packages[:]
    travel_packages_history.append(copy)
    return travel_packages_history

def add_package(travel_packages, package):
    travel_packages.append(package)
    return travel_packages

def can_modify_package(travel_packages, index):
    if index > len(travel_packages) or index < 1:
        return False
    return True

def modify_package(travel_packages, package, index):
    travel_packages[index-1] = package
    return travel_packages

def delete_package_by_destination(travel_packages, destination):
    i = 0
    while i < len(travel_packages):
        if travel_packages[i]["destination"] == destination:
            del(travel_packages[i])
            i -= 1 
        i += 1
    return travel_packages

def delete_package_below_days(travel_packages, days):
    i = 0
    while i < len(travel_packages):
        duration = travel_packages[i]["end_date"]-travel_packages[i]["start_date"]
        if duration.days < days:
            del(travel_packages[i])
            i -= 1 
        i += 1
    return travel_packages

def is_price_valid(price):
    try:
       float(price)
    except:
        return False
    return True

def delete_package_above_price(travel_packages, price):
    i = 0
    while i < len(travel_packages):
        if travel_packages[i]["price"] > price:
            del(travel_packages[i])
            i -= 1 
        i += 1
    return travel_packages

def is_date_valid(date):
    try:
        datetime.strptime(date, '%d/%m/%Y')
    except:
        return False
    return True

def search_package_in_interval(travel_packages, start_date, end_date):
    print_list = []
    for i in range(len(travel_packages)):
        if travel_packages[i]["start_date"] >= start_date and travel_packages[i]["end_date"] <= end_date:
            print_list.append(travel_packages[i])
    return print_list

def search_package_destination_price(travel_packages, destination, price):
    print_list = []
    for i in range(len(travel_packages)):
        if travel_packages[i]["destination"] == destination and travel_packages[i]["price"] < price:
            print_list.append(travel_packages[i])
    return print_list

def search_package_end_date(travel_packages, end_date):
    print_list = []
    for i in range(len(travel_packages)):
        if travel_packages[i]["end_date"] == end_date:
            print_list.append(travel_packages[i])
    return print_list

def report_destination(travel_packages, destination):
    print_list = []
    for i in range(len(travel_packages)):
        if travel_packages[i]["destination"] == destination:
            print_list.append(travel_packages[i])
    return print_list

def sort_packages(travel_packages):
    for i in range(1, len(travel_packages)):
        for j in range(i, 0, -1):
            if travel_packages[j]["price"] < travel_packages[j-1]["price"]:
                travel_packages[j], travel_packages[j-1] = travel_packages[j-1], travel_packages[j]
    return sort_packages

def report_average_price_destination(travel_packages, destination):
    sum = 0.0
    terms = 0
    for i in range(len(travel_packages)):
        if travel_packages[i]["destination"] == destination:
            sum += travel_packages[i]["price"]
            terms += 1
    return float(sum/terms)

def filter_destination_price(travel_packages, destination, price):
    delete_package_above_price(travel_packages, price)
    i = 0
    while i < len(travel_packages):
        if travel_packages[i]["destination"] != destination:
            del(travel_packages[i])
            i -= 1
        i += 1
    return travel_packages

def filter_month(travel_packages, month):
    i = 0
    while i < len(travel_packages):
        if (travel_packages[i]["start_date"].month <= month and travel_packages[i]["end_date"].month >= month) or (travel_packages[i]["start_date"].month < month and travel_packages[i]["end_date"].month + travel_packages[i]["end_date"].year-travel_packages[i]["start_date"].year*12 > month):
            del(travel_packages[i])
            i -= 1
        i += 1
    return travel_packages

def undo(travel_packages_history):
    return travel_packages_history.pop(-1)