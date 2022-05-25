"""
City module
"""


class City:
    """Representation of the city table in database"""

    def __init__(self, **kwargs):
        self.city_id = kwargs.get("_id")
        self.department_code = kwargs.get("department_code")
        self.insee_code = kwargs.get("insee_code")
        self.zip_code = kwargs.get("zip_code")
        self.name = kwargs.get("name")
        self.lat = kwargs.get("lat")
        self.lon = kwargs.get("lon")

    def get_dict(self):
        """Return a dict representation of the city"""
        return {
            "_id": self.city_id,
            "department_code": self.department_code,
            "insee_code": self.insee_code,
            "zip_code": self.zip_code,
            "name": self.name,
            "lat": self.lat,
            "lon": self.lon,
        }

    def __repr__(self):
        return f"<City {self.name}>"
