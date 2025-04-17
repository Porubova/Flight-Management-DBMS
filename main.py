import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])

from tabulate import tabulate
from utils.utils import *
from db_creation import create_db
from flights_class import Flights


def main_menu():
    flights = Flights('Flight_Management')

    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input(f"{COLOR_BLUE}Select an option: ")

        try:
            clear_screen()
            if choice == '1':
                create_db()
            elif choice == '2':
                flights.get_stats()
            elif choice == '3':
                flights.add_new_flight()
            elif choice == '4':
                flights.view_flights()
            elif choice == '5':
                flights.update_flight_info()
            elif choice == '6':
                print(tabulate(flights.get_pilots_names(), headers='keys', tablefmt='pretty'))
            elif choice == '7':
                flights.get_pilots_schedules()
            elif choice == '8':
                flights.assign_pilot_flight()
            elif choice == '0':
                print(f"{COLOR_RED}Exiting...")
                break
            else:
                print(f"{COLOR_RED}Invalid choice. Please try again.")
        except Exception as e:
            print(f"{COLOR_RED} Error: {e}")
        prompt_continue()


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        sys.exit(0)