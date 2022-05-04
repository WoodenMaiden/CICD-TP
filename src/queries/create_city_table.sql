CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  department_code VARCHAR(2) NOT NULL,
  insee_code VARCHAR(5),
  zip_code VARCHAR(5),
  name VARCHAR(255) NOT NULL,
  lat FLOAT NOT NULL,
  lon FLOAT NOT NULL
);