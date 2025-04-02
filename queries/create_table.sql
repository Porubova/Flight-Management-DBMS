-- create Pilots table
DROP TABLE IF EXISTS Pilots;

CREATE TABLE Pilots (
    Pilot_ID VARCHAR(8) PRIMARY KEY,
    Pilot_Name VARCHAR(100) NOT NULL,
    Current_Address VARCHAR(255) NOT NULL,
    Airman_Certificate VARCHAR(50) UNIQUE NOT NULL,
    Medical_Certificate VARCHAR(50) NOT NULL
);

-- populate Pilots table

INSERT INTO Pilots VALUES ('NT526887', 'Daniel Williams', '3313 Mathews Inlet West Kristentown, MI 15408', 'RU/GJ/754215V/B', 'YMW-794-000');
INSERT INTO Pilots VALUES('DV970448', 'Keith Wheeler', '64747 Murray Track East Matthew, NM 15640', 'IT/WK/162548F/A', 'MHE-816-042');
INSERT INTO Pilots VALUES('LH321831', 'Joshua Bruce', '0423 Tamara Brooks Suite 876 Ryanfort, CO 30402', 'JP/BE/644951S/I', 'DQG-450-414');
INSERT INTO Pilots VALUES('EI968000', 'Shane Garcia', '55371 Amber Pine Schroedertown, SD 15235', 'RU/XC/793201N/J', 'ZEA-290-666');
INSERT INTO Pilots VALUES('JA056521', 'Jessica Jackson', '7780 Elizabeth River Kimberlyview, MI 20477', 'LV/OQ/736293R/U', 'FTK-393-082');
INSERT INTO Pilots VALUES('ZJ142471', 'Rebecca Carter', '1685 Mason Creek Apt. 950 Pricechester, WI 64839', 'RU/OB/525738L/E', 'QIU-822-048');
INSERT INTO Pilots VALUES('LV393982', 'Tina Miller', '68848 Fisher Flat Suite 887 Lake Beverly, CO 46708', 'JP/ND/289328B/O', 'ONE-328-811');
INSERT INTO Pilots VALUES('AJ095036', 'Joshua Morgan', '5781 Martinez Neck Suite 626 East Brittany, OR 16823', 'FR/SN/371936Y/H', 'KIB-379-065');
INSERT INTO Pilots VALUES('DU424209', 'Michael Green', '96591 Jenna Crossroad Suite 275 East Amandaland, SD 85089', 'IT/VL/017847T/W', 'YPL-809-105');
INSERT INTO Pilots VALUES('TQ234233', 'Gregory Wallace', '892 Andrew Loop Katherineton, RI 92270', 'JP/JQ/549264O/J', 'FSG-404-788');
INSERT INTO Pilots VALUES('DC505617', 'Aaron Aguilar', '222 Jackson Spurs Suite 546 Lewismouth, PW 38555', 'RU/OY/380108V/W', 'BMX-983-758');
INSERT INTO Pilots VALUES('AP024941', 'Kevin Lee', '3142 Heather Spurs Taylorberg, HI 12471', 'FR/QJ/536966S/U', 'NOR-728-519');
INSERT INTO Pilots VALUES('SQ314115', 'Kimberly Huang', '8820 Joseph Neck Apt. 224 Lake Patriciaberg, NM 89016', 'JP/ZC/018141F/X', 'ZDK-561-279');
INSERT INTO Pilots VALUES('YY792263', 'Stephen Owens', '86517 Velazquez Harbor Cherylfort, NJ 73196', 'UK/FQ/647564B/E', 'DGJ-067-256');
INSERT INTO Pilots VALUES('AR637412', 'James Odonnell', '6617 Peter Mews Danielchester, IN 75968', 'UK/RK/203956A/R', 'RKF-720-599');

-- create Destinaitons table

DROP TABLE IF EXISTS Destinaitons;

CREATE TABLE Destinaitons  (
    Airport_Code CHAR(3) PRIMARY KEY,
    Airport_Name VARCHAR(15) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Country VARCHAR(15) NOT NULL,
    Region VARCHAR(10) 
);

