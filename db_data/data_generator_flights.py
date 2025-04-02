
import random
import string
import time
from datetime import datetime, timedelta

def generate_departures(n,start = "20-04-2025 13:30:00", end= "20-11-2025 13:30:00"):
    # https://stackoverflow.com/questions/50165501/generate-random-list-of-timestamps-in-python
    """ 
    Generates  a list of departure times
        args:
        int n - number of generated records
        returns:
        list: list of generated departure times   
    """
    frmt = '%d-%m-%Y %H:%M:%S'
    times = []
    for i in range(n):
        stime = time.mktime(time.strptime(start, frmt))
        etime = time.mktime(time.strptime(end, frmt))
        ptime = stime + random.random() * (etime - stime)
        times.append(str(datetime.fromtimestamp(time.mktime(time.localtime(ptime)))))
    return times
def generate_arrivals(departures_list):
    #https://stackoverflow.com/questions/58626395/add-hours-or-minutesrandomly-generated-in-24-hour-format-time-python/58626465#58626465
    """ 
    Generates  a list of departure times
        args:
        list departutrs_list - list of generated departures
        returns:
        list: list of generated arrivals times   
    """
    frmt = '%Y-%m-%d %H:%M:%S'
    random_hour = random.uniform(1, 12)
    times = []
    for departure in departures_list:
        departure_time = datetime.strptime(departure, frmt )
        random_hour = random.uniform(1, 12)  
        arrival_time = departure_time + timedelta(hours=random_hour)
        times.append(arrival_time.strftime(frmt ))
    return times

def generate_flight_number(n):
    """ 
    Generates a list of flights numbers
        args:
        int n - number of generated records
        returns:
        list: list of generated flight numbers   
    """
    licences = []
    for i in range(n):    
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=6))
        licences.append(f"{letters}{numbers}")
    return licences

def generate_status(n):
    """ 
    Generates a list of flights status
        args:
        int n - number of generated records
        returns:
        list: list of generated statuses 
    """
    airlines = []
    for i in range(n):
        airlines.append(random.choice(["Scheduled",
                                        "Active",
                                        "Redirected",
                                        "Landed", 
                                        "Diverted",
                                        "Cancelled", 
                                        "Unknown"]))
    return airlines

def generate_airlines(n):
    #https://bolt.eu/en/blog/best-airlines-to-fly-with/
    """ 
    Generates a list of airline names
        args:
        int n - number of generated records
        returns:
        list: list of generated airline names
    """
    airlines = []
    for i in range(n):
        airlines.append(random.choice(["Qatar Airways",
                                        "Singapore Airways",
                                        "All Nippon Airways",
                                        "Emirates",
                                        "Japan Airlines",
                                        "Cathay Pacific Airways" ,
                                        "EVA Air",
                                        "Qantas Airways",
                                        "Air France",
                                        "Swiss International Air Lines"]))
    return airlines
def generate_airports(n):
    """ 
    Generates a list of airport codes
        args:
        int n - number of generated records
        returns:
        list: list of generated airport codes
    """
    airports = []
    for i in range(n):
       airports.append(random.choice(['DFW', 
                                        'DEN',
                                        'PEK',
                                        'PKX',
                                        'LHR',
                                        'HND', 
                                        'ORD', 
                                        'LAX', 
                                        'CDG', 
                                        'MAD']))
    return airports
def generate_pilots(n):
    """ 
    Generates a list of pilots
        args:
        int n - number of generated records
        returns:
        list: list of generated pilots
    """
    pilots = []
    for i in range(n):
       pilots.append(random.choice(['NT526887', 'DV970448',
                                     'JA056521', 'ZJ142471',
                                     'DU424209', 'TQ234233', 
                                     'DC505617', 'AP024941',
                                     'SQ314115','AR637412']))
    return pilots

dates = generate_departures(10)
arrivals = generate_arrivals(dates)
flight_numbs = generate_flight_number(10)
status = generate_status(10)
airlines = generate_airlines(10)
airports = generate_airports(10)
pilots = generate_pilots(10)

data = zip(flight_numbs,dates, arrivals, status,airlines, airports, pilots)
for i in data:
    print(i)