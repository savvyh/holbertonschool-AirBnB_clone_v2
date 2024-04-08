-- Prepare a MySQL server
-- Create a database hbnb_dev_db:
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user hbnb_dev (in localhost) with the password be set to hbnb_dev_pwd:
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Set all privileges on the database hbnb_dev_db for hbnb_dev:
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Set SELECT privilege on the database performance_schema for hbnb_dev:
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
