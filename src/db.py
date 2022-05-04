import os
import psycopg2
import dotenv

from city import City

dotenv.load_dotenv()

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT']
        )

    def create_city_table(self):
        cursor = self.connection.cursor()
        with open('queries/create_city_table.sql') as f:
            sql = f.read()
        cursor.execute(sql)
        self.connection.commit()

    def get_cities(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cities")
        rows = cursor.fetchall()
        return [City(*row) for row in rows]

    def post_city(self, city):
        cursor = self.connection.cursor()

        with open('queries/insert_city.sql') as f:
            sql = f.read()
        cursor.execute(sql.format(
            city.id, 
            city.department_code,
            city.insee_code,
            city.zip_code,
            city.name,
            city.lat,
            city.lon
        ))
        self.connection.commit()