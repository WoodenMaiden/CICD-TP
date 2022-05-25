class City:
    def __init__(self, id, department_code, insee_code, zip_code, name, lat, lon):
        self.id = id
        self.department_code = department_code
        self.insee_code = insee_code
        self.zip_code = zip_code
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_dict(self):
        return {
            "id": self.id,
            "department_code": self.department_code,
            "insee_code": self.insee_code,
            "zip_code": self.zip_code,
            "name": self.name,
            "lat": self.lat,
            "lon": self.lon,
        }
