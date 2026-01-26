import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="testuser",
    password="password"
)
mycursor = mydb.cursor()

def findairport(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    mycursor.execute(sql, (icao,))
    row = mycursor.fetchone()

    if row:
        print(f"Airport name: {row[0]}")
        print(f"Location: {row[1]}")
    else:
        print(f"No airport found with ICAO code {icao}")

findairport(input("Enter the ICAO code of an airport: ").upper())