-- populate Destinaitons table

INSERT INTO Destinaitons VALUES ('DFW', 'Dallas-Fort Worth International Airport', 'Dallas','US', 'AMERICAS');
INSERT INTO Destinaitons VALUES ('DEN', 'Denver International Airpor', 'Denver', 'US', 'AMERICAS');
INSERT INTO Destinaitons VALUES ('PEK', 'Beijing Capital International Airport', 'Beijing', 'CH', NULL);
INSERT INTO Destinaitons VALUES ('PKX', 'Beijing Daxing International Airport', 'Beijing', 'CH', NULL);
INSERT INTO Destinaitons VALUES ('LHR', 'London Heathrow Airport', 'London', 'UK', 'EUROPE');
INSERT INTO Destinaitons VALUES ('HND', 'Tokyo International Airport', 'Tokyo', 'JP', NULL);
INSERT INTO Destinaitons VALUES ('ORD', 'Chicago OHare International Airport', 'Chicago', 'US', NULL);
INSERT INTO Destinaitons VALUES ('LAX', 'Los Angeles International Airport', 'Los Angeles', 'US', 'AMERICAS');
INSERT INTO Destinaitons VALUES ('CDG', 'Charles de Gaulle International Airport', 'Paris', 'FR', 'EUROPE');
INSERT INTO Destinaitons VALUES ('MAD', 'Madrid–Barajas Airport', 'Madrid', 'ES', NULL);

-- create Flights table

DROP TABLE IF EXISTS Flights;

CREATE TABLE Flights  (
    Flight_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Flight_Number VARCHAR(15) NOT NULL,
    Departure_Time DATETIME NOT NULL,
    Arrival_Time DATETIME NOT NULL,
    Flight_Status TEXT CHECK (Flight_Status IN ('Scheduled', 'Active', 'Redirected', 'Landed', 'Diverted', 'Cancelled', 'Unknown')) NOT NULL,
    Airline VARCHAR(15) NOT NULL,
    Airport_Code CHAR(3) NOT NULL,
    Pilot_ID VARCHAR(8) NOT NULL);

-- populate Flights table

INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('KX434155', '2025-05-07 03:34:35', '2025-05-07 09:09:35', 'Redirected', 'Swiss International Air Lines', 'ORD', 'NT526887');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('UE827061', '2025-06-19 18:15:08', '2025-06-19 20:43:04', 'Cancelled', 'Cathay Pacific Airways', 'PKX', 'DU424209');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('QV483124', '2025-07-29 16:48:56', '2025-07-30 04:05:30', 'Active', 'Qatar Airways', 'HND', 'TQ234233');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('WZ675984', '2025-05-22 03:16:51', '2025-05-22 11:36:37', 'Active', 'Qatar Airways', 'DEN', 'JA056521');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('CF714009', '2025-09-21 03:47:44', '2025-09-21 06:30:59', 'Cancelled', 'Qantas Airways', 'PKX', 'AP024941');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('PP166907', '2025-08-29 00:37:20', '2025-08-29 11:12:00', 'Diverted', 'Swiss International Air Lines', 'LHR', 'AR637412');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('ZB742741', '2025-06-19 19:55:05', '2025-06-19 23:30:32', 'Cancelled', 'Air France', 'HND', 'JA056521');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('PS759346', '2025-05-22 04:04:28', '2025-05-22 09:35:47', 'Cancelled', 'Emirates', 'HND', 'DC505617');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('JB199294', '2025-07-04 00:07:59', '2025-07-04 09:32:14', 'Unknown', 'Qantas Airways', 'HND', 'JA056521');
INSERT INTO Flights(Flight_Number, Departure_Time, Arrival_Time, Flight_Status, Airline, Airport_Code, Pilot_ID) VALUES('ZL194473', '2025-07-21 10:01:48', '2025-07-21 11:58:21', 'Cancelled', 'All Nippon Airways', 'CDG', 'DU424209');
