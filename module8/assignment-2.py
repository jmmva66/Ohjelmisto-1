import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="testuser",
    password="password"
)
mycursor = mydb.cursor()

def get_airports_by_country(country_code):
    sql = "SELECT COUNT(*), type FROM airport WHERE iso_country = %s GROUP BY type"
    mycursor.execute(sql, (country_code,))
    return mycursor.fetchall()

def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    results = get_airports_by_country(country_code)

    if results:
        print(f"\n\nAirports in {country_code}:")
        for count, airport_type in results:
            print(f"{airport_type} {count} airports")
    else:
        print(f"No airports found for country code '{country_code}'.")


run_country_program()