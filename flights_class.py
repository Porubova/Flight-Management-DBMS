import sqlite3
import pandas as pd
from tabulate import tabulate
from datetime import datetime, timedelta
import random
from utils.utils import *


class Flights:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.destination = None
        self.status = None

    def add_new_flight(self):
        frmt = '%Y-%m-%d %H:%M:%S'
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Adding new flight")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")

        # User input for flight number
        flight_number = str.upper(input(f"{COLOR_YELLOW}Please provide flight number (AB123456): "))

        while not is_valid_format(flight_number):
            print(f"{COLOR_RED}Invalid flight number format, try agin.")
            flight_number = str.upper(input(f"{COLOR_YELLOW}Please provide flight number (AB123456): "))

        # User input for departure time
        departure_time = input(f"{COLOR_YELLOW}Please provide Departure Time (YYYY-MM-DD HH:MM:SS): ").strip()

        while not is_valid_datetime(departure_time):
            print(f"{COLOR_RED}Invalid date format, try agin.")
            departure_time = input(f"{COLOR_YELLOW}Enter new departure time (YYYY-MM-DD HH:MM:SS): ").strip()
        departure_time = datetime.strptime(departure_time, frmt)
        departure_time_str = departure_time.strftime(frmt)

        # User input for time in the air. Arrival time computed as addition to the departure time
        air_time = float(input(f"{COLOR_YELLOW}Please provide Flight Time in hours: ").strip())
        arrival_time = departure_time + timedelta(hours=air_time)
        arrival_time_str = arrival_time.strftime(frmt)
        print(departure_time_str, arrival_time)

        # User input for status from the list of accepted statuses
        status = input(f"{COLOR_YELLOW}Enter new flight status from ['Scheduled', 'Active',"
                           " 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']: ").strip().capitalize()

        while status not in ['Scheduled', 'Active', 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']:
            print(f"{COLOR_RED}Invalid status, try again.")
            status = input(f"{COLOR_YELLOW}Enter new flight status from ['Scheduled', 'Active',"
                               " 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']: ").strip().capitalize()

        # User input for airline code as a selection from available in the DB airlines
        available_airlines = [i[0] for i in self.cursor.execute("""SELECT airline_code
                                                                         FROM airlines""").fetchall()]
        airline_code = str.upper(
            input(f"{COLOR_YELLOW}Please provide Airline Code from list {str(available_airlines)}:")).strip()
        while airline_code not in available_airlines:
            print(f"{COLOR_RED}Invalid airline code, try agin.")
            airline_code = str.upper(
                input(
                    f"{COLOR_YELLOW}Please provide Airline Code from list {str(available_airlines)}:")).strip()

        # User input for origin airport code as a selection from available in the DB airlines
        available_airports = [i[0] for i in self.cursor.execute("""SELECT airport_code
                                                                 FROM destinations""").fetchall()]
        origin_airport_code = str.upper(
            input(f"{COLOR_YELLOW}Please provide Originated Airport Code from list {str(available_airports)}:")).strip()
        while origin_airport_code not in available_airports:
            print(f"{COLOR_RED}Invalid airport code, try agin.")
            origin_airport_code = str.upper(
                input(
                    f"{COLOR_YELLOW}Please provide Originated Airport Code from list {str(available_airports)}:")).strip()

        # User input for destination airport code as a selection from available in the DB airlines
        # minus originated airport code.
        available_airports = [i for i in available_airports if i != origin_airport_code]
        destination_airport_code = str.upper(
                input(
                    f"{COLOR_YELLOW}Please provide Originated Airport Code from list {str(available_airports)}:")).strip()
        while destination_airport_code  not in available_airports:
            print(f"{COLOR_RED}Invalid airport code, try agin.")
            destination_airport_code = str.upper(
                input(
                    f"{COLOR_YELLOW}Please provide Originated Airport Code from list {str(available_airports)}:")).strip()

        # Pilot selected randomly from all available pilots
        available_pilots = [i[0] for i in self.cursor.execute("""SELECT pilot_id
                                                                 FROM pilots""").fetchall()]
        pilot_id = random.choice(available_pilots)

        # Add new flight to the flights table
        query = """INSERT INTO flights
                                     (flight_number, departure_time, arrival_time, flight_status,
                                      airline_code, origin_airport_code, destination_airport_code, pilot_id)
                                      VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (flight_number, departure_time_str, arrival_time_str, status,
                                      airline_code, origin_airport_code, destination_airport_code, pilot_id,)).fetchall()
        self.conn.commit()

        # Display all flights
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Adding new flight")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_YELLOW}New Flight has been added.")
        print()
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE FLIGHTS")
        print(f"{COLOR_END}", tabulate(self.get_flights_all().set_index("flight_id"), headers='keys', tablefmt='pretty'))

    def view_flights(self):
        """
        Filter flights based on different attributes
        """
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing flights information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_LIGHT_BLUE}       All FLIGHTS")
        print(f"{COLOR_END}", tabulate(self.get_flights_all().set_index("flight_id"), headers='keys', tablefmt='pretty'))
        print(f"{COLOR_YELLOW}Which field do you want to filter available flights on?{COLOR_END}")
        print(f"{COLOR_PURPLE}1.{COLOR_END}Airline")
        print(f"{COLOR_PURPLE}2.{COLOR_END}Flight Status")
        print(f"{COLOR_PURPLE}3.{COLOR_END}Destination City")
        print(f"{COLOR_PURPLE}4.{COLOR_END}Airline and Flight Status")
        choice = int(input(f"{COLOR_YELLOW}Enter 1, 2, 3 or 4: ").strip())

        while choice not in [1, 2, 3, 4]:
            print(f"{COLOR_RED}Invalid choice.")
            choice = int(input(f"{COLOR_YELLOW}Enter 1, 2, 3 or 4: ").strip())
        if choice == 1:
            self.get_flights_airline()
        if choice == 2:
            self.get_flights_status()
        if choice == 3:
            self.get_flights_destinations()
        if choice == 4:
            self.get_flights_airline_status()

    def get_flights_all(self):
        # retrieves all flights data
        query = """SELECT * 
                   FROM flights"""
        df = pd.DataFrame(self.cursor.execute(query).fetchall())
        df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(flights)").fetchall()]
        return df

    def get_pilots_all(self):
        # retrieves all pilots data
        query = """SELECT * 
                   FROM pilots"""
        df = pd.DataFrame(self.cursor.execute(query).fetchall())
        df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(pilots)").fetchall()]
        return df

    def get_flights_airline(self):
        # retrieves all flights for specific airline
        available_airlines = self.get_airline_names()
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE AIRLINES{COLOR_END}")
        print(tabulate(available_airlines, headers='keys', tablefmt='pretty'))
        airline_code = str.upper(input(f"{COLOR_YELLOW}Please enter the valid airline code: ").strip())

        while airline_code not in [i for i in available_airlines.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            airline_code = str.upper(input(f"{COLOR_YELLOW}Please enter the valid airline code: ").strip())

        query = f"""SELECT flight_number, departure_time, arrival_time, flight_status, origin_airport_code,
                    destination_airport_code
                    FROM flights 
                    WHERE airline_code = ?"""
        df = pd.DataFrame(self.cursor.execute(query, (airline_code,)).fetchall())
        airline_name = self.cursor.execute(f"SELECT airline_name FROM airlines WHERE airline_code = ?",
                             (airline_code,)).fetchall()[0][0]
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing flights information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()

        print(f"{COLOR_END}Displaying flights for {COLOR_CYAN}{airline_name}")
        print(f"{COLOR_END}")
        df.columns = ['flight_number', 'departure_time', 'arrival_time', 'flight_status', 'origin_airport_code',
                      'destination_airport_code']
        print(tabulate(df.set_index('flight_number'), headers='keys', tablefmt='pretty'))
        return df.set_index('flight_number')

    def get_flights_status(self):
        # retrieves all flights for specific status
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE STATUSES{COLOR_END}")
        available_statuses = pd.DataFrame([s[0] for s in self.cursor.execute(
            """SELECT DISTINCT flight_status  FROM flights """).fetchall()]).reset_index()
        available_statuses.columns = ["status_code", "status"]
        print(tabulate(available_statuses.set_index("status_code"), headers='keys', tablefmt='pretty'))
        status_code = input(f"{COLOR_YELLOW}Please enter the valid status: ")

        while str(status_code) not in [str(i) for i in available_statuses.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            status_code = input(f"{COLOR_YELLOW}Please enter the valid status: ")
        flight_status_code = available_statuses.loc[available_statuses.index == int(status_code)].status.values[0]

        query = f"""SELECT flight_number, departure_time, arrival_time, flight_status, origin_airport_code,
                    destination_airport_code  
                    FROM flights 
                    WHERE flight_status = ?"""

        df = pd.DataFrame(self.cursor.execute(query, (flight_status_code,)).fetchall())
        print(df)
        df.columns = ['flight_number', 'departure_time', 'arrival_time', 'flight_status', 'origin_airport_code',
                      'destination_airport_code']
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing flights information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"Displaying {COLOR_CYAN}{COLOR_BOLD}{flight_status_code} {COLOR_END}flights")
        print()

        print(tabulate(df.set_index('flight_number'), headers='keys', tablefmt='pretty'))
        return df.set_index('flight_number')

    def get_flights_airline_status(self):
        # retrieves all flights for specific airline and flight status
        available_airlines = self.get_airline_names()
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE AIRLINES{COLOR_END}")
        print(tabulate(available_airlines, headers='keys', tablefmt='pretty'))
        airline_code = str.upper(input(f"{COLOR_YELLOW}Please enter the valid airline code: ").strip())

        while airline_code not in [i for i in available_airlines.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            airline_code = str.upper(input(f"{COLOR_YELLOW}Please enter the valid airline code: ").strip())

        airline_name = self.cursor.execute(f"SELECT airline_name FROM airlines WHERE airline_code = ?",
                                           (airline_code,)).fetchall()[0][0]
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE STATUSES{COLOR_END}")
        available_statuses = (pd.DataFrame([s[0] for s in self.cursor.execute(
            """SELECT DISTINCT flight_status  FROM flights WHERE airline_code = ?""", (airline_code,))
                                           .fetchall()]).reset_index())
        available_statuses.columns = ["status_code", "status"]
        print(tabulate(available_statuses.set_index("status_code"), headers='keys', tablefmt='pretty'))
        status_code = input(f"{COLOR_YELLOW}Please enter the valid status: ")

        while str(status_code) not in [str(i) for i in available_statuses.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            status_code = input(f"{COLOR_YELLOW}Please enter the valid status: ")
        flight_status_code = available_statuses.loc[available_statuses.index == int(status_code)].status.values[0]

        query = f"""SELECT flight_number, departure_time, arrival_time, flight_status, origin_airport_code,
                            destination_airport_code
                            FROM flights 
                            WHERE airline_code = ?
                            AND flight_status = ?"""
        df = pd.DataFrame(self.cursor.execute(query, (airline_code, flight_status_code, )).fetchall())

        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing flight information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_END}Displaying flights for {COLOR_CYAN}{airline_name}{COLOR_END} and {COLOR_CYAN}{flight_status_code}{COLOR_END}")
        print(f"{COLOR_END}")
        df.columns = ['flight_number', 'departure_time', 'arrival_time', 'flight_status', 'origin_airport_code',
                      'destination_airport_code']
        print(tabulate(df.set_index('flight_number'), headers='keys', tablefmt='pretty'))
        return df.set_index('flight_number')

    def get_flights_destinations(self):
        # retrieves all flights for specific airline
        available_destinations_df = self.get_destination_names()
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE AIRLINES{COLOR_END}")
        print(tabulate(available_destinations_df[["city_code", "city_name"]].set_index("city_code"), headers='keys', tablefmt='pretty'))
        city_code = str.upper(input(f"{COLOR_YELLOW}Please enter the valid destination city code: ").strip())
        while city_code not in [i for i in available_destinations_df.city_code.values]:
            print(f"{COLOR_RED}Invalid choice.")
            city_code = str.upper(input(f"{COLOR_YELLOW}Please enter the valid destination city code: ").strip())
        destination_code = (available_destinations_df.loc[available_destinations_df.city_code==city_code]
                            .destination_airport_code.values[0])
        query = f"""SELECT flight_number, departure_time, arrival_time, flight_status, origin_airport_code,
                    destination_airport_code  
                    FROM flights WHERE destination_airport_code = ?"""
        df = pd.DataFrame(self.cursor.execute(query, (destination_code,)).fetchall())
        destination_name = (available_destinations_df
                            .loc[available_destinations_df.city_code ==city_code]["city_name"].values[0])
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing flight information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_END}Displaying flights for {COLOR_CYAN}{destination_name}")
        print(f"{COLOR_END}")
        df.columns = ['flight_number', 'departure_time', 'arrival_time', 'flight_status', 'origin_airport_code',
                        'destination_airport_code']
        print(tabulate(df.set_index('flight_number'), headers='keys', tablefmt='pretty'))
        return df.set_index('flight_number')

    def get_airline_names(self):
        query = """SELECT DISTINCT airlines.airline_code, airlines.airline_name from airlines
                 JOIN flights ON airlines.airline_code = flights.airline_code"""
        table = self.cursor.execute(query).fetchall()
        df = pd.DataFrame(table)
        df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(airlines)").fetchall()]
        return df.set_index('airline_code')

    def get_destination_names(self):
        query = """SELECT cities.city_code, cities.city_name, ap.destination_airport_code  FROM (SELECT DISTINCT destinations.airport_code,
         destinations.city_code, flights.destination_airport_code  FROM destinations
                 JOIN flights ON flights.destination_airport_code  = destinations.airport_code) ap JOIN cities ON cities.city_code = ap.city_code"""
        table = self.cursor.execute(query).fetchall()
        df = pd.DataFrame(table)
        df.columns = ["city_code", "city_name", "destination_airport_code"]
        return df

    def get_pilots_names(self):
        query = """SELECT pilots.pilot_id, pilots.pilot_name from pilots"""
        table = self.cursor.execute(query).fetchall()
        df = pd.DataFrame(table)
        df.columns = ["pilot_id", "pilot_name"]
        return df.set_index("pilot_id")

    def get_pilots_schedules_count(self):
        """
        Extracting count of flight for each pilot
        """
        query = """SELECT pilots.pilot_name, pl.pilot_id, pl.flight_count 
                   FROM (
                         SELECT flights.pilot_id ,COUNT (flights.flight_id) AS flight_count 
                         FROM flights GROUP BY flights.pilot_id
                         ORDER BY flight_count DESC) pl 
                   JOIN pilots 
                        ON pilots.pilot_id = pl.pilot_id"""
        table = self.cursor.execute(query).fetchall()
        df = pd.DataFrame(table)
        df.columns = ["pilot_name", "pilot_id", "flight_count"]
        return df

    def get_destinations_count(self):
        """
        Extracting count of flight to each destination
        """
        query = """SELECT destinations.airport_name, destinations.airport_code, pl.flight_count
                   FROM (
                        SELECT flights.destination_airport_code,COUNT (flights.flight_id) AS flight_count 
                        FROM flights 
                        GROUP BY flights.destination_airport_code
                        ORDER BY flight_count DESC) pl 
                    JOIN destinations 
                         ON destinations.airport_code  = pl.destination_airport_code """
        table = self.cursor.execute(query).fetchall()
        df = pd.DataFrame(table)
        df.columns = ["airport_name", "airport_code", "flight_count"]
        return df

    def get_pilots_schedules(self):
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing pilots information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        active_pilots_df = self.get_pilots_schedules_count()[["pilot_id", "pilot_name"]].set_index("pilot_id")
        print(f"{COLOR_LIGHT_BLUE}       ACTIVE PILOTS{COLOR_END}")
        print(tabulate(active_pilots_df, headers='keys', tablefmt='pretty'))
        pilot_id = str.upper(input(f"{COLOR_YELLOW}Please enter the valid pilot id: ").strip())

        while pilot_id not in [i for i in active_pilots_df.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            pilot_id = str.upper(input(f"{COLOR_YELLOW}Please enter the valid pilot id: ").strip())

        pilot_data_df = (pd.DataFrame(self.cursor.execute("""SELECT * FROM pilots WHERE pilot_id =?""", (pilot_id, ))
                                      .fetchall()))

        pilot_data_df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(pilots)").fetchall()]
        pilot_name = pilot_data_df.pilot_name.values[0]
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing pilots information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_END}Displaying information for {COLOR_CYAN}{pilot_name}")
        print(f"{COLOR_END}")
        print(tabulate(pilot_data_df.set_index('pilot_id'), headers='keys', tablefmt='pretty'))
        input(f"{COLOR_YELLOW}Please press any key to see flights for {pilot_name}...")
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Viewing pilots information")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        query = """SELECT * 
                  FROM flights
                  WHERE pilot_id = ?
                  """
        table = self.cursor.execute(query, (pilot_id, )).fetchall()
        df = pd.DataFrame(table)
        df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(flights)").fetchall()]
        print(f"{COLOR_END}Displaying flights for {COLOR_CYAN}{pilot_name}")
        print(f"{COLOR_END}")
        print(tabulate(df.set_index('pilot_id'), headers='keys', tablefmt='pretty'))
        return df

    def assign_pilot_flight(self):
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Assigning pilot to the flight")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        pilots = self.get_pilots_names()
        print(f"{COLOR_END}Available pilots")
        print(f"{COLOR_END}")
        print(tabulate(pilots, headers='keys', tablefmt='pretty'))
        pilot_id = str.upper(input(f"{COLOR_YELLOW}"
                                   f"Please enter the valid pilot id you want to assign to a flight: ").strip())

        while pilot_id not in [i for i in pilots.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            pilot_id = str.upper(input(f"{COLOR_YELLOW}"
                                       f"Please enter the valid pilot id you want to assign to a flight: ").strip())

        pilot_name = pilots.loc[pilots.index == pilot_id].pilot_name.values[0]

        flights = self.get_flights_all().set_index('flight_id')
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Assigning pilot to the flight")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_END}Available flights")
        print(f"{COLOR_END}")
        print(tabulate(flights, headers='keys', tablefmt='pretty'))
        print()
        flight_id = input(f"{COLOR_YELLOW}"
                                    f"Please enter the valid flight id you want to assign {pilot_name} to: ").strip()

        while flight_id not in [str(i) for i in flights.index.values]:
            print(f"{COLOR_RED}Invalid choice.")
            flight_id = input(f"{COLOR_YELLOW}Please enter the valid pilot id: ").strip()
        query = """UPDATE flights 
                   SET pilot_id = ? 
                   WHERE flight_id = ?"""
        self.cursor.execute(query, (pilot_id, int(flight_id)))
        self.conn.commit()
        flights = self.get_flights_all().set_index('flight_id')
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Assigning pilot to the flight")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        updated_flight = flights.loc[flights.index == int(flight_id)]
        pilot_flights = flights.loc[flights.pilot_id == pilot_id].reset_index().set_index("pilot_id")
        print(f"{COLOR_END}Pilot {COLOR_CYAN}{pilot_name}{COLOR_END} "
              f"has been assigned to flight number {COLOR_CYAN}{flight_id}{COLOR_END}")
        print()
        print(f"{COLOR_BLUE}Updated flight")
        print(f"{COLOR_END}")
        print(tabulate(updated_flight, headers='keys', tablefmt='pretty'))
        print()
        input(f"{COLOR_YELLOW}Please press any key to see flights for {pilot_name}...")
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Assigning pilot to the flight")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_BLUE}Flights for {pilot_name}")
        print(f"{COLOR_END}")
        print(tabulate(pilot_flights, headers='keys', tablefmt='pretty'))

    def get_stats(self):
        """
        Displaying basic stats for flights and pilots
        """
        all_flights = self.get_flights_all().set_index('flight_id')
        all_pilots = self.get_pilots_all().set_index('pilot_id')
        pilots_schedules = self.get_pilots_schedules_count().set_index('pilot_name')
        destinations_schedules = self.get_destinations_count().set_index("airport_name")
        clear_screen()
        print(f"{COLOR_CYAN}Displaying all flights:{COLOR_END}")
        print()
        print(tabulate(all_flights, headers='keys', tablefmt='pretty'))
        input(f"{COLOR_YELLOW}Press any key to continue...")
        clear_screen()
        print(f"{COLOR_CYAN}Displaying all pilots:{COLOR_END}")
        print()
        print(tabulate(all_pilots, headers='keys', tablefmt='pretty'))
        input(f"{COLOR_YELLOW}Press any key to continue...")
        clear_screen()
        print(f"{COLOR_CYAN}Displaying number of flights assigned to the pilots:{COLOR_END}")
        print()
        print(tabulate(pilots_schedules, headers='keys', tablefmt='pretty'))
        input(f"{COLOR_YELLOW}Press any key to continue...")
        clear_screen()
        print(f"{COLOR_CYAN}Displaying number of flights to the destinations:{COLOR_END}")
        print()
        print(tabulate(destinations_schedules, headers='keys', tablefmt='pretty'))

    def update_flight_info(self):
        """
        Updates departure time or status of a specific flight
        """
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Updating flight info")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        frmt = '%Y-%m-%d %H:%M:%S'
        available_flights_df = pd.DataFrame(self.cursor.execute("""SELECT flight_id, flight_number
                                                                   FROM flights""").fetchall())
        available_flights_df.columns = ["flight_id", "flight_number"]
        print(f"{COLOR_LIGHT_BLUE}       AVAILABLE FLIGHTS")
        print(f"{COLOR_END}", tabulate(available_flights_df.set_index("flight_id"), headers='keys', tablefmt='pretty'))
        flight_id = input(f"{COLOR_YELLOW}Please enter the valid fight id you want to modify:").strip()

        while flight_id not in [str(i) for i in available_flights_df['flight_id'].values]:
            print(f"{COLOR_RED}Flight cannot be retrieved!")
            flight_id = input(f"{COLOR_YELLOW}Please enter the valid fight id you want to modify:").strip()

        flight_info_df = pd.DataFrame(self.cursor.execute("""SELECT * 
                                                             FROM flights 
                                                             WHERE flight_id = ?""", (flight_id,)).fetchall())
        flight_info_df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(flights)").fetchall()]
        clear_screen()
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print(f"{COLOR_LIGHT_BLUE}       Updating flight info")
        print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
        print()
        print(f"{COLOR_LIGHT_BLUE}       RETRIEVED FLIGHT")
        print(f"{COLOR_END}", tabulate(flight_info_df.set_index('flight_id'), headers='keys', tablefmt='pretty'))
        print(f"{COLOR_YELLOW}Which field do you want to update?{COLOR_END}")
        print(f"{COLOR_PURPLE}1.{COLOR_END}Departure Time")
        print(f"{COLOR_PURPLE}2.{COLOR_END}Flight Status")
        print(f"{COLOR_PURPLE}3.{COLOR_END}Flight Status and Departure Time")
        choice = int(input(f"{COLOR_YELLOW}Enter 1, 2 or 3:{COLOR_END} ").strip())

        while choice not in [1, 2, 3]:
            print(f"{COLOR_RED}Invalid choice.")
            choice = int(input(f"{COLOR_YELLOW}Enter 1, 2 or 3: ").strip())

        if choice == 1:
            new_time = input(f"{COLOR_YELLOW}Enter new departure time (YYYY-MM-DD HH:MM:SS): ").strip()

            while not is_valid_datetime(new_time):
                print(f"{COLOR_RED}Invalid date format, try agin.")
                new_time = input(f"{COLOR_YELLOW}Enter new departure time (YYYY-MM-DD HH:MM:SS): ").strip()
            new_time_str = datetime.strptime(new_time, frmt).strftime(frmt)

            self.cursor.execute("""UPDATE flights 
                                   SET departure_time = ? 
                                   WHERE flight_id = ?""", (new_time_str, flight_id))

            print("Departure time updated.")
            print(f"{COLOR_END}")
            print(f"{COLOR_LIGHT_BLUE}       UPDATED FLIGHT{COLOR_END}")

            flight_info_df = pd.DataFrame(self.cursor.execute("""SELECT * FROM flights
                                                                 WHERE flight_id = ?""", (flight_id,)).fetchall())
            flight_info_df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(flights)").fetchall()]
            print(tabulate(flight_info_df.set_index('flight_id'), headers='keys', tablefmt='pretty'))

        elif choice == 2:
            new_status = input(f"{COLOR_YELLOW}Enter new flight status from ['Scheduled', 'Active',"
                               " 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']: ").strip().capitalize()

            while new_status not in ['Scheduled', 'Active', 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']:
                print(f"{COLOR_RED}Invalid choice.")
                new_status = input(f"{COLOR_YELLOW}Enter new flight status from ['Scheduled', 'Active',"
                                   " 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']: ").strip().capitalize()

            self.cursor.execute("""UPDATE flights
                                   SET flight_status = ? 
                                   WHERE flight_id = ?""", (new_status, flight_id))
            print(f"{COLOR_YELLOW}Flight status updated.")
            flight_info_df = pd.DataFrame(self.cursor.execute("""SELECT * 
                                                                 FROM flights 
                                                                 WHERE flight_id = ?""", (flight_id,)).fetchall())
            flight_info_df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(flights)").fetchall()]
            print()
            print(f"{COLOR_LIGHT_BLUE}       UPDATED FLIGHT{COLOR_END}")
            print(tabulate(flight_info_df.set_index('flight_id'), headers='keys', tablefmt='pretty'))

        elif choice == 3:
            new_time = input(f"{COLOR_YELLOW}Enter new departure time (YYYY-MM-DD HH:MM:SS): ").strip()

            while not is_valid_datetime(new_time):
                print(f"{COLOR_RED}Invalid date format, try agin.")
                new_time = input(f"{COLOR_YELLOW}Enter new departure time (YYYY-MM-DD HH:MM:SS): ").strip()
            new_time_str = datetime.strptime(new_time, frmt).strftime(frmt)

            self.cursor.execute("""UPDATE flights
                                   SET departure_time = ? 
                                   WHERE flight_id = ?""", (new_time_str, flight_id))
            new_status = input(f"{COLOR_YELLOW}Enter new flight status from ['Scheduled', 'Active',"
                               " 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']: ").strip().capitalize()

            while new_status not in ['Scheduled', 'Active', 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']:
                print(f"{COLOR_RED}Invalid choice.")
                new_status = input(f"{COLOR_YELLOW}Enter new flight status from ['Scheduled', 'Active',"
                                   " 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown']: ").strip().capitalize()

            self.cursor.execute("UPDATE flights SET flight_status = ?, departure_time = ? WHERE flight_id = ?",
                                (new_status, new_time_str, flight_id))
            print(f"{COLOR_YELLOW}Flight status updated.")
            flight_info_df = pd.DataFrame(self.cursor.execute("""SELECT * 
                                                                 FROM flights 
                                                                 WHERE flight_id = ?""", (flight_id,)).fetchall())
            flight_info_df.columns = [i[1] for i in self.cursor.execute(f"PRAGMA table_info(flights)").fetchall()]
            print()
            print(f"{COLOR_LIGHT_BLUE}       UPDATED FLIGHT{COLOR_END}")
            print(tabulate(flight_info_df.set_index('flight_id'), headers='keys', tablefmt='pretty'))

        else:
            pass

        self.conn.commit()