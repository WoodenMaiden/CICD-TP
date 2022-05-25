"""Database module"""
import os
import psycopg2
import dotenv

from city import City

dotenv.load_dotenv()


class Database:
    """database class"""

    def __init__(self):
        addr = os.environ.get("CITY_API_DB_URL", "localhost:5432").split(":")

        if len(addr) == 1:
            host, port = addr[0], 5432
        else:
            host, port = addr

        config = {
            "database": os.environ.get("CITY_API_DB_NAME", "postgres"),
            "user": os.environ.get("CITY_API_DB_USER", "postgres"),
            "password": os.environ.get("CITY_API_DB_PWD", "postgres"),
            "host": host,
            "port": port,
        }
        self.connection = psycopg2.connect(**config)

    def create_city_table(self):
        """Create the city table"""
        cursor = self.connection.cursor()
        with open("queries/create_city_table.sql", encoding="UTF-8") as file:
            sql = file.read()
        cursor.execute(sql)
        self.connection.commit()

    def get_cities(self):
        """get cities in db"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cities")
        rows = cursor.fetchall()
        cities = [
            {
                "id": row[0],
                "department_code": row[1],
                "insee_code": row[2],
                "zip_code": row[3],
                "name": row[4],
                "lat": row[5],
                "lon": row[6],
            }
            for row in rows
        ]
        return [City(**city) for city in cities]

    def post_city(self, city):
        """add city in db"""
        cursor = self.connection.cursor()

        with open("queries/insert_city.sql", encoding="UTF-8") as file:
            sql = file.read()
        cursor.execute(
            sql.format(
                city.city_id,
                city.department_code,
                city.insee_code,
                city.zip_code,
                city.name,
                city.lat,
                city.lon,
            )
        )
        self.connection.commit()
