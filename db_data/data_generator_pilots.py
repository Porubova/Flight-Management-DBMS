import os
os.system('pip install faker')
import random
import string
from faker import Faker

fake = Faker()

def generate_names(n):
    """ 
    Generates  a list of pilots names
        args:
        int n - number of generated records
        returns:
        list: list of generated names   
    """
    names = []
    for i in range(n):
        names.append(fake.name())
    return names

def generate_addresses(n):
    """ 
    Generates  a list of pilots addresses
        args:
        int n - number of generated records
        returns:
        list: list of generated addresses    
    """
    addresses = []
    for i in range(n):
        addresses.append(fake.address().replace("\n", " "))
    return addresses
def generate_licence(n):
    # Licence format 'UK/PP/123456D/A' 
    # https://forums.flyer.co.uk/viewtopic.php?t=4203

    """ 
    Generates a list of pilots licences
        args:
        int n - number of generated records
        returns:
        list: list of generated licences    
    """
    licences = []
    for i in range(n):
        country_code = random.choice(["UK", "FR", "RU", "US", "IT", "JP", "LV"])
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        number = ''.join(random.choices(string.digits, k=6))
        letter1 = random.choice(string.ascii_uppercase)
        letter2 = random.choice(string.ascii_uppercase)
        licences.append(f"{country_code}/{letters}/{number}{letter1}/{letter2}")
    return licences

def generate_med_cert(n):
    """ 
    Generates a list of pilots medical certificates
        args:
        int n - number of generated records
        returns:
        list: list of generated certificates  
    """
    certs = []
    for i in range(n):
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers1 = ''.join(random.choices(string.digits, k=3))
        numbers2 = ''.join(random.choices(string.digits, k=3))
        certs.append(f"{letters}-{numbers1}-{numbers2}")
    return certs

def generate_pilot_id(n):
    """ 
    Generates a list of pilots IDs
        args:
        int n - number of generated records
        returns:
        list: list of generated Ids
    """
    ids = []
    for i in range(n):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=6))
        ids.append(f"{letters}{numbers}")
    return ids

ids = generate_pilot_id(15)
names = generate_names(15)
addresses = generate_addresses(15)
licences = generate_licence(15)
med_certs = generate_med_cert(15)

data = zip(ids, names, addresses, licences, med_certs)
for i in data:
    print(i)
print()
print(ids)