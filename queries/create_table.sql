-- create pilots table
DROP TABLE IF EXISTS pilots;

CREATE TABLE pilots(
    pilot_id VARCHAR(8) PRIMARY KEY,
    pilot_name VARCHAR(100) NOT NULL,
    current_address VARCHAR(255) NOT NULL,
    airman_certificate VARCHAR(50) UNIQUE NOT NULL,
    medical_certificate VARCHAR(50) NOT NULL
);

-- populate pilots table

INSERT INTO pilots VALUES ('NT526887', 'Daniel Williams', '3313 Mathews Inlet West Kristentown, MI 15408', 'RU/GJ/754215V/B', 'YMW-794-000');
INSERT INTO pilots VALUES('DV970448', 'Keith Wheeler', '64747 Murray Track East Matthew, NM 15640', 'IT/WK/162548F/A', 'MHE-816-042');
INSERT INTO pilots VALUES('LH321831', 'Joshua Bruce', '0423 Tamara Brooks Suite 876 Ryanfort, CO 30402', 'JP/BE/644951S/I', 'DQG-450-414');
INSERT INTO pilots VALUES('EI968000', 'Shane Garcia', '55371 Amber Pine Schroedertown, SD 15235', 'RU/XC/793201N/J', 'ZEA-290-666');
INSERT INTO pilots VALUES('JA056521', 'Jessica Jackson', '7780 Elizabeth River Kimberlyview, MI 20477', 'LV/OQ/736293R/U', 'FTK-393-082');
INSERT INTO pilots VALUES('ZJ142471', 'Rebecca Carter', '1685 Mason Creek Apt. 950 Pricechester, WI 64839', 'RU/OB/525738L/E', 'QIU-822-048');
INSERT INTO pilots VALUES('LV393982', 'Tina Miller', '68848 Fisher Flat Suite 887 Lake Beverly, CO 46708', 'JP/ND/289328B/O', 'ONE-328-811');
INSERT INTO pilots VALUES('AJ095036', 'Joshua Morgan', '5781 Martinez Neck Suite 626 East Brittany, OR 16823', 'FR/SN/371936Y/H', 'KIB-379-065');
INSERT INTO pilots VALUES('DU424209', 'Michael Green', '96591 Jenna Crossroad Suite 275 East Amandaland, SD 85089', 'IT/VL/017847T/W', 'YPL-809-105');
INSERT INTO pilots VALUES('TQ234233', 'Gregory Wallace', '892 Andrew Loop Katherineton, RI 92270', 'JP/JQ/549264O/J', 'FSG-404-788');
INSERT INTO pilots VALUES('DC505617', 'Aaron Aguilar', '222 Jackson Spurs Suite 546 Lewismouth, PW 38555', 'RU/OY/380108V/W', 'BMX-983-758');
INSERT INTO pilots VALUES('AP024941', 'Kevin Lee', '3142 Heather Spurs Taylorberg, HI 12471', 'FR/QJ/536966S/U', 'NOR-728-519');
INSERT INTO pilots VALUES('SQ314115', 'Kimberly Huang', '8820 Joseph Neck Apt. 224 Lake Patriciaberg, NM 89016', 'JP/ZC/018141F/X', 'ZDK-561-279');
INSERT INTO pilots VALUES('YY792263', 'Stephen Owens', '86517 Velazquez Harbor Cherylfort, NJ 73196', 'UK/FQ/647564B/E', 'DGJ-067-256');
INSERT INTO pilots VALUES('AR637412', 'James Odonnell', '6617 Peter Mews Danielchester, IN 75968', 'UK/RK/203956A/R', 'RKF-720-599');

-- create Destinations table

DROP TABLE IF EXISTS destinations;

CREATE TABLE destinations(
    airport_code CHAR(3) PRIMARY KEY,
    airport_name VARCHAR(15) NOT NULL,
    city_code VARCHAR(15) NOT NULL
);

-- populate destinations table

INSERT INTO destinations VALUES ('DFW', 'Dallas-Fort Worth International Airport', 'DFW');
INSERT INTO destinations VALUES ('DEN', 'Denver International Airpor', 'DEN');
INSERT INTO destinations VALUES ('PEK', 'Beijing Capital International Airport', 'BJS');
INSERT INTO destinations VALUES ('PKX', 'Beijing Daxing International Airport', 'BJS');
INSERT INTO destinations VALUES ('LHR', 'London Heathrow Airport', 'LON');
INSERT INTO destinations VALUES ('HND', 'Tokyo International Airport', 'TYO');
INSERT INTO destinations VALUES ('ORD', 'Chicago OHare International Airport', 'CHI');
INSERT INTO destinations VALUES ('LAX', 'Los Angeles International Airport', 'LAX');
INSERT INTO destinations VALUES ('CDG', 'Charles de Gaulle International Airport', 'PAR');
INSERT INTO destinations VALUES ('MAD', 'Madrid-Barajas Airport', 'MAD');

