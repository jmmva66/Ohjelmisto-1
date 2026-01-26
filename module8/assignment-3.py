import mysql.connector
from geopy.distance import geodesic


mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="testuser",
    password="password"
)

mycursor = mydb.cursor()

def get_airport_coordinates(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    mycursor.execute(sql, (icao,))
    return mycursor.fetchone()


def run_airport_distance():

    icao1 = (input("Enter the ICAO code of the first airport: ").upper())
    coords1 = get_airport_coordinates(icao1)
    icao2 = (input("Enter the ICAO code of the second airport: ").upper())
    coords2 = get_airport_coordinates(icao2)

    distance = float(geodesic(coords1, coords2).kilometers)

    if (coords1 is None):
        print(f"Airport with ICAO code {icao1} not found in the database.")
    elif(coords2 is None):
        print(f"Airport with ICAO code {icao2} not found in the database.")
    else:
        print(f"\n\nDistance between {icao1} and {icao2}: {distance:.2f} kilometers")

run_airport_distance()