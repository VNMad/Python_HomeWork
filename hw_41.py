#____________________________________________________________________
#1. Список всех стран
#____________________________________________________________________
import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'test'),
}

try:
    with pymysql.connect(**config) as conn_ich:
        print('Connection opened')
        try:
            with conn_ich.cursor() as cursor:
                cursor.execute("SELECT Name FROM world.country")
                for num, row in enumerate(cursor.fetchall(), 1):
                    print(f'{num}. {row[0]}')
        except pymysql.MySQLError as e:
            print("Query error:", e)

except pymysql.MySQLError as e:
    print("Connection error:", e)

#____________________________________________________________________
#2. Города выбранной страны
#____________________________________________________________________
import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_DATABASE', 'test'),
}

try:
    with pymysql.connect(**config) as conn_ich:
        print('Connection opened')
        try:
            with conn_ich.cursor() as cursor:
                countries = {}
                cursor.execute("SELECT Name, Code FROM world.country")
                for num, row in enumerate(cursor.fetchall(), 1):
                    country_name, country_code = row
                    countries[num] = country_code
                    print(f'{num}. {country_name}')
                while True:
                    try:
                        user_country_number = int(input('Enter the number of Country from the list: '))
                    except ValueError:
                        print('Invalid input. Please enter a number.')
                    else:
                        if user_country_number not in countries.keys():
                            print('Invalid country number. Please try again.')
                            continue
                        else:
                            break
                selected_country_code = countries[user_country_number]
                cursor.execute("""SELECT c.Name, c.Population FROM world.city as c
                                         JOIN world.country as coun ON coun.Code = c.CountryCode
                                         WHERE Code = %s""", (selected_country_code,))
                for num, row in enumerate(cursor.fetchall(), 1):
                    city_name, Population = row
                    print(f'{num}. {city_name} -- {Population}')

        except pymysql.MySQLError as e:
            print("Query error:", e)

except pymysql.MySQLError as e:
    print("Connection error:", e)