-- create cities table
DROP TABLE IF EXISTS cities;

CREATE TABLE cities(
    city_code VARCHAR(3)  PRIMARY KEY,
    city_name VARCHAR(15) NOT NULL,
    country VARCHAR(15) NOT NULL
);

-- populate cities table

INSERT INTO cities VALUES ('DFW','Dallas','US');
INSERT INTO cities VALUES ('DEN', 'Denver', 'US');
INSERT INTO cities VALUES ('BJS','Beijing', 'CH');
INSERT INTO cities VALUES ('SAO', 'Sao Paulo', 'BR');
INSERT INTO cities VALUES ('LON', 'London', 'UK');
INSERT INTO cities VALUES ('TYO', 'Tokyo', 'JP');
INSERT INTO cities VALUES ('CHI', 'Chicago', 'US');
INSERT INTO cities VALUES ('LAX', 'Los Angeles', 'US');
INSERT INTO cities VALUES ('PAR', 'Paris', 'FR');
INSERT INTO cities VALUES ('MAD', 'Madrid', 'ES');

-- create flights table

DROP TABLE IF EXISTS flights;

CREATE TABLE flights(
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_number VARCHAR(15) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    flight_status TEXT CHECK (flight_Status IN ('Scheduled', 'Active', 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown')) NOT NULL,
    airline_code VARCHAR(2) NOT NULL,
    origin_airport_code CHAR(3) NOT NULL,
    destination_airport_code CHAR(3) NOT NULL,
    pilot_id VARCHAR(8) NOT NULL);

-- populate flights table

INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id) VALUES('KX434155', '2025-05-07 03:34:35', '2025-05-07 09:09:35', 'Redirected', 'LX','HND', 'ORD', 'NT526887');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('UE827061', '2025-06-19 18:15:08', '2025-06-19 20:43:04', 'Cancelled', 'CH', 'HND', 'PKX', 'DU424209');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('QV483124', '2025-07-29 16:48:56', '2025-07-30 04:05:30', 'Active', 'QR', 'HND', 'LHR', 'TQ234233');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('WZ675984', '2025-05-22 03:16:51', '2025-05-22 11:36:37', 'Active', 'QR', 'DEN', 'MAD', 'JA056521');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('CF714009', '2025-09-21 03:47:44', '2025-09-21 06:30:59', 'Cancelled', 'QF', 'PKX', 'HND', 'AP024941');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('PP166907', '2025-08-29 00:37:20', '2025-08-29 11:12:00', 'Diverted', 'LX', 'LHR', 'PKX', 'AR637412');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('ZB742741', '2025-06-19 19:55:05', '2025-06-19 23:30:32', 'Cancelled', 'AF', 'HND', 'MAD', 'JA056521');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('PS759346', '2025-05-22 04:04:28', '2025-05-22 09:35:47', 'Cancelled', 'EK', 'HND', 'MAD','DC505617');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('JB199294', '2025-07-04 00:07:59', '2025-07-04 09:32:14', 'Unknown', 'QF', 'HND', 'CDG', 'JA056521');
INSERT INTO flights(flight_number, departure_time, arrival_time, flight_status, airline_code, origin_airport_code, destination_airport_code, pilot_id)  VALUES('ZL194473', '2025-07-21 10:01:48', '2025-07-21 11:58:21', 'Cancelled', 'NH', 'CDG', 'LHR', 'DU424209');

-- create airlines table

DROP TABLE IF EXISTS airlines;

CREATE TABLE airlines(
    airline_code CHAR(2) PRIMARY KEY,
    airline_name VARCHAR(15) NOT NULL);

-- populate airlines table
INSERT INTO airlines VALUES ("LX", "Swiss International Air Lines");
INSERT INTO airlines VALUES ("CX", "Cathay Pacific Airways");
INSERT INTO airlines VALUES ("QR", "Qatar Airways");
INSERT INTO airlines VALUES ("QF", "Qantas Airways");
INSERT INTO airlines VALUES ("AF", "Air France");
INSERT INTO airlines VALUES ("EK", "Emirates");
INSERT INTO airlines VALUES ("NH", "All Nippon Airways");
INSERT INTO airlines VALUES ("JL", "Japan Airlines");
INSERT INTO airlines VALUES ("BR", "EVA Air");
INSERT INTO airlines VALUES ("SQ", "Singapore Airways");