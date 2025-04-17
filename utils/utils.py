from utils.colours import *
import re

def is_valid_format(s):
    return bool(re.fullmatch(r'[A-Za-z]{2}\d{6}', s))
def is_valid_datetime(s):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    return bool(re.match(pattern, s))

def clear_screen():
    print("\n" * 100)


def prompt_continue():
    input(f"\n{COLOR_YELLOW}Press Enter to return to the main menu...")


def print_banner():
    print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")
    print(f"{COLOR_LIGHT_BLUE}       FLIGHT MANAGEMENT SYSTEM")
    print(f"{COLOR_LIGHT_BLUE}{'=' * 40}")


def print_menu():
    print(f"""
        {COLOR_PURPLE}1.{COLOR_END} Create/Reset DB
        {COLOR_PURPLE}2.{COLOR_END} View stats
        {COLOR_PURPLE}3.{COLOR_END} Add new flight
        {COLOR_PURPLE}4.{COLOR_END} View flights and filter 
        {COLOR_PURPLE}5.{COLOR_END} Update flight details
        {COLOR_PURPLE}6.{COLOR_END} View pilot list
        {COLOR_PURPLE}7.{COLOR_END} View detailed pilot information and schedule
        {COLOR_PURPLE}8.{COLOR_END} Assign pilot to flight
        {COLOR_LIGHT_RED}0.{COLOR_END} Exit
        """